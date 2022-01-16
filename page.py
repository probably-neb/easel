import core
import pdfkit
import os

def download_page(course_id, page_name):
    """dowloads a page with page_name from course with course_id as html"""
    with open('page.html', 'w') as page:
        res = core.get_request(f"/courses/{course_id}/pages/{page_name}")
        print(res.json()["body"])
        page.write(res.json()["body"])
        page.close()

    #to turn html file into pdf with pdfkit
    # pdfkit.from_file('page.html', 'page.pdf')
    # os.remove("page.html")

def get_pages(course_id):
    """gets pages from course course_id"""

    return core.get_request(f"courses/{course_id}/pages")
