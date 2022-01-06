import json
import requests
from canvas_file_tree import CanvasFile
from pprint import pprint

config_file = open("canvas_cli_config.json", 'r')
config = json.loads(config_file.read())

def get_domain_header():
    domain = config["info"]["domain"]
    token = config["info"]["token"]
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

def get_favorite_courses():
    domain, header = get_domain_header()
    param = {'per_page': 100, 'include': "favorites"}
    url = f"{domain}courses"
    response = requests.get(url, headers=header, params=param)
    courses = response.json()
    favorite_courses = []
    for course in courses:
        try:
            if course["is_favorite"]:
                favorite_courses.append(course)
        except KeyError:
            continue
    return favorite_courses

def get_course_id(course):
    return course["id"]

def get_course_files(course_id):
    domain, header = get_domain_header()
    url = f"{domain}courses/{course_id}/files"
    response = requests.get(url, headers=header)
    return response.json()

def get_course_name(course):
    return course["course_code"]

def course_file_structure():
    favorite_courses = get_favorite_courses() 
    course_ids = {}
    for course in favorite_courses:
        course_ids[get_course_id(course)] = get_course_name(course)
    root = CanvasFile(name='root', is_file=False)
    root.add_children(list(course_ids.values()))
    return root

if __name__ == "__main__":
    root = course_file_structure()
    tree = root.build_tree()
    for entry in tree:
        print(entry)

