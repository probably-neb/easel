import requests
from requests import Response, HTTPError
import config

def get_request(path, params=None, headers=None) -> Response:
    """sends a get request
    path: the http path to the object i.e course/{course_id}/modules/{modules_id}
        path can start with https://[domain] or not
    """
    domain, header = get_domain_header()
    if headers:
        header |= headers
    if not path.startswith("https://"):
        url = domain + path
    else:
        url = path
    return requests.get(url, headers=header, params=params, allow_redirects=True)

def get_domain_header():
    """loads domain name and user api token from config and creates the request header from the token"""
    
    domain = config.get_domain()
    token = config.get_token()
    header = {'Authorization': 'Bearer ' + token}
    domain = 'https://' + domain + '/api/v1/'
    return domain, header

def check_response(res):
    try: 
        res.raise_for_status()
        #will raise ValueError if either of these exist because they are generated when no access
        # try:
        #     json = res.json()
        #     if not res.json():
        #         json = res.text
        #         if json["message"]:
        #             raise 
        #         json["errors"]
        # except TypeError:
        #     pass
        if res:
            return
    except (AttributeError, HTTPError, ValueError) as e:
        raise CanvasNoAccessError("That page has been disabled for this course")

class CanvasNoAccessError(Exception):
    """When user has no access to a canvas object. Most often because an instructor has not given access to said obj. To check, try checking the class through the browser and see if you can see the object for the class"""
    pass
