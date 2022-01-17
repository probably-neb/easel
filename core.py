import json
import requests
from requests import HTTPError
from pprint import pprint
from files import get_files
from courses import get_favorite_courses
from modules import get_modules
from pages import get_pages
from api_request import get_request, check_response, CanvasNoAccessError
import config

def init_file_structure():
    """creates easelstructure.json"""
    courses = {}
    hr = '-'*10
    for course in get_favorite_courses():
        name = course["name"]

        # print(f"attempting info for course {name}")
        course_data = { "name": name ,"info": course}
        id = course["id"]

        """For each, if no access then CanvasNoAccessError will be raised. User is notified through print statement and None type is added to file structure"""

        # print(f"attempting modules for course {name}")
        try:
            modules = get_modules(id)
        except CanvasNoAccessError as e:
            no_access('modules', name)
            modules = "That page has been disabled for this course"
        course_data['modules'] = modules

        # print(f"attempting pages for course {name}")
        try:
            pages = get_pages(id)
        except CanvasNoAccessError as e:
            no_access('pages', name)
            pages = "That page has been disabled for this course"
        course_data['pages'] = pages

        # print(f"attempting files for course {name}")
        try:
            files = get_files(id)
        except CanvasNoAccessError as e:
            no_access('files', name)
            files = "That page has been disabled for this course"
        course_data['files'] = files

        courses[id] = course_data
    with open('easelstructure.json', 'w') as struc:
        struc.write(json.dumps(courses, indent=2))
        struc.close()

def no_access(obj_type, course_name):
    print(f"No access to {obj_type} for course {course_name}.")

"""this exists so you can run core and make it do stuff"""
if __name__ == "__main__":
    init_file_structure()
