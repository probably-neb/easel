from pprint import pprint
from api_request import get_request, check_response
import files

def get_modules(course_id):
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

# def midterm2():
#     id = 68161
#     mods = get_modules(id)
#     archives = mods["Archives"]
#     for name,file in archives.items():
#         if "Midterm2" in name:
#            files.download_file(file["url"]) 

# midterm2()
