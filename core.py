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
import threading

def parse(type,name,id,course_data):
    obj = None
    try:
        if type == 'modules':
            obj = get_modules(id)
        elif type == 'files':
            obj = get_files(id)
        elif type == 'pages':
            obj = get_pages(id)
        if not obj:
            obj = "Nothing has been posted to this page"
    except CanvasNoAccessError:
        out = f'The page {type} has been disabled for course {name}.'
        print(out)
        obj = out
    course_data[type] = obj

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

        threads = []
        for i in ['pages','files','modules']:
            thread = threading.Thread(target=parse, args=(i,name,id,course_data))
            threads.append(thread)

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
    init_file_structure()
