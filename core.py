import json
import requests
from pprint import pprint

config_file = open("canvas_cli_config.json", 'r')
config = json.loads(config_file.read())

def get_domain_token():
    domain = config["info"]["domain"]
    token = config["info"]["token"]
    return domain, token

def get_header(token):
    header = {'Authorization': 'Bearer ' + token}
    return header

def get_favorite_courses():
    domain, token = get_domain_token()
    header = get_header(token)
    param = {'per_page': 100, 'include': "favorites"}
    response = requests.get('https://' + domain + '/api/v1/courses', headers=header, params=param)
    courses = response.json()
    favorite_courses = []
    for course in courses:
        try:
            if course["is_favorite"]:
                favorite_courses.append(course)
        except KeyError:
            continue
    return favorite_courses

if __name__ == "__main__":
    favorite_courses = get_favorite_courses() 
    print(pprint(favorite_courses))
