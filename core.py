import json
import requests
# from file_tree import CanvasItem
from pprint import pprint

config_file = open("easel.json", 'r')
config = json.loads(config_file.read())

def get_request(path, params=None, headers=None):
    domain, header = get_domain_header()
    if headers:
        header |= headers
    if not path.startswith("https://"):
        url = domain + path
    else:
        url = path
    return requests.get(url, headers=header, params=params)

def get_domain_header():
    domain = config["info"]["domain"]
    token = config["info"]["token"]
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

def get_favorite_courses():
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

def get_course_files(course_id, type="folders"):
    path = f"courses/{course_id}/{type}"
    response = get_request(path)
    return response.json()

def get_folder(folder_id, course_id=None):
    path = f"folders/{folder_id}"
    if course_id:
        path = f"courses/{course_id}/{path}"
    return get_request(path)

def init_file_structure():
    courses = {}
    for course in get_favorite_courses():
        course_data = { "name": course["name"],"info": course}
        courses[course["id"]] = course_data
    with open('easelstructure.json', 'w') as struc:
        struc.write(json.dumps(courses, indent=2))
        struc.close()

if __name__ == "__main__":
    init_file_structure()
    
