# import pdfkit
import os
from api_request import get_request, check_response
from pprint import pprint

def get_grades(course_id):
    """gets pages from course course_id"""

    res = get_request(f"courses/{course_id}/assignments")
    check_response(res)
    grades = res.json()
    # for grade in res.json():
    return grades

