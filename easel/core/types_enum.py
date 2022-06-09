from enum import Enum
import typing

_base_path =  "courses/{course_id}/"

class CanvasType(Enum):
    # values are the singular (not plural) version of the specifiers canvas uses in its api paths 
    COURSE = ("course", "")
    ASSIGNMENT_GROUP = ("assignment_group", globals()["_base_path"])
    ASSIGNMENT = ("assignment",globals()["_base_path"])
    MODULE = ("module",globals()["_base_path"])
    MODULE_ITEM = ("item", globals()["_base_path"] + "modules/{module_id}/")
    PAGE = ("page", globals()["_base_path"])
    SUBMISSION = ("submission", globals()["_base_path"] + "assignments/{assignment_id}/")
    FILE = ("file", globals()["_base_path"])
    FOLDER = ("folder", globals()["_base_path"])

    def __init__(self, type:str, path:str) -> None:
        self.name = type
        self.plural_name = self.name + "s"
        # duplicate for verbosity
        self.table_name = self.plural_name
        self.path = path + self.plural_name

    def item_path(self, course_id:int=None, module_id:int=None, assignment_id:int=None):
        error_str = "required for item path"
        if not course_id:
            raise TypeError(f"{course_id=} {error_str}")
        if self == CanvasType.COURSE:
            #to keep error messages similar
            global _base_path
            return _base_path.format(course_id=course_id)
        elif self == CanvasType.ASSIGNMENT:
            if not assignment_id:
                raise TypeError(f'{assignment_id=} {error_str}')
            return self.path.format(course_id=course_id) + f"/{assignment_id}"
        else:
            return NotImplemented
