import json
from pprint import pprint
import config
import threading
import timeit
import requests
import os

def get_modules(course_id):
    """gets modules from course with course_id"""
    mods = get_request(f"courses/{course_id}/modules")
    modules = {}
    for mod in mods.json():
        name = mod["name"]
        res = get_request(mod["items_url"])
        items = {}
        for item in res.json():
            title = item["title"]
            items[title] = item

        modules[name] = items

    return modules

# def midterm2():
#     id = 68161
#     mods = get_modules(id)
#     archives = mods["Archives"]
#     for name,file in archives.items():
#         if "Midterm2" in name:
#            files.download_file(file["url"]) 

# midterm2()
from requests import Response, HTTPError

def get_request(path, params=None, headers=None) -> Response:
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

    res = requests.get(url, headers=header, params=params, allow_redirects=True)
    check_response(res)
    return res

def get_domain_header():
    """loads domain name and user api token from config and creates the request header from the token"""
    
    domain = config.get_domain()
    token = config.get_token()
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

def check_response(res):
    try: 
        res.raise_for_status()
        #will raise ValueError if either of these exist because they are generated when no access
        # try:
        #     json = res.json()
        #     if not res.json():
        #         json = res.text
        #         if json["message"]:
        #             raise 
        #         json["errors"]
        # except TypeError:
        #     pass
        if res:
            return
    except (AttributeError, HTTPError, ValueError) as e:
        raise CanvasNoAccessError("That page has been disabled for this course")

class CanvasNoAccessError(Exception):
    """When user has no access to a canvas object. Most often because an instructor has not given access to said obj. To check, try checking the class through the browser and see if you can see the object for the class"""
    pass

def get_files(course_id):
    """gets files from course with course_id"""
    # print(course_id)
    root_path = f"courses/{course_id}/"
    res = get_request(root_path + 'files')
    files = {}
    # pprint(res.json())
    for file in res.json():
        files[file["display_name"]] = file
    return files
            #TODO process files and create folders

def get_folders(folder_id, course_id=None):
    """gets folder with folder_id from course with course_id"""

    path = f"folders/{folder_id}"
    if course_id:
        path = f"courses/{course_id}/{path}"

def download_file(url):
    file = get_request(url)
    download = get_request(file.json()["url"])
    # pprint(file.content)
    open(file.json()["display_name"], 'wb').write(download.content)
# import pdfkit

def download_page(course_id, page_name):
    """dowloads a page with page_name from course with course_id as html"""
    with open('page.html', 'w') as page:
        res = get_request(f"/courses/{course_id}/pages/{page_name}")
        page.write(res.json()["body"])
        page.close()

    #to turn html file into pdf with pdfkit
    # pdfkit.from_file('page.html', 'page.pdf')
    # os.remove("page.html")

def get_pages(course_id):
    """gets pages from course course_id"""

    res = get_request(f"courses/{course_id}/pages")
    pages = {}
    for page in res.json():
        pages[page["url"]] = page
    return pages

def get_grades(course_id):
    """gets pages from course course_id"""

    res = get_request(f"courses/{course_id}/assignments")
    grades = res.json()
    # for grade in res.json():
    return grades


# from file_tree import CanvasItem
def get_favorite_courses():
    """gets courses that are favorited"""
    param = {'per_page': 100, 'include': "favorites"}
    path = "courses"
    response = get_request(path, params=param)
    courses = response.json()
    favorite_courses = []
    for course in courses:
        try:
            if course["is_favorite"]:
                favorite_courses.append(course)
        except KeyError:
            continue
    return favorite_courses

def thread_parse(type,name,id,course_data):
    obj = None
    try:
        if type == 'modules':
            obj = get_modules(id)
        elif type == 'files':
            obj = get_files(id)
        elif type == 'pages':
            obj = get_pages(id)
        elif type == 'grades':
            obj = get_grades(id)
        if not obj:
            obj = "Nothing has been posted to this page"
    except CanvasNoAccessError:
        out = f'The page {type} has been disabled for course {name}.'
        # print(out)
        obj = out
    course_data[type] = obj

def thread_init_file_structure():
    """creates easelstructure.json"""
    courses = {}
    hr = '-'*10
    for course in get_favorite_courses():
        name = course["name"]

        # print(f"attempting info for course {name}")
        course_data = { "name": name ,"info": course}
        id = course["id"]

        """For each, if no access then CanvasNoAccessError will be raised. User is notified through print statement and None type is added to file structure"""

        threads = []
        for i in ['pages','files','modules','grades']:
            thread = threading.Thread(target=thread_parse, args=(i,name,id,course_data))
            # thread = asyncio.ensure_future(parse(i,name,id,course_data))
            threads.append(thread)

        # data = await asyncio.gather(*threads)
        for i in range(len(threads)):
            threads[i].start()

        for i in range(len(threads)):
            threads[i].join()
        # print(f"attempting pages for course {name}")

        # print(f"attempting files for course {name}")
        courses[id] = course_data
    with open('easelstructure.json', 'w') as struc:
        struc.write(json.dumps(courses, indent=2))
        struc.close()

"""this exists so you can run core and make it do stuff"""
if __name__ == "__main__":
   # print("async\t\t",timeit.timeit(lambda: asyncio.run(init_file_structure()), number=1))
   print("thread\t\t",timeit.timeit(thread_init_file_structure, number=1))
   # print("norm\t\t", timeit.timeit(norm_init_file_structure, number=1))
   
