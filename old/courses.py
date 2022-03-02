from api_request import *

# from file_tree import CanvasItem
def get_favorite_courses():
    """gets courses that are favorited"""
    param = {'per_page': 100, 'include': "favorites"}
    path = "courses"
    response = get_request(path, params=param)
    check_response(response)
    courses = response.json()
    favorite_courses = []
    for course in courses:
        try:
            if course["is_favorite"]:
                favorite_courses.append(course)
        except KeyError:
            continue
    return favorite_courses
