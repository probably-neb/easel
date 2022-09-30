from typing import List
from declarations import *
import warnings
import copy
from dataclasses import asdict
import json

from parse_published_docs import get_doc_objs_and_requests
from parse_model_comments import get_model_objs

def sort_objs_by_name(objs: List[ObjectDefinition]):
    return sorted(objs, key=lambda o: o.name_snake)

def to_dict_by_name(objs: List[ObjectDefinition]):
    return dict(map(lambda o: (o.name, o), objs))

def merge_types_from_model(fields: List[ObjectField], model_fields: List[ObjectField]) -> None:
    by_name = lambda f: f.name
    fields.sort(key=by_name)
    model_fields.sort(key=by_name)
    if len(fields) != len(model_fields):
        print(f"model fields: {model_fields}\ndocs fields: {fields}")
        raise Exception("field count mismatch")
    new_fields = []
    for field, model_field in zip(fields, model_fields):
        new_field = ObjectField(name=field.name, description=field.description, example=field.example, type=field.type_, documented_type=field.documented_type, primary_key=field.primary_key, option_enum=field.option_enum)
        refmatch = re.match(RE_REF_TYPE, model_field.type)
        arrmatch = re.match(RE_ARRAY_TYPE, model_field.type)
        if refmatch:
            new_field.type_ = refmatch.group(1)
        elif arrmatch:
            new_field.type_ = f'list[{arrmatch.group(1)}] = field(default_factory=list)'
        else:
            new_field.type_ = SQL_TYPEMAP[model_field.documented_type]
        new_fields.append(new_field)
    return new_fields

def merge_models_and_docs(model_objs: List[ObjectDefinition], docs_objs: List[ObjectDefinition]):
    model_objs_dict = to_dict_by_name(model_objs)
    docs_objs_dict = to_dict_by_name(docs_objs)
    new_objs = []

    for model_obj_name in model_objs_dict.keys():
        model_obj = model_objs_dict[model_obj_name]
        docs_obj = docs_objs_dict.get(model_obj_name)
        if docs_obj == None:
            warnings.warn(f"{model_obj_name} not in parsed docs")
            new_objs.append(copy.copy(model_obj))
            continue
        else:
            #TODO: make new obj and take from both returning new obj
            # merge fields
            new_obj = ObjectDefinition(name=model_obj.name, name_snake=model_obj.name_snake)
            if model_obj.description is None:
                new_obj.description = docs_obj.description
            else:
                new_obj.description = model_obj.description
            new_obj.fields = merge_types_from_model(docs_obj.fields, model_obj.fields)
            new_objs.append(new_obj)
    return new_objs

def merge_obj_lists(a_objs: List[ObjectDefinition], b_objs: List[ObjectDefinition]) -> List[ObjectDefinition]:
    a_objs_dict = to_dict_by_name(a_objs)
    b_objs_dict = to_dict_by_name(b_objs)
    # initialize as a and then merge b into it
    new_objs = a_objs_dict.copy()

    for b_obj_name in b_objs_dict.keys():
        b_obj = b_objs_dict[b_obj_name]
        a_obj = a_objs_dict.get(b_obj_name)
        if a_obj == None:
            # b not in a, add it
            new_objs[b_obj_name] = b_obj
        else:
            # b in a, merge fields
            new_objs[b_obj_name].merge(b_obj)
    return list(new_objs.values())

def render_objects(objs: List[ObjectDefinition]) -> List[str]:
    objs = sort_objs_by_name(objs)
    rendered_objs = []
    for obj in objs:
        rendered_obj = obj.render()
        rendered_objs.append(rendered_obj)
    return rendered_objs

def render_requests(requests: List[Request]) -> List[str]:
    req_rends = []
    for req in requests:
        rend = REQUEST_MAKO_TEMPLATE.render(**req.__dict__)
        # print(rend)
        req_rends.append(rend)
    return req_rends

def get_obj_req_rends(objects, requests):
    return (render_objects(objects), render_requests(requests))

def save_rendered_objects_to_file(rendered_objs: List[str], file=RENDERED_OBJS_FILE):
    with open(file, 'w') as f:
        for obj in rendered_objs:
            f.write(obj)
            f.write('\n')
        
def save_rendered_requests_to_file(rendered_reqs: List[str]):
    with open(RENDERED_REQUESTS_FILE, 'w') as f:
        for req in rendered_reqs:
            f.write(req)
            f.write('\n')

def save_objs_json(objs: List[ObjectDefinition], file=OBJECTS_FILE):
    objs = sort_objs_by_name(objs)
    with open(file, 'w') as f:
        obj_name_obj = {obj.name: asdict(obj) for obj in objs}
        json.dump(obj_name_obj, f, indent=3)

def save_reqs_json(requests: List[Request]):
    with open(REQUESTS_FILE, 'w') as f:
        req_name_req = {req.name: asdict(req) for req in requests}
        json.dump(req_name_req, f, indent=3)

def print_obj_dict(obj):
    print(asdict(obj))

def generate_seperate_files():
    docs_objs, docs_requests = get_doc_objs_and_requests()
    model_objs = get_model_objs()
    save_objs_json(docs_objs, file=DOC_OBJS_FILE)
    save_objs_json(model_objs, file=MODEL_OBJS_FILE)
    save_rendered_objects_to_file(render_objects(docs_objs), file=RENDERED_DOC_OBJS_FILE)
    save_rendered_objects_to_file(render_objects(model_objs), file=RENDERED_MODEL_OBJS_FILE)

def generate_merged_file():
    docs_objs, docs_reqs = get_doc_objs_and_requests()
    model_objs = get_model_objs()
    # print(model_objs)
    merged_objs = merge_obj_lists(model_objs, docs_objs)

    rendered_objs = render_objects(merged_objs)
    rendered_requests = render_requests(docs_reqs)
    save_rendered_objects_to_file(rendered_objs)
    save_rendered_requests_to_file(rendered_requests)

def main():
    generate_seperate_files()

if __name__ == "__main__":
    main()
