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
INDEX_URL = 'https://canvas.instructure.com/doc/api/index.html'
BASE_URL = path.dirname(INDEX_URL)
OBJ_FIELD_LINE_RE = re.compile(r'"(.*)":\s*(.*)[,]$')

def get_docs_to_parse() -> List[str]:
    urls = []
    if path.exists(DOCS_TO_PARSE_FILE):
    #     with open(DOCS_TO_PARSE_FILE, "r") as f:
    #         urls = f.read().splitlines()
    # else:
        indexpage = requests.get(INDEX_URL)
        content = indexpage.content
        soup = BeautifulSoup(content, "html.parser")
        h2s = soup.find_all("h2")
        for h2 in h2s:
            if h2.string == "Resources":
                for sibling in h2.next_siblings:
                    if sibling.name == "h2":
                        break
                    if sibling.name == "a":
                        url = '/'.join([BASE_URL, sibling['href']])
                        urls.append(url)
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
        obj.docs_html = obj_def.prettify()
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
        req = Request()
        req.name = get_request_name(req_def)
        req.params = parse_params(get_params(req_def))
        req.description = req_def.find("a").text.strip()
        if req_def.find("p") is not None:
            req.description += ("\n" + req_def.find("p").text.strip())
        req.method, canv_endpoint = (req_def.find(class_="endpoint").text.strip().split())
        req.endpoint,req.needs = get_endpoint_and_needs(canv_endpoint)
        requests.append(req)
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

def main() -> None:
    get_docs_to_parse()

if __name__ == '__main__':
    main()