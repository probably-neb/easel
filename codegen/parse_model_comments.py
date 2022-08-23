#!./env/bin/python
"""Parses canvas api documentation and generates SQLAlchemy orm code based on results"""
import os
import sys
import json
import re
from pprint import pprint
import requests
import concurrent.futures
from mako.template import Template
import enum
from itertools import repeat

from typing import List, Union, Dict, Optional, Any

from declarations import *
from io import TextIOWrapper

from utils import camelToSnake, snake_to_camel

# _capitalizer = re.compile(r'_(.)')

def get_ifnn_or_empty(thing: Any) -> Optional[Any]:
    """ignores empty strings as well as None values"""
    return thing if thing else None

def get_file_links():
    """Returns a list of filename : extractedurl for scraping"""
    owner = "instructure"
    repo_name = "canvas-lms"
    path = "app/controllers"
    temtemplate_path = "https://api.github.com/repos/:owner/:repo_name/contents/:path"
    temtemplate_path = re.sub(r":(\w+)", r"{\1}", template_path)
    url_path = temtemplate_path.format(owner=owner, repo_name=repo_name, path=path)
    print("Attempting to download:",url_path)
    res = requests.get(url_path)
    # pprint(res.json())
    files = []
    for file in res.json():
        if file["type"] == "file":
            # print(file["name"], file["download_url"])
            files.append(file["download_url"])
    return files

def get_extracted_models_from_text(lines):
    extracted_models = []
    cur = ""
    in_extracted_model = False
    parens = 0
    for line in lines:
        if not line.startswith("#"):
            continue
        if not in_extracted_model and "@model" in line:
            in_extracted_model = True
            # cur = re.sub(r"#\s*@model ","", line)
            # cur = cur.strip()
            # extracted_models[cur] = ""
            cur = ""
        elif in_extracted_model: #elif to skip model line
            line = line.lstrip("#")
            line = line.strip()
            cur += line
            parens+=line.count("{")
            parens-=line.count("}")
            if parens == 0:
                extracted_models.append(cur)
                in_extracted_model = False
    return extracted_models

def get_extracted_models_from_remote_file(file_link) -> list[Dict]:
    res = requests.get(file_link)
    lines = res.text.split("\n")
    models = get_extracted_models_from_text(lines)

    return models

def get_extracted_models_from_local_file(file_path, dir_path) -> list[Dict]:
    with open(dir_path + file_path, "r") as file:
        lines = file.readlines()
        models = get_extracted_models_from_text(lines)
    return models

def get_extracted_models_from_local_dir():
    files = [f for f in os.listdir(DOWNLOADED_MODEL_FILES) if f.endswith(".rb")]
    extracted_models = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for extracted_model in executor.map(get_extracted_models_from_local_file, files, repeat(DOWNLOADED_MODEL_FILES)):
            extracted_models+=extracted_model # += because get_model_from_controller_link returns a list
    return extracted_models

def get_extracted_models_from_remote_dir():
    file_links = get_file_links()
    extracted_models = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for extracted_model in executor.map(get_extracted_models_from_remote_file, file_links):
            extracted_models+=extracted_model # += because get_model_from_controller_link returns a list
    return extracted_models

def get_jsoned_models_from_save_file(save_file: TextIOWrapper) -> List[Dict[str, Any]]:
    models = json.load(save_file)
    return models

def json_models(extracted_models):
    """ converts stringified model to a dict using json.loads()"""
    jsoned_models = []
    jsoned_models = [*map(json.loads, extracted_models)]
    return jsoned_models

def store_jsoned_models(store_file, jsoned_models):
    json.dump(jsoned_models, store_file, indent=2)

def format_ref(ref: str) -> str:
    return f'$ref -> {ref}'

def format_array_type(items: Optional[Union[Dict[str, str], Dict[str, Union[str, Dict[str, str]]]]]) -> Optional[str]:
    if not items:
        return None
    item_type = TYPEMAP[items.get('type')]
    if item_type == "None" and items.get('$ref'):
        item_type = format_ref(items.get('$ref'))

    # i think items is showing up because i return items here
    elif item_type == "Array":
        item_type = f"{format_array_type(items['items'])}"
    return f"Array : {item_type}"

def parse_field(field_name: str, jsoned_field: Dict[str, Any], jsoned_model_name: str) -> ObjectField:
        field = ObjectField()
        field.name = field_name.replace('-','_')
        field.documented_type = jsoned_field.get('type')
        mapped_type = TYPEMAP[field.documented_type]
        if mapped_type == "None" and jsoned_field.get('$ref'):
            field.type_ = format_ref(jsoned_field['$ref'])
        else:
            field.type_ = mapped_type
        field.description = get_ifnn_or_empty(jsoned_field.get('description'))
        field.example = get_ifnn_or_empty(jsoned_field.get('example'))
        if type(field.example) != str:
            # when the fields type is an integer it is stored as an integer type 
            # but we need it as a string
            field.example = str(field.example)
        field.primary_key = field.name == "id"
        field.option_enum = None

        if jsoned_field.get('allowableValues'):
            field.option_enum = OptionEnum()
            field.option_enum.name = snake_to_camel(field.name) + "AllowedValues"
            field.option_enum.name.capitalize()
            field.option_enum.values = jsoned_field['allowableValues']['values']

        if mapped_type == "Array":
            items = jsoned_field.get('items')
            array_type = format_array_type(items)
            field.type_ = array_type
            if field.type_ is None:
                print(f"WARNING: field {field.name} of item {jsoned_model_name} has type \"Array\" but no specified item types\n", jsoned_field)
        elif field.option_enum is not None:
            field.type_ = "Enum"
        return field
    
def parse_fields(properties_dict: Dict[str, Any], model_name: str) -> List[Union[Any, ObjectField]]:
    parsed_fields = []
    for f_name, jsoned_field in properties_dict.items():
        parsed_field = parse_field(f_name, jsoned_field, model_name)
        parsed_fields.append(parsed_field)
    return parsed_fields

def parse_model(jsoned_model: Dict[str, Any]) -> ObjectDefinition:
    model = ObjectDefinition()

    model.name = jsoned_model.get('id')
    model.name_snake = camelToSnake(model.name)

    model.fields = parse_fields(jsoned_model.get('properties'), model.name)
    model.description = jsoned_model.get('description')
    
    return model

def parse_models(jsoned_models: List[Dict[str, Any]]) -> List[ObjectDefinition]:
    parsed_models = [*map(parse_model, jsoned_models)]
    return parsed_models

def store_parsed_models(parsed_models):
    json.dump(parsed_models, PARSED_MODELS_FILE, indent=2)

def tuple_models(extracted_models):
    """ convert all parsed (dict and renamed) models to namedparse objects for easier use in temtemplate"""
    models = []
    for extracted_model in extracted_models:
        extracted_model['fields'] = [ObjectField(**field) for field in extracted_model['fields']]
        model = ObjectDefinition(**extracted_model)
        models.append(model)
    return models

def store_templated_models_together(templated_models: dict):
    with open(TEMPLATED_MODELS_DIR, "w") as out:
        for templated_model in templated_models.values():
            out.write(stored_model)
            out.write("\n\n" + "#"*30 + "\n\n")
        print("successfully generated items")

def store_templated_models_individually(templated_models: dict):
    try:
        os.mkdir(GENERATED_MODELS_DIR)
    except FileExistsError:
        pass
    for model_name, templated_model in templated_models.items():
        path = os.path.join(GENERATED_MODELS_DIR, model_name + ".py")
        with open(path, "w") as out:
            out.write(templated_model)

def get_parsed_models_online():
    extracted_models = get_extracted_models_from_remote_file()
    jsoned_models = json_models(extracted_models)
    parsed_models = parse_models(jsoned_models)
    store_parsed_models(parsed_models)
    print(f"downloaded docs into {PARSED_MODELS_FILE}")
    return parsed_models

def get_parsed_models_offline() -> List[ObjectDefinition]:
    print(f"using existing {PARSED_MODELS_FILE}")
    with open(PARSED_MODELS_FILE, "r+") as store_file:
        jsoned_models = get_jsoned_models_from_save_file(store_file)
    parsed_models = parse_models(jsoned_models)
    return parsed_models

def get_model_objs() -> List[ObjectDefinition]:
    if USE_OFFLINE:
        return get_parsed_models_offline()
    else:
        return get_parsed_models_online()

if __name__ == '__main__':
    parsed_models = get_model_objs()
    templated_models = template_parsed_models(parsed_models)
    # store_templated_models_individually(templated_models)
    

