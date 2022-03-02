# import pdfkit
import os
from api_request import get_request, check_response

def download_page(course_id, page_name):
    """dowloads a page with page_name from course with course_id as html"""
    with open('page.html', 'w') as page:
        res = get_request(f"/courses/{course_id}/pages/{page_name}")
        check_response(res)
        page.write(res.json()["body"])
        page.close()

    #to turn html file into pdf with pdfkit
    # pdfkit.from_file('page.html', 'page.pdf')
    # os.remove("page.html")

def get_pages(course_id):
    """gets pages from course course_id"""

    res = get_request(f"courses/{course_id}/pages")
    check_response(res)
    pages = {}
    for page in res.json():
        pages[page["url"]] = page
    return pages
