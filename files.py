from courses import get_favorite_courses
from pprint import pprint
from api_request import get_request, check_response
import requests

def get_files(course_id):
    """gets files from course with course_id"""
    # print(course_id)
    root_path = f"courses/{course_id}/"
    res = get_request(root_path + 'files')
    check_response(res)
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
    pprint(file.content)
    open(file.json()["display_name"], 'wb').write(download.content)
