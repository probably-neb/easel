from asyncio.events import get_running_loop
from cement import App
import json
import config
import timeit
import aiofile
import aiohttp
import asyncio
from pprint import pprint
from typing import Dict

user_id = 0

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
    # for page in pages:
        #page only object without "id". this avoids checking type every time searching with id
        # page["id"] = page["url"]
    return pages

async def get_modules(course_id,session):
    """gets modules from course with course_id"""
    mods = await get_request(f"courses/{course_id}/modules", session)
    modules = await mods.json()
    items = {}
    for mod in modules:
        module_id = mod["id"]
        res = await get_request(f"courses/{course_id}/modules/{module_id}/items", session)
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
#NOT WORKING

async def get_user_id(session):
    """how to do persisistently store this?"""
    user = await get_request("users/self",session)
    id = await user.json()
    global user_id
    user_id =  id["id"]

async def get_assignment_submission_data(session, course_id, assignment_id, user_id):
    url = f'courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}'
    sub = await get_request(url, session)
    return await sub.json()

async def get_assignments(course_id, session):
    """gets pages from course course_id"""
    params = {'include': '"score_statistics","submission", "assignments"'}
    res = await get_request(f"courses/{course_id}/assignment_groups", session,params=params)
    assignment_groups = await res.json()
    # from cement import App
    # with App('easel') as app:
    # global user_id
    # if not user_id:
    #     await get_user_id(session)
    # revised_assignment_groups = {}
    # for assignment_group in assignment_groups:
    #     revised_assignment_groups[assignment_group["id"]] = assignment_group
    # for grade in res.json():
    # print("assignment_groups:",type(assignment_groups))
    # for assignment_group in assignment_groups:
    #     print("assignment group:",type(assignment_group))
    #     print("assignments:",type(assignment_group["assignments"]))
    # verbose declaration of keys for converting list of dicts to one dictionary with sub dictionaries
    # assignment_group_key = "id"
    # assignment_key = "id"
    # for assignment_group in assignment_groups:
    #     assignment_dict = await list_of_dicts_to_dict(assignment_group["assignments"], assignment_key)
    #     assignment_group["assignments"] = assignment_dict
    # assignment_groups = await list_of_dicts_to_dict(assignment_groups, assignment_group_key)
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

async def parse(type,id, tables, session):
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
    return {type: obj}


async def get_course_data(id, tables, session):
    threads = []
    """For each, if no access then CanvasNoAccessError will be raised. User is notified through print statement and None type is added to file structure"""

    for type in ['pages','files','modules','assignment_groups']:
        if not tables.get(type):
            tables[type] = []
        thread = asyncio.create_task(parse(type,id,tables, session))
        threads.append(thread)
    course_items = await asyncio.gather(*threads)
    # [{'type' : [items of type]}, {'type2' : [items of type2]}...]
    return course_items

async def get_course_structure():
    """creates easelstructure.json"""
    tables = {}
    hr = '-'*10
    async with aiohttp.ClientSession() as session:
        favorite_courses = await get_favorite_courses(session)
        tables["courses"] = favorite_courses
        course_tasks = []
        # loop = asyncio.get_running_loop()
        # global user_id 
        # user_id = loop.create_future()
        # course_tasks.append(asyncio.create_task(get_users(session)))
        for course in favorite_courses:
            course_task = asyncio.create_task(get_course_data(course["id"], tables, session))
            course_tasks.append(course_task)
            # course["type"] = "course"
        courses_items = await asyncio.gather(*course_tasks)
        # for course_items in courses_items:
        #     tables |= course_items
        return tables
