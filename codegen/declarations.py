from dataclasses import dataclass, field
from typing import List
import enum
from os import path
import os
import sys
from mako.template import Template
import re

from utils import take_longer
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

DOCUMENTED_TYPE_MAP = {"string": "str", "integer": "int", "number": "int", "float": "float", "boolean": "bool", "datetime": "datetime", "object": "obj", None: "None"}
TYPEMAP = {"string":"String", "boolean":"Boolean", "integer":"Integer","number":"Integer", "datetime":"DateTime", "array":"Array", "object" :"PickleType", None:"None"}

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
    name: str = None
    values: list[str] = field(default_factory=list)

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


@dataclass(slots=True)
class ObjectField:
    name: str = None
    description: str = None
    example: str = None
    type_: str = None
    documented_type: str = None
    primary_key: bool = None
    option_enum: OptionEnum = None

    def as_dict(self):
        attrs = {s: getattr(self, s, None) for s in self.__slots__}
        # replace type_ with type
        del attrs['type_']
        attrs['type'] = self.type_
        return attrs
    
    def set_defaults(self):
        """sets defaults for string fields with values of None"""
        if self.name is None:
            self.name = 'undefined_field_name'
        if self.description is None:
            self.description = NODESC
        if self.example is None:
            self.example = ''
        if self.type_ is None:
            self.type_ = 'unknown_type'
        if self.documented_type is None:
            self.documented_type = 'unknown_type'
        return self

    def merge(self, other):
        self.description = take_longer(self.description, other.description)
        self.example = take_longer(self.example, other.example)
        if self.type_ is None and other.type_ is not None:
            self.type_ = other.type_
            self.documented_type = other.documented_type
        elif other.type_ is not None and self.type_ != other.type_:
            warnings.warn(f"Field {self.name} has conflicting types {self.type_} and {other.type_}.\nTaking {self.type_}")
        # else other is None or self.type_ == other.type_ so do nothing
        self.primary_key = self.primary_key or other.primary_key
        if self.option_enum is None and other.option_enum is not None:
            self.option_enum = other.option_enum
        elif self.option_enum is not None and other.option_enum is not None:
            self.option_enum.values.extend(other.option_enum.values)
            self.option_enum.values = list(set(self.option_enum.values))
        return self

@dataclass(slots=True)
class ObjectDefinition:
    name: str = None
    name_snake: str = None
    description: str = None
    fields: list = field(default_factory=list)
    # relationships = field(default_factory=list)

    def as_dict(self):
        attrs = {s: getattr(self, s, None) for s in self.__slots__}
        # convert fields to dict as well
        attrs['fields'] = [field.as_dict() for field in self.fields]
        return attrs

    @property
    def fields_dict(self):
        return {field.name: field for field in self.fields}

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
    
    @property
    def is_table(self) -> bool:
        """determines whether an object is a table based on whether a field is called id"""
        for field in self.fields:
            if field.name == "id":
                return True
        return False


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
        print(f"Adding id field to {self.name}")
        self.fields.insert(0,ObjectField(name="id", type_="Integer", description=f"The unique identifier of the {self.name}", example="123456", primary_key=True))


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