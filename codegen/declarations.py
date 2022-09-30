from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from typing import List
import enum
from os import path
import os
import sys
from mako.template import Template
from mako.lookup import TemplateLookup
import re

from utils import take_longer, camel_to_snake, snake_to_camel, capitalize, to_classname
import warnings

USE_OFFLINE = True

ROOT_DIR = path.dirname(path.abspath(__file__))

DOWNLOADED_MATERIALS_DIR = path.join(ROOT_DIR, "downloaded_materials")
DOWNLOADED_MODEL_FILES = path.join(DOWNLOADED_MATERIALS_DIR, "model_files")
DOWNLOADED_DOCS_DIR = path.join(DOWNLOADED_MATERIALS_DIR, "docs")
DOWNLOADED_JSON_DIR = path.join(DOWNLOADED_MATERIALS_DIR, "json_definitions")

GENERATED_CODE_DIR = path.join(ROOT_DIR, "generated_code")
RENDERED_DOC_OBJS_FILE = path.join(GENERATED_CODE_DIR, "doc_objs.py")
RENDERED_MODEL_OBJS_FILE = path.join(GENERATED_CODE_DIR, "model_objs.py")
RENDERED_OBJS_FILE = path.join(GENERATED_CODE_DIR, "generated_items_one_file.py")
RENDERED_REQUESTS_FILE = path.join(GENERATED_CODE_DIR, "generated_requests_one_file.py")

OBJECTS_FILE = path.join(GENERATED_CODE_DIR, "objects.json")
DOC_OBJS_FILE = path.join(GENERATED_CODE_DIR, "doc_objs.json")
MODEL_OBJS_FILE = path.join(GENERATED_CODE_DIR, "model_objs.json")
REQUESTS_FILE = path.join(GENERATED_CODE_DIR, "requests.json")
PARSED_MODELS_FILE = path.join(ROOT_DIR, "parsed_models.json")
DOCS_TO_PARSE_FILE = path.join(ROOT_DIR, "docs_to_parse.txt")

TEMPLATE_DIR = path.join(ROOT_DIR, "templates")
SQL_OBJECT_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIR , "sql_object.mako"))
OBJECT_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIR, "object.mako"))
REQUEST_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIR, "request.mako"))
LOOKUP = TemplateLookup(directories=TEMPLATE_DIR)
API_V1_CLIENT_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIR, "api_v1_client.mako"), lookup=LOOKUP)

CANVAS_FORMAT_VALUE_RE = re.compile(r':([^/]*)')
PYTHON_FORMAT_VALUE_RE = r'{\1}'
PYTHON_FORMATTED_VALUES_RE = re.compile(r'{([^}]*)')
RE_ARRAY_TYPE = re.compile(r'Array : (.*)')
RE_REF_TYPE = re.compile(r'$ref -> (.*)')

NODESC = "No Description Provided"

# USE_OFFLINE = False
@dataclass
class OptionEnum:
    name: str # name required for setting init in objectfield
    values: list[str] = field(default_factory=list)
    
    # @property
    # def name_snake(self):
    #     return camel_to_snake(self.name)

# class RelationShipSide(enum.Enum):
#     MANY = "many"
#     ONE = "one"
#     UNKNOWN = "unknown"

# @dataclass
# class Relationship:
#     local_field_name: str = None
#     side_type: RelationShipSide = RelationShipSide.UNKNOWN
#     other_class_name: str = None
#     other_field_name: str = None

@dataclass
class FieldInit:
    """the [py,sql]_repr fields format how the field will be initialized in the python and sql code"""
    # both of these map from the documented model types to the named type
    _PYTHON_TYPEMAP = {"string": "str", "integer": "int", "number": "int", "float": "float", "boolean": "bool", "datetime": "datetime", "object": "obj", "any" : "Any", None: "None", "void": "None"}
    _SQL_TYPEMAP = {"string":"String", "boolean":"Boolean", "integer":"Integer","number":"Integer", "datetime":"DateTime", "array":"JsonObject(List)", "object" :"JsonObject(Dict)", "any": "String", None:"None"}
    # _type_: str = ""
    #NOTE: "object" in models refers to dicts and values can be other objects, arrays are lists
    """ a list of additional strings to include in the repr (usually only relevent for sql repr"""
    type_: str
    sql_args: List[str] = field(default_factory=list, init=False)
    _data_type_: str = "default"

    # @property
    # def type_(self):
    #     return self._type_  
    
    # @type_.setter
    # def type_(self, value):
    #     self._type_ = value
    
    @property
    def py_type_(self):
        # get or default to 
        return self._PYTHON_TYPEMAP.get(self.type_, self.type_)
    #TODO: add setters for type_ properties for more flexibility
    
    @property
    def sql_type_(self):
        return self._SQL_TYPEMAP.get(self.type_, self.type_)
    
    def sql_args_repr(self):
        # insert empty string at beginning for leading comma
        if self.sql_args and self.sql_args[0] != "":
            self.sql_args.insert(0, "")
        return ", ".join(self.sql_args)
    
    def py_repr(self, py_type_=None):
        if py_type_ is None:
            py_type_ = self.py_type_
        return f"{py_type_}"
    
    def sql_repr(self, sql_type_=None):
        if sql_type_ is None:
            sql_type_ = self.sql_type_
        return f"Column({sql_type_}{self.sql_args_repr()})"
    
    def __str__(self):
        return self.py_repr()
    
    def basic_repr(self):
        # intented to be overloaded in subclasses
        return self.type_

@dataclass
class ForeignKeyFieldInit(FieldInit):
    class_name: str = ""
    field_name: str = ""
    _data_type_: str = "foreign_key"

    def __post_init__(self):
        self.sql_args.append(f"ForeignKey('{self.class_name}.{self.field_name}')")

@dataclass
class EnumFieldInit(FieldInit):
    type_: str = "enum" # type_ will be overwritten with enum definition
    name: str = None
    _data_type_: str = "enum"
    values: List[str] = field(default_factory=list)

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value + "AllowedValues"

    #TODO: names should be snake case in fields, but camel case in Requests ( if not in objects)
    def __post_init__(self):
        # make enum_name required
        if not self.name:
            raise ValueError("enum_name must be set")
    
    def enum_def(self):
        if not self.values:
            raise ValueError("values must be set")
        return f"{self.name} = enum.Enum('{self.name}', {self.values})"

    def py_repr(self):
        return super().py_repr(py_type_=self.name)

    def sql_repr(self):
        sql_type_ = f"Enum({self.name})"
        return super().sql_repr(sql_type_=sql_type_)

@dataclass
class RefFieldInit(FieldInit):
    """for references to other classes (sql orm relationships and normal py references i.e. parent: ParentClass = None)"""
    type_: str = "$ref" # placeholder
    class_name: str = ""
    """should be table name for sql objects"""
    back_populates: str = ""
    secondary: str = ""
    _data_type_: str = "ref"

    def __post_init__(self):
        if not self.class_name and not self.type_:
            # one of class_name or type_ must be set
            raise ValueError("class_name must be set")
        elif not self.class_name:
            # set class_name to type_ if type_ is set
            self.class_name = self.type_
        kwformat = lambda kw: f"{kw}='{getattr(self, kw)}'"
        if self.back_populates != "":
            self.sql_args.append(kwformat("back_populates"))
        if self.secondary != "":
            self.sql_args.append(kwformat("secondary"))

    def py_repr(self):
        return super().py_repr(py_type_=self.class_name)
    
    def sql_repr(self):
        return f"relationship('{self.class_name}'{super().sql_args_repr()})"

@dataclass
class JsonFieldInit(FieldInit):
    """for json fields"""
    type_: str = None
    # override type_ to remove from init
    _data_type_: str = "json"

    def sql_repr(self, py_repr_str):
        repr_ = super().sql_repr(sql_type_="JsonObject")
        # document type in comment
        return repr_ + f'\n"""{py_repr_str}"""'

@dataclass
class ListJsonFieldInit(JsonFieldInit):
    """for json list fields"""
    _data_type_: str = "list"
    item_type_: FieldInit = None

    def __post_init__(self):
        if self.item_type_ is None:
            raise ValueError("item_type_ must be set")
    
    def py_repr(self):
        return f'List[{self.item_type_.py_repr()}]'
    
    def sql_repr(self):
        return super().sql_repr(self.py_repr())
        

@dataclass
class DictJsonFieldInit(JsonFieldInit):
    """for json dict fields"""
    key_type_: FieldInit = None
    value_type_: FieldInit = None
    """ the level of array nesting of the field
        e.g. 0: int, 1: List[int], 2: List[List[int]]
        simplifies formatting of lists """
    # both sql and py typing will use python typing format. This is initallized during post init as such
    _data_type_: str = "dict"

    def __post_init__(self):
        if bool(self.key_type_) != bool(self.value_type_): # logical xor
            # one of key or value is none
            raise ValueError("key_type_ and value_type_ must both be set")
    
    def py_repr(self):
        return f'Dict[{self.key_type_.py_repr()}, {self.value_type_.py_repr()}]'
    
    def sql_repr(self):
        return super().sql_repr(self.py_repr())

@dataclass(slots=True)
class ObjectField:
    name: str = None
    description: str = None
    example: str = None
    """migrated to InitVar after type_ was replaced by init to help ease migration"""
    type_: FieldInit = None
    # documented_type: str = None
    # primary_key: bool = None

    @property
    def is_enum(self):
        return type(self.type_) is EnumFieldInit

    @property
    def enum_description(self):
        if self.is_enum:
            return f'"""Enum for the allowed values of the {self.name} field"""'
        else:
            raise ValueError("field is not an enum")

    def as_dict(self):
        attrs = {s: getattr(self, s, None) for s in self.__slots__}
        # replace type_ with type
        # del attrs['type_']
        # attrs['type'] = self.type_
        return attrs
    
    def set_defaults(self):
        """sets defaults for string fields with values of None"""
        if self.description is None:
            self.description = NODESC
        if self.example is None:
            self.example = ''
        # if self.type_ is None:
        #     self.type_ = 'unknown_type'
        if self.type_ is None:
            self.type_ = FieldInit(type_='unknown_type')
        if self.name is None:
            self.name = 'undefined_field_name'
        elif self.name == "id":
            self.type_.sql_args.append("primary_key=True")
        # if self.documented_type is None:
        #     self.documented_type = 'unknown_type'
        return self

    def merge(self, other):
        self.description = take_longer(self.description, other.description)
        self.example = take_longer(self.example, other.example)
        # if self.type_ is None and other.type_ is not None:
        #     self.type_ = other.type_
        #     self.documented_type = other.documented_type
        # elif other.type_ is not None and self.type_ != other.type_:
        #     warnings.warn(f"Field {self.name} has conflicting types {self.type_} and {other.type_}.\nTaking {self.type_}")
        if self.type_ is None:
            self.type_ = other.type_
        elif other.type_ is not None and type(self.type_) != type(other.type_):
            warnings.warn(f"Field {self.name} has conflicting init types {type(self.type_).__name__} and {type(other.type_).__name__}.\nTaking {type(self.type_).__name__}")
        # else other is None or self.type_ == other.type_ so do nothing
        if self.option_enum is None and other.option_enum is not None:
            self.option_enum = other.option_enum
        elif self.option_enum is not None and other.option_enum is not None:
            self.option_enum.values.extend(other.option_enum.values)
            self.option_enum.values = list(set(self.option_enum.values))
        return self

# slots to prevent accidental adding of attributes
@dataclass(slots=True)
class ObjectDefinition:
    name: str = None
    description: str = None
    fields: list = field(default_factory=list)
    # relationships = field(default_factory=list)
    model_json: dict = None
    docs_html: str = None

    @property
    def fields_dict(self):
        return {field.name: field for field in self.fields}
    
    @property
    def name_snake(self):
        return camel_to_snake(self.name)

    @property
    def is_table(self) -> bool:
        """determines whether an object is a table based on whether a field is called id"""
        return "id" in self.fields_dict.keys()
    
    def cleanup(self):
        """ fully preps the object for rendering"""
        if not self.is_table:
            self.add_id_field()
        self.set_defaults()
        self.organize_fields()
        self.rectify_foriegn_key_fields()

    
    def render(self):
        """ default render is to render as an sql orm class"""
        self.cleanup()
        return SQL_OBJECT_MAKO_TEMPLATE.render(obj=self)
    
    def organize_fields(self):
        """
        - moves id field to the front if present
        - moves _id foreign key fields to the end if present
        - moves {field_name} and {field_name}_id fields to the end and puts them after one another
        - moves relationship fields to the end if present
        """
        def move_field(field, index):
            self.fields.remove(field)
            if index == -1:
                self.fields.append(field)
            else:
                self.fields.insert(index, field)
        # move id field to the front if present
        if "id" in self.fields_dict.keys():
            if len(self.fields) > 0 and self.fields[0].name != "id":
                move_field(self.fields_dict["id"], 0)
        # move _id foreign key fields to the end if present
        for field in self.fields:
            if field.name.endswith("_id"):
                # move {field_name}_id field to the end
                move_field(field, -1)
                # move {field_name} field to the end
                if field.name[:-3] in self.fields_dict.keys():
                    move_field(self.fields_dict[field.name[:-3]], -1)
        # move relationship fields to the end if present
        for field in self.fields:
            if type(field.type_) is RefFieldInit:
                move_field(field, -1)


    def as_dict(self):
        attrs = {s: getattr(self, s, None) for s in self.__slots__}
        # convert fields to dict as well
        attrs['fields'] = [field.as_dict() for field in self.fields]
        return attrs

    def merge(self, other):
        if self.name != other.name:
            warnings.warn(f"attempting to merge {self.name} with {other.name}\n taking {self.name}")
        self.description = take_longer(self.description, other.description)
        if other.docs_html is not None and self.docs_html is None:
            self.docs_html = other.docs_html
        if other.model_json is not None and self.model_json is None:
            self.model_json = other.model_json

        for field in other.fields:
            if field.name in self.fields_dict.keys():
                if field != self.fields_dict[field.name]:
                    self.fields_dict[field.name].merge(field)
                # fields are identical, do nothing
            else:
                self.fields.append(field)
        return self
    
    def rectify_foriegn_key_fields(self):
        """ sometimes {field_name} and {field_name}_id fields point to the opposite thing they should 
        e.g. user field is foreign key and user_id is integer"""
        pass
        # TODO: once type_ has been migrated to fieldinit use type of fieldinit to identify foreign key fields and ref fields
        # for field in self.fields:
        #     if field.name.endswith('_id'):


    #TODO: classmethod that identifies relationships and adds backrefs 
    # and possibly adds fields to backref too
    
    def set_defaults(self):
        """sets defaults for string fields with values of None"""
        if self.name is None:
            self.name = 'undefined_object_name'
        if self.description is None:
            self.description = NODESC
        if self.fields is None:
            self.fields = []
        else:
            for field in self.fields:
                field.set_defaults()
        return self
    
    def add_id_field(self):
        """adds an id field to the object.
        this is done to easily make the object into a sql table 
        and avoid storing objects within other tables as strings"""
        print(f"Adding id field to {self.name}")
        self.fields.insert(0,ObjectField(name="id", type_=FieldInit("integer"), description=f"The unique identifier of the {self.name}", example="123456"))


@dataclass(slots=True)
class RequestParameter:
    name: str = None
    required: bool = None
    type_: FieldInit = None
    description: str = None
    allowed_values: list[str] = field(default_factory=list)
    object_: str = None

    def __str__(self):
        return f"{self.param_repr()}: {self.type_.py_repr()} {'= None' if self.required else ''}"
    
    def param_repr(self):
        if self.object_ is not None:
            return f"{self.object_}_{self.name}"
        else:
            return self.name

class MethodEnum(str, enum.Enum):
    POST = "POST"
    GET = "GET"
    PATCH = "PATCH"
    DELETE = "DELETE"
    PUT = "PUT"

@dataclass(slots=True)
class Request:
    """methods describe possible requests"""
    name: str = None
    description_: str = None
    notes: str = None
    summary: str = None
    endpoint: str = None
    method: "MethodEnum" = None
    parameters: list[RequestParameter] = field(default_factory=list)
    return_type: FieldInit = None
    #TODO: return from function for non get return types should return success or failure
    #TODO: creating parameters dict

    @property
    def description(self):
        """modify getter to return the best description between
        the description_, and notes fields"""
        return take_longer(self.description_, self.notes)
    
    @description.setter
    def description(self, value):
        self.description_ = value

    @property
    def classname(self):
        return to_classname(self.name)

    def sorted_params(self):
        """puts required parameters first"""
        return sorted(self.parameters, key=lambda param: (param.required, param.name))

    def param_repr(self):
        params = self.sorted_params()
        return ", ".join(str(param) for param in params)
    
    def param_field_repr(self):
        params = self.sorted_params()
        return "\n".join(f"{param.name}: {param.type_.py_repr()}" for param in params)
    
    def render(self):
        #TODO: replace \n in description with \n\t to fix indenting
        # (Dont actually modify the description make copy)
        return REQUEST_MAKO_TEMPLATE.render(req=self)


@dataclass(slots=True)
class ObjectGroup:
    group_name: str
    objects: List[ObjectDefinition] = field(default_factory=list)
    requests: List[Request] = field(default_factory=list)

    @property
    def classname(self):
        return to_classname(self.group_name)

    def sort_alphabetically(self):
        self.objects.sort(key=lambda obj: obj.name)
        self.requests.sort(key=lambda req: req.name)
    
    @classmethod
    def sort_all_alphabetically(cls, groups):
        for group in groups:
            group.sort_alphabetically()
        groups.sort(key=lambda group: group.group_name)

    @classmethod
    def render_api_client(self, object_groups):
        self.sort_all_alphabetically(object_groups)
        return API_V1_CLIENT_MAKO_TEMPLATE.render(object_groups=object_groups)