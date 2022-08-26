from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from typing import List
import enum
from os import path
import os
import sys
from mako.template import Template
import re

from utils import take_longer, camel_to_snake
import warnings

USE_OFFLINE = True

DIRNAME = path.dirname(path.abspath(__file__))
TEMPLATE_DIRNAME = path.join(DIRNAME, "templates")
GENERATED_CODE_DIRNAME = path.join(DIRNAME, "generated_code")

PARSED_DOCS_DIR = path.join(DIRNAME, "parsed_docs")
DOWNLOADED_DOCS_DIR = path.join(DIRNAME, "downloaded_materials", "docs")
RENDERED_OBJS_FILE = path.join(GENERATED_CODE_DIRNAME, "generated_items_one_file.py")
RENDERED_REQUESTS_FILE = path.join(GENERATED_CODE_DIRNAME, "generated_requests_one_file.py")
DOWNLOADED_MODEL_FILES = path.join(DIRNAME, "downloaded_model_files/")
PARSED_MODELS_FILE = path.join(DIRNAME, "parsed_models.json")

DOCS_TO_PARSE_FILE = path.join(DIRNAME, "docs_to_parse.txt")

SQL_OBJECT_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIRNAME , "sql_object.mako"))
OBJECT_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIRNAME, "object.mako"))
REQUEST_MAKO_TEMPLATE = Template(filename=path.join(TEMPLATE_DIRNAME, "request.mako"))


OBJ_FIELD_LINE_RE = re.compile(r'"(.*)": "*([^"]*)"*.*,*')
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
    _PYTHON_TYPEMAP = {"string": "str", "integer": "int", "number": "int", "float": "float", "boolean": "bool", "datetime": "datetime", "object": "obj", "any" : "Any", None: "None"}
    _SQL_TYPEMAP = {"string":"String", "boolean":"Boolean", "integer":"Integer","number":"Integer", "datetime":"DateTime", "array":"JsonObject(List)", "object" :"JsonObject(Dict)", "any": "String", None:"None"}
    # _type_: str = ""
    #NOTE: "object" in models refers to dicts and values can be other objects, arrays are lists
    """ a list of additional strings to include in the repr (usually only relevent for sql repr"""
    sql_args: List[str] = field(default_factory=list, init=False)
    type_: str

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
    
    def basic_repr(self):
        # intented to be overloaded in subclasses
        return self.type_

@dataclass
class ForeignKeyFieldInit(FieldInit):
    class_name: str = ""
    field_name: str = ""

    def __post_init__(self):
        self.sql_args.append(f"ForeignKey('{self.class_name}.{self.field_name}')")

@dataclass
class EnumFieldInit(FieldInit):
    type_: str = "enum" # type_ will be overwritten with enum definition
    enum_name: str = None

    def __post_init__(self):
        # make enum_name required
        if not self.enum_name:
            raise ValueError("enum_name must be set")

    def py_repr(self):
        return super().py_repr(py_type_=self.enum_name)

    def sql_repr(self):
        sql_type_ = f"Enum({self.enum_name})"
        return super().sql_repr(sql_type_=sql_type_)

@dataclass
class RefFieldInit(FieldInit):
    """for references to other classes (sql orm relationships and normal py references i.e. parent: ParentClass = None)"""
    type_: str = "$ref"
    class_name: str = ""
    """should be table name for sql objects"""
    back_populates: str = ""
    secondary: str = ""

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
    _data_type_: str = None

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
    # TODO: create type_ object that handles all type logic
    type_: InitVar[str] = None
    """migrated to InitVar after type_ was replaced by init to help ease migration"""
    init: FieldInit = None
    # documented_type: str = None
    # primary_key: bool = None
    _option_enum: OptionEnum = None

    def __post_init__(self, type_):
        # allow for type_ to be passed resulting in creation of default InitField with type_
        if type_ is not None:
            if self.init is not None:
                raise ValueError("cannot specify both type and init")
            else:
                self.init = FieldInit(type_=type_)

    @property
    def option_enum(self):
        return self._option_enum

    @option_enum.setter
    def option_enum(self, value):
        self._option_enum = value
        if value is not None:
            self.init = EnumFieldInit(enum_name=value.name)

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
        if self.init is None:
            self.init = FieldInit(type_='unknown_type')
        if self.name is None:
            self.name = 'undefined_field_name'
        elif self.name == "id":
            self.init.sql_args.append("primary_key=True")
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
        if self.init is None:
            self.init = other.init
        elif other.init is not None and type(self.init) != type(other.init):
            warnings.warn(f"Field {self.name} has conflicting init types {type(self.init).__name__} and {type(other.init).__name__}.\nTaking {type(self.init).__name__}")
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

    @property
    def fields_dict(self):
        return {field.name: field for field in self.fields}
    
    @property
    def name_snake(self):
        return camel_to_snake(self.name)

    @property
    def is_table(self) -> bool:
        """determines whether an object is a table based on whether a field is called id"""
        for field in self.fields:
            if field.name == "id":
                return True
        return False
    
    def cleanup(self):
        """ fully preps the object for rendering"""
        if not self.is_table:
            self.add_id_field()
        self.set_defaults()
        self.organize_fields()
        self.rectify_foriegn_key_fields()
    
    def render(self):
        """ default render is to render as an sql orm class"""
        return SQL_OBJECT_MAKO_TEMPLATE.render(obj=self)
    
    def organize_fields(self):
        """
        - moves id field to the front if present
        - moves _id foreign key fields to the end if present
        - moves {field_name} and {field_name}_id fields to the end and puts them after one another
        """
        if "id" in self.fields_dict.keys():
            if len(self.fields) > 0 and self.fields[0].name != "id":
                idx = self.fields.index(self.fields_dict["id"])
                id_field = self.fields.pop(idx)
                self.fields.insert(0, id_field)
        for field in self.fields:
            if field.name.endswith("_id"):
                # move {field_name}_id field to the end
                idx = self.fields.index(field)
                self.fields.pop(idx)
                self.fields.append(field)
                # move {field_name} field to the end
                if field.name[:-3] in self.fields_dict.keys():
                    idx = self.fields.index(self.fields_dict[field.name[:-3]])
                    id_field = self.fields.pop(idx)
                    self.fields.append(id_field)

    def as_dict(self):
        attrs = {s: getattr(self, s, None) for s in self.__slots__}
        # convert fields to dict as well
        attrs['fields'] = [field.as_dict() for field in self.fields]
        return attrs

    def merge(self, other):
        if self.name != other.name:
            warnings.warn(f"attempting to merge {self.name} with {other.name}\n taking {self.name}")
        self.description = take_longer(self.description, other.description)

        for field in other.fields:
            if field.name in self.fields_dict:
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
        self.fields.insert(0,ObjectField(name="id", type_="Integer", description=f"The unique identifier of the {self.name}", example="123456"))

@dataclass
class RequestParameter:
    parameter: str = None
    required: bool = None
    type_: str = None
    description: str = None
    allowed_values: list[str] = field(default_factory=list)

class MethodEnum(str, enum.Enum):
    POST = "POST"
    GET = "GET"
    PATCH = "PATCH"
    DELETE = "DELETE"
    PUT = "PUT"

@dataclass
class Request:
    """methods describe possible requests"""
    name: str = None
    description: str = None
    endpoint: str = None
    method: "MethodEnum" = None
    needs: list[str] = field(default_factory=list)
    parameters: list[RequestParameter] = field(default_factory=list)