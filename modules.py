import core
from pprint import pprint

def get_modules(course_id=72755):
    mods = core.get_request(f"courses/{course_id}/modules")
    modules = {}
    for mod in mods.json():
        name = mod["name"]
        items = core.get_request(mod["items_url"])
        modules[name] = items.json()
    pprint(modules)

        


get_modules()
