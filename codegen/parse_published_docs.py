#!./env/bin/python
from itertools import tee
import re
from pprint import pprint
import os
from os import path
from bs4 import BeautifulSoup
import enum
import requests
from collections import namedtuple
from parse_model_comments import camel_to_snake
# from parse_model_comments import main as get_table_objects
# from parse_model_comments import template_parsed_models as render_table_objects
from declarations import *
from bs4.element import ResultSet, Tag
from typing import Any, List, Tuple, Union

from utils import depluralize

def get_docs_to_parse() -> List[str]:
    with open(DOCS_TO_PARSE_FILE, "r") as docs_to_parse:
        urls = docs_to_parse.readlines()
    return urls

def save_doc_to_file(url, content):
    try:
        os.mkdir(DOWNLOADED_DOCS_DIR)
    except FileExistsError:
        pass
    with open(path.join(DOWNLOADED_DOCS_DIR, path.basename(url)), "w+") as f:
        f.write(content)

def get_doc_page_soup(url: str) -> BeautifulSoup:
    content = None
    if USE_OFFLINE and path.exists(path.join(DOWNLOADED_DOCS_DIR, path.basename(url))):
        content = open(path.join(DOWNLOADED_DOCS_DIR, path.basename(url)), "r").read()
    else:
        page = requests.get(url)
        content = page.content
        save_doc_to_file(url, page.text)
    return BeautifulSoup(content, "html.parser")

def get_objects(page_soup: BeautifulSoup) -> ResultSet:
     return page_soup.find_all("div", class_="object_definition")

def get_object_name(obj_def: Tag) -> str:
    name_tag = obj_def.find("a")
    return name_tag['name']

def get_object_fields(obj_def: Tag) -> List[ObjectField]:
    example_obj = obj_def.find("pre", class_="example code prettyprint")
    txt = example_obj.text
    lines = txt.split('\n')
    fields: list[ObjectField] = []
    description_lines = []
    for line in lines:
        line = line.strip()
        if line.startswith("//"):
            line = line.replace("//","").strip()
            description_lines.append(line)
        match = re.search(OBJ_FIELD_LINE_RE, line)
        if match:
            field = ObjectField()
            field.description = ''.join(description_lines)
            field.name = match.group(1).strip()
            field.example = match.group(2).strip()
            fields.append(field)
            description_lines.clear()
    return fields

def parse_objects(obj_defs: ResultSet) -> List[ObjectDefinition]:
    objects: list[ObjectDefinition] = []
    for obj_def in obj_defs:
        obj = ObjectDefinition()
        obj.name = get_object_name(obj_def)
        obj.fields = get_object_fields(obj_def)
        if not obj.is_table:
            # see documentation in add_id_field function for why this is necessary
            obj.add_id_field()
        objects.append(obj)

    return objects

def get_requests(page_soup: BeautifulSoup) -> ResultSet:
    return page_soup.find_all("div", class_="method_details")

def get_params(req_def: Tag) -> ResultSet:
    return req_def.find_all("tr", class_="request-param")

def get_param_columns(param_def: Tag) -> ResultSet:
    return param_def.find_all("td")

def parse_param_col_description(param_desc: Tag) -> Union[Tuple[str, List[Any]], Tuple[str, List[str]]]:
    value_list = param_desc.find("p", class_="param-values")
    values = []
    if value_list:
        values = [val.text.strip() for val in value_list.extract().find_all(class_="enum")]
    description = param_desc.text.strip()

    return (description, values)

def parse_param_columns(param_cols: ResultSet) -> RequestParameter:
    param_col_dict = {
        'parameter': param_cols[0].text,
        'required': param_cols[1].text == "Required",
        'type_': param_cols[2].text,
    }
    param_col_dict['description'], param_col_dict['allowed_values'] = parse_param_col_description(param_cols[3])
    return RequestParameter(**param_col_dict)

def parse_params(param_defs: ResultSet) -> List[Union[RequestParameter, Any]]:
    req_params = []
    for param_def in param_defs:
        req_param = parse_param_columns(get_param_columns(param_def))
        req_params.append(req_param)
    return req_params


def get_endpoint_and_needs(endpoint_str: str) -> Union[Tuple[str, List[Any]], Tuple[str, List[str]]]:
    """parses the canvas endpoint_str into a string using 
    the format string sintax ('{value}') 
    and a list of the values to be formatted """
    # the values that will be formatted with the correct values when run
    needs = [n.replace(':','') for n in re.findall(CANVAS_FORMAT_VALUE_RE, endpoint_str)]
    link_sep = endpoint_str.split('/')
    for idx, part in enumerate(link_sep):
        if part == ":id":
            """sometimes the docs have a lone :id 
            where a name would be more descriptive"""
            part = part.replace(':','')
            prefix = depluralize(link_sep[idx-1])
            corrected = '_'.join([prefix,part])
            endpoint_str = endpoint_str.replace("/:id", f"/:{corrected}")
            needs[needs.index("id")] = corrected

    py_format_str, _ = re.subn(CANVAS_FORMAT_VALUE_RE, PYTHON_FORMAT_VALUE_RE, endpoint_str) 
    return py_format_str, needs

def get_request_name(req_def: Tag) -> str:
    name_txt = req_def.find("h2", class_="api_method_name").a.text.strip().lower()
    name_txt = name_txt.replace("/","_or_")
    name_txt_words = name_txt.split()
    try:
        name_txt_words.remove("a")
    except ValueError:
        pass
    try:
        name_txt_words.remove("an")
    except ValueError:
        pass
    return '_'.join(name_txt_words)

def parse_requests(req_defs: ResultSet) -> List[Request]:
    requests = []
    for req_def in req_defs:
        req_dict = {
        'name': get_request_name(req_def),
        'parameters': parse_params(get_params(req_def)),
        'description': req_def.p.text.strip()
        }
        req_dict['method'], canv_endpoint = (req_def.find(class_="endpoint").text.strip().split())
        req_dict['endpoint'],req_dict['needs'] = get_endpoint_and_needs(canv_endpoint)
        requests.append(Request(**req_dict))
    return requests

def parse_doc(page_soup: BeautifulSoup) -> Tuple[List[ObjectDefinition], List[Request]]:
    objs = parse_objects(obj_defs=get_objects(page_soup))
    requests = parse_requests(req_defs=get_requests(page_soup))
    return objs, requests

def get_url_name(url):
    return os.path.basename(url).replace(".html", "")

def get_doc_objs_and_requests():
    objects = []
    requests = []
    for url in get_docs_to_parse():
        url_name = get_url_name(url)
        objs, reqs = parse_doc(get_doc_page_soup(url))
        objects += objs
        requests += reqs

    return objects, requests
    # return {"objects":objects, "requests":requests}

# def main() -> None:
#     try: 
#         os.mkdir(PARSED_DOCS_DIR)
#     except FileExistsError:
#         pass
#     objects = []
#     requests = []
#     for url in get_docs_to_parse():
#         url_name = get_url_name(url)
#         objs, requests = parse_doc(get_doc_page_soup(url))
        
#         table_obj_rends: list = get_table_objects()
#         table_obj_rends_dict = dict(map(lambda o: (o.name, o), table_obj_rends))
#         """get renders of parsed objects from models in canvas github repo"""
#         table_objs_to_rend = []
#         objs_to_rend = []
#         for obj in objs:
#             if obj.is_table:
#                 table_objs_to_rend.append(table_obj_rends_dict[obj.name])
#             else:
#                 if table_obj_rends_dict.get(obj.name):
#                     model_fields = table_obj_rends_dict[obj.name].fields
#                     merge_types_from_model(obj.fields, model_fields)
                
#                 objs_to_rend.append(obj)
#         obj_rends = list(render_table_objects(table_objs_to_rend).values()) + render_objects(objs_to_rend)
#         request_rends = render_requests(requests)

#         with open(path.join(PARSED_DOCS_DIR, url_name+".py"), "w") as outfile:
#             for obj_rend in obj_rends:
#                 outfile.write(obj_rend)
#                 outfile.write("\n\n")
            
#             for req_rend in request_rends:
#                 outfile.write(req_rend)
#                 outfile.write("\n\n")

if __name__ == '__main__':
    main()