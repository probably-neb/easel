import json
from pprint import pprint
import config
import asyncio
import timeit
import requests
import aiohttp
import aiofile

async def download_page(course_id, page_name,session):
    """dowloads a page with page_name from course with course_id as html"""
    with open('page.html', 'w') as page:
        res = await get_request(f"/courses/{course_id}/pages/{page_name}", session)
        page.write(await res.json()["body"])
        page.close()

async def get_pages(course_id,session):
    """gets pages from course course_id"""
    res = await get_request(f"courses/{course_id}/pages", session)
    pages = {}
    for page in await res.json():
        pages[page["url"]] = page
    return pages

async def get_modules(course_id,session):
    """gets modules from course with course_id"""
    mods = await get_request(f"courses/{course_id}/modules", session)
    modules = {}
    for mod in await mods.json():
        name = mod["name"]
        res = await get_request(mod["items_url"], session)
        items = {}
        for item in await res.json():
            title = item["title"]
            items[title] = item
        modules[name] = items
    return modules

async def get_files(course_id,session):
    """gets files from course with course_id"""
    # print(course_id)
    root_path = f"courses/{course_id}/"
    res = await get_request(root_path + 'files', session)
    files = {}
    # pprint(res.json())
    for file in await res.json():
        files[file["display_name"]] = file
    return files

async def get_folders(folder_id,session, course_id=None):
    """gets folder with folder_id from course with course_id"""

    path = f"folders/{folder_id}"
    if course_id:
        path = f"courses/{course_id}/{path}"

async def download_file(url,session):
    file = await get_request(url, session)
    download = await get_request(file.json()["url"],session)
    # pprint(file.content)
    open(file.json()["display_name"], 'wb').write(download.content)

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

async def get_grades(course_id, session):
    """gets pages from course course_id"""

    res = await get_request(f"courses/{course_id}/assignments", session)
    grades = await res.json()
    # for grade in res.json():
    return grades

import config

async def get_request(path, session, params=None, headers=None, ):
    """sends a get request
    path: the http path to the object i.e course/{course_id}/modules/{modules_id}
        path can start with https://[domain] or not
    """
    domain, header = get_domain_header()
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
    
    domain = config.get_domain()
    token = config.get_token()
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

from aiohttp import ClientResponseError
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
    except (AttributeError, ClientResponseError, ValueError) as e:
        raise CanvasNoAccessError("That page has been disabled for this course")

class CanvasNoAccessError(Exception):
    """When user has no access to a canvas object. Most often because an instructor has not given access to said obj. To check, try checking the class through the browser and see if you can see the object for the class"""
    pass


async def parse(type,name,id,session):
    obj = None
    # print(f"attempting:   {' '*(6-len(type))}[ {type} ]{' '*(7-len(type))}   for course:   {name}")
    try:
        if type == 'modules':
            obj = await get_modules(id, session)
        elif type == 'files':
            obj = await get_files(id, session)
        elif type == 'pages':
            obj = await get_pages(id, session)
        elif type == 'grades':
            obj = await get_grades(id, session)
        if not obj:
            obj = "Nothing has been posted to this page"
    except CanvasNoAccessError:
        out = f'The page {type} has been disabled for course {name}.'
        # print(out)
        obj = out
    return type,obj

async def get_course_data(course, session):
    name = course["name"]
    id = course["id"]
    course_data = { "id": id ,"info": course}

    """For each, if no access then CanvasNoAccessError will be raised. User is notified through print statement and None type is added to file structure"""
    threads = []
    for i in ['pages','files','modules','grades']:
        thread = asyncio.create_task(parse(i,name,id,session))
        threads.append(thread)

    data = await asyncio.gather(*threads)
    for type, obj in data:
        course_data[type] = obj
    return (name, course_data)
from typing import Dict, Any


async def init_file_structure():
    """creates easelstructure.json"""
    courses = {}
    hr = '-'*10
    async with aiofile.async_open('easelstructure.json', 'w') as struc:
        async with aiohttp.ClientSession() as session:
            favorite_courses = await get_favorite_courses(session)
            course_tasks = []
            for course in favorite_courses:
                # print(course["name"], hr, sep='\n')
                course_task = asyncio.create_task(get_course_data(course,session))
                course_tasks.append(course_task)
            courses_data = await asyncio.gather(*course_tasks)
            for id,course_data in courses_data:
                courses[id] = course_data
                
            # pprint(courses)
            
            await struc.write(json.dumps(courses, indent=2))

            await session.close()

# def course_structure(courses_data):
#     for id, course_data in courses_data:
#         print(id, course_data["name"])

"""this exists so you can run core and make it do stuff"""
if __name__ == "__main__":
   print("async\t\t",timeit.timeit(lambda: asyncio.run(init_file_structure()), number=1))
