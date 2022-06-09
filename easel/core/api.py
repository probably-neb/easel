from asyncio.events import get_running_loop 
from cement import App
import time
import aiohttp
import asyncio
from pprint import pprint
from typing import Dict
import requests
from cement.utils import fs
import os
import hashlib
from collections import OrderedDict
from typing import Callable
from tinydb.table import Document
from tinydb import Query
from bs4 import BeautifulSoup
from rich.progress import track
import rich 

user_id = 0
append_time = 0.0
domain = None
header = None

def html_to_md(html):
    return BeautifulSoup(html, features='html.parser').get_text('\n')

# used to avoid passing session around, for organization
class Requests:
    def __init__(self, app, headers:dict={}, domain:str="", api_path:str="/api/v1/"):
        self.headers =headers
        self.domain = domain
        self.api_path = api_path
        self.app = app

    async def __aenter__(self):
        self.loop = asyncio.get_event_loop()
        self._session: aiohttp.ClientSession = aiohttp.ClientSession(base_url=self.domain, raise_for_status=True, headers=self.headers)
        return self

    async def get_courses(self):
        """gets courses that are favorited"""
        params = {"per_page": 100, "include": "favorites"} #,"syllabus_body","public_description","total_scores","current_grading_period_scores","grading_periods","term","course_progress","sections","storage_quota_used_mb","passback_status","favorites","teachers","observed_users","concluded"'}
        course_task = asyncio.create_task(self._session.get(self.api_path + "courses", params=params))
        response: aiohttp.ClientResponse = await course_task
        courses: list[dict] = await response.json()
        favorite_courses = []
        for course in track(sequence=courses, description="Updating Courses..."):
            if course.get("is_favorite"):
                course['type'] = 'canvas'
                id = course['id']
                names = []
                # keys that canvas stores different names under
                for name_option in ["name", "friendly_name", "course_code"]:
                    name = course.get(name_option)
                    if name is not None:
                        names.append({'name' : name, 'type' : name_option})
                #TODO: when adding links if 'links' is empty add whatever link as default
                course['links'] = {'default' : self.domain + f"/courses/{id}"}
                course['names'] = names
                self.app.log.info(f"Found Favorite Course: {id}: {names}")
                # store = asyncio.to_thread(self.app.db.table("courses").upsert, Document(course, doc_id=course["id"]))
                # await store
                self.app.db.table("courses").upsert, Document(course, doc_id=course["id"])
                favorite_courses.append(course)
        return favorite_courses

    async def get_assignment_group_assignments(self, course_id: int, group_id: int):
        params = {'include': '"score_statistics","submission"'}
        task = asyncio.create_task(self._session.get(self.api_path + f"courses/{course_id}/assignment_groups/{group_id}/assignments", params=params))
        result: aiohttp.ClientResponse = await task
        group_assignments = await result.json()
        return group_assignments

    async def get_assignment_groups(self, course_id: int):
        """gets pages from course course_id"""
        params = {'include': '"score_statistics","submission", "assignments"'}
        # params = {"include": "assignments"}
        task = asyncio.create_task(self._session.get(self.api_path + f"courses/{course_id}/assignment_groups",params=params))
        result: aiohttp.ClientResponse = await task
        assignment_groups = await result.json()

        # why does canvas include copy of assignment in submission?
        for group in track(assignment_groups, description=f"Updating Assignments for course with ID: {course_id}"):
            self.app.log.info(f"Syncing Assignment Group '{group['name']}' in course: {course_id}")
            if not group.get('assignments'):
                group_task = asyncio.create_task(self.get_assignment_group_assignments(course_id=course_id, group_id=group['id']))
                group['assignments'] = await group_task
            for assignment in group['assignments']:
                # change to submissions if downloading multiple submissions
                assignment['course_id'] = course_id
                del assignment['submission']['assignment']
                html: str = assignment.get('description')
                if html:
                    assignment['description_md'] = html_to_md(html)
                del assignment['secure_params']
                
            group['course_id'] = course_id

            #This probably isn't safe
            # store = asyncio.run_in_executor(self.app.db.table('assignments').upsert, Document((group), doc_id=group['id']))
            # await store
            self.app.db.table('assignments').upsert(Document((group), doc_id=group['id']))

        return assignment_groups

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

# async wrapper
def wrap_async(async_func: Callable):
    def wrap(*args, **kwargs):
        return asyncio.run(async_func(*args, **kwargs))
    return wrap

class CanvasApi:
    def __init__(self,app):
        self.app = app
        self.header: dict = {"Authorization": 'Bearer ' + app.config.get('easel','token')}
        self.domain: str = 'https://' + app.config.get('easel','domain')
        self.api_path = '/api/v1/'
        self.path = self.domain + self.api_path
    
    @wrap_async
    #TODO: better name (called in dbfuncs)
    async def sync_with_api(self, types: list, ids:list[int]=[]):
        async with Requests(headers=self.header, domain=self.domain,app=self.app) as api:
            # course_info:list = []

            # BLOCKING
            # if we should update courses or we need course ids for other updates
            if "courses" in types or not len(self.app.db.table("courses")) > 0:
                courses: list[dict] = await api.get_courses()
            if not ids:
                ids = list(map(lambda doc: doc.doc_id, self.app.db.table('courses').search(Query().type == "canvas")))
            tasks = []
            if 'assignments' in types:
                for id in ids:
                    task: asyncio.Task = asyncio.create_task(api.get_assignment_groups(id))
                    tasks.append(task)

            await asyncio.gather(*tasks)
                # assignments: list[dict] = await api.get_assignments()
            # store list of course names by id in 
            # self.app.db.upsert(Document({'course_info': course_info},doc_id=2))

    def get_domain_header(self):
        return (self.domain, self.header)

# The `ignore` and `ignore_permanently` URLs can be used to update the user's preferences on what items will be displayed. Performing a DELETE request against the `ignore` URL will hide that item from future todo item requests, until the item changes. Performing a DELETE request against the `ignore_permanently` URL will hide that item forever.
    def get_todo_items(self):
        items =  self.api_request('users/self/todo').json()
        for item in items:
            if item.get('assignment') is not None:
                st = time.time()
                if self.app.db:
                    item['assignment']['description_text'] = html_to_md(item['assignment']['description'])
                    self.app.db.table('assignments').upsert((Document({'description_text' : item['assignment']['description_text']}, doc_id=item['assignment']['id'])))
                et = time.time()
                self.app.log.info(f'text conversion took {(et - st):.4} seconds')
        return items

    def get_upcoming(self):
        items = self.api_request('/users/self/upcoming_events').json()
        todo_list = {}
        for item in items:
            if item.get('assignment') is not None:
                st = time.time()
                if self.app.db:
                    item['assignment']['description_text'] = html_to_md(item['assignment']['description'])
                    self.app.db.table('assignments').upsert((Document({'description_text' : item['assignment']['description_text']}, doc_id=item['assignment']['id'])))
                et = time.time()
                # self.app.log.info(f'text conversion took {(et - st):.4} seconds')
        return items

    def submit_assignment(self, course_id, assignment_id, path):
        path = fs.abspath(path)
        size = os.path.getsize(path)
        url = self.domain + f'/courses/{course_id}/assignments/submissions/self/files/{assignment_id}'
        name = os.path.basename(file_path)
        response = requests.post(url=url, params={'name' : name, 'size' : size}, headers=self.header)
        response.raise_for_status()
        upload_info = response.json()
        upload_url = upload_info['upload_url']
        upload_params = upload_info['upload_params']
        # file must be last entry in parameters
        # ordered_params = OrderedDict()
        # ordered_params |= upload_params
        file={'file' : open(path, 'rb')}
        upload_response = requests.post(url=url, params=upload_params, files=file)
        upload_response.raise_for_status()
        if upload_response.status_code >= 300:
            requests.get(url, headers={"Content-Lenght" : '0'}.update(self.header))


    def check_response(self, res):
        try: 
            res.raise_for_status()
        except (AttributeError,aiohttp.ClientResponseError, ValueError):
            raise CanvasNoAccessError("That page has been disabled for this course")

    # avoid setting up session for non async request
    def api_request(self, path, params=None, headers=None):
        """sends a get request
        path: the http path to the object i.e course/{course_id}/modules/{modules_id}
            path can start with https://[domain] or not
        """
        param = {'per_page': 100, 'include': "favorites"}
        # domain, header = get_domain_header()
        if params:
            param |= params
            # print(param)
        header = self.header
        if headers:
            header |= headers
        if not path.startswith("https://"):
            path = self.domain + self.api_path + path
        response = requests.get(path, headers=header, params=param, allow_redirects=True)
        self.check_response(response)
        return response

#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
#################################
##                             ##
##   ####   #     ###    #  #  ##
##  #    #  #     #  #   #  #  ##
##  #    #  #     #   #  #  #  ##
##  #    #  #     #  #         ##
##   ####   ##### ###    #  #  ##
##                             ##
#################################
async def list_of_dicts_to_dict(lst, key):
    """ converts list of dictionaries to a new dictionary with each dictionary as a sub dictionrary corresponding to the value of the given key
    ex. ex_list = [{"id" : 123},{"id" : 456}]
    list_of_dicts_to_dict(ex_list, "id") ->{123: {"id" : 123}, 456: {"id" : 456}} """
    new_dict = {}
    for dict in lst:
        if not isinstance(dict, Dict):
            raise TypeError("Sub dictionary is not a dictionary. Found when converting list of dictionaries to dictionary")
        if not dict.get(key):
            raise KeyError()
        new_dict[dict[key]] = dict
    return new_dict

async def download_page(course_id, page_name,session):
    """dowloads a page with page_name from course with course_id as html"""
    with open('page.html', 'w') as page:
        res = await get_request(f"/courses/{course_id}/pages/{page_name}", session)
        page.write(await res.json()["body"])
        page.close()

async def get_pages(course_id,session):
    """gets pages from course course_id"""
    res = await get_request(f"courses/{course_id}/pages", session)
    pages = await res.json()
    for page in pages:
        # page only object without "id". this avoids checking type every time searching with id
        hash = hashlib.sha256(page["url"].encode('utf8'))
        #takes the first 9 bits (guaruntees result is not more than a 32bit int) which is hopefully different enough.
        #TODO: collision checking with these generated ids
        id = int(str(int(hash.hexdigest(),base=16))[0:9])
        page["id"] = id
    return pages

async def get_modules(course_id,session):
    """gets modules from course with course_id"""
    params = {'include': '"items","content_details"'}
    mods = await get_request(f"courses/{course_id}/modules", session, params=params)
    modules = await mods.json()
    items = {}
    for mod in modules:
        if mod.get("items") is None:
            res = await get_request(mod["items_url"], session)
            items = await res.json()
            mod["items"] = items
    return modules

async def get_files(course_id,session,search_term=None):
    """gets files from course with course_id"""
    root_path = f"courses/{course_id}/"
    param=None
    if search_term:
        param={"search_term":search_term}
    res = await get_request(root_path + 'files',session, params=param)
    files = await res.json()
    return files

async def get_folders(folder_id,session, course_id=None):
    """gets folder with folder_id from course with course_id"""

    path = f"folders/{folder_id}"
    if course_id:
        path = f"courses/{course_id}/{path}"

#NOT WORKING
async def download_file(course_id, file_id ,session):
    file = await get_request(f"courses/{course_id}/files/{file_id}", session)
    file_data = await file.json()
    download = await get_request(file_data["url"],session)
    # pprint(file.content)
    download_content = await asyncio.StreamReader.read(download.content)
    from aiofile import async_open
    async with async_open(file_data["display_name"], 'wb') as newFile:
        await newFile.write(download_content)

async def get_assignments(course_id, session):
    """gets pages from course course_id"""
    params = {'include': '"score_statistics","submission", "assignments"'}
    res = await get_request(f"courses/{course_id}/assignment_groups", session,params=params)
    assignment_groups = await res.json()

    # why does canvas include copy of assignment in submission?
    for group in assignment_groups:
        for assignment in group['assignments']:
            # change to submissions if downloading multiple submissions
            del assignment['submission']['assignment']

    return assignment_groups

async def get_users(session):
    user = await get_request("users/self/", session)
    user_dat = await user.json()
    user_dat["user"] = True
    return user_dat

async def get_favorite_courses(session):
    """gets courses that are favorited"""
    param = {'per_page': 100, 'include': "favorites"}
    path = "courses"
    response =  await get_request(path, session, params=param)
    courses = await response.json()
    favorite_courses = []
    for course in courses:
        try:
            if course["is_favorite"]:
                favorite_courses.append(course)
        except KeyError:
            continue
    return favorite_courses

async def get_request(path, session, params=None, headers=None, ):
    """sends a get request
    path: the http path to the object i.e course/{course_id}/modules/{modules_id}
        path can start with https://[domain] or not
    """
    param = {'per_page': 100, 'include': "favorites"}
    global header
    global domain
    if domain is None and header is None:
        domain, header = get_domain_header()
    if params:
        param |= params
        # print(param)
    if headers:
        header |= headers
    if not path.startswith("https://"):
        url = domain + path
    else:
        url = path
    response = await session.get(url, headers=header, params=params,allow_redirects=True)
    await check_response(response)
    # t1 = time.time()
    # t2 = time.time()
    # global append_time
    # append_time += t2 - t1
    return response

def get_domain_header():
    """loads domain name and user api token from config and creates the request header from the token"""
    with App('easel') as app:
        domain = app.config.get('easel','domain')
        token = app.config.get('easel','token')
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

class CanvasNoAccessError(Exception):
    """When user has no access to a canvas object. Most often because an instructor has not given access to said obj. To check, try checking the class through the browser and see if you can see the object for the class"""
    pass

async def check_response(res):
    try: 
        res.raise_for_status()
        # will raise ValueError if either of these exist because they are generated when no access
        # try:
        #     json = res.json()
        #     if not res.json():
        #         json = res.text
        #         # if not json["message"]:
        #         #     raise AttributeError
        #          # json["errors"]
        # except TypeError:
        #     pass
        if res:
            return
    except (AttributeError,aiohttp.ClientResponseError, ValueError) as e:
        raise CanvasNoAccessError("That page has been disabled for this course")

async def parse(type,id,tables, session):
    obj = []
    try:
        if type == 'modules':
            obj = await get_modules(id, session)
        elif type == 'files':
            obj = await get_files(id, session)
        elif type == 'pages':
            obj = await get_pages(id, session)
        elif type == 'assignment_groups':
            obj = await get_assignments(id, session)
        if not obj:
            obj = []
    except CanvasNoAccessError:
        obj = []
    for item in obj:
        # item["type"] = type
        item["course_id"] = id
    tables[type] += obj
    # return {type: obj}

async def get_course_data(id,tables,session):
    threads = []
    """For each, if no access then CanvasNoAccessError will be raised. User is notified through print statement and None type is added to file structure"""

    for type in ['pages','files','modules','assignment_groups']:
        if not tables.get(type):
            tables[type] = []
        thread = asyncio.create_task(parse(type,id,tables,session))
        threads.append(thread)
    # course_items = await asyncio.gather(*threads)
    await asyncio.gather(*threads)
    # [{'type' : [items of type]}, {'type2' : [items of type2]}...]
    # comp = {}
    # for dict in course_items:
    #     comp.update(dict)
    # return comp

def rec_print_type(obj):
    if not isinstance(obj, str):
        if isinstance(obj, dict):
            return {key:"..." for key in obj.keys()}
        if isinstance(obj, list):
            return [rec_print_type(sub) for sub in obj]
    return "str"

async def get_course_structure(ndomain, nheader):
    """creates easelstructure.json"""
    global header
    global domain
    header = nheader
    domain = ndomain
    tables = {}
    hr = '-'*10
    async with aiohttp.ClientSession() as session:
        favorite_courses = await get_favorite_courses(session)
        tables["courses"] = favorite_courses
        course_tasks = []
        for course in favorite_courses:
            course_task = asyncio.create_task(get_course_data(course["id"],tables,session))
            course_tasks.append(course_task)

        courses_items = await asyncio.gather(*course_tasks)
        # print(rec_print_type(courses_items))
        # for type in ['pages','files','modules','assignment_groups']:
        #     tables[type] = []
        #     tables[type] += [course_item[type] for course_item in courses_items]
        return tables
