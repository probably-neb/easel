from pprint import pprint
from api_request import get_request, check_response

def get_modules(course_id=72755):
    """gets modules from course with course_id"""

    mods = get_request(f"courses/{course_id}/modules")
    check_response(mods)
    modules = {}
    for mod in mods.json():
        name = mod["name"]
        res = get_request(mod["items_url"])
        check_response(res)
        items = {}
        for item in res.json():
            title = item["title"]
            items[title] = item

        modules[name] = items

    return modules
