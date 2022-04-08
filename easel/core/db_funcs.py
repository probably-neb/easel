from tinydb import Query
from tinydb.table import Document
import re
import time
from pprint import pprint

class DBFuncs:
    def __init__(self, app):
        self.app = app

    def update_db(self, api: bool=True, types:list=[]):
        if api and types:
            self.app.api.sync_with_api(types)
        custom_courses = 

    def store_tables(self,tables):
        #TODO: check if tables are the right types
        for table_type in tables.keys():
            # pprint(tables[table_type])
            #TODO: could set "id" field to doc_id (multiple writes per page though)
            if table_type == 'pages':
                Page = Query()
                # stime = time.time()
                for page in tables[table_type]:
                    self.app.db.table(table_type).upsert(page,Page.url == page['url'])
                # etime = time.time()
            else:
                # stime = time.time()
                for document in tables[table_type]:
                    # should map assignments to ids as docs as well
                    # switch from assignment groups to assignments
                        # can include assignment group when requesting assignments?
                    if table_type == "assignment":
                        document["grade_str"] = self.get_grade(document)
                    self.app.db.table(table_type).upsert(Document(document, doc_id=document["id"]))
                # etime = time.time()
            # self.app.log.info(f"storage of {table_type} took {(etime -stime):.4}") #, to_console=False)

    def get_course_names_and_ids(self) -> list[tuple[str, int]]:
        courses = []
        for course in self.app.db.table("courses").all():
            name = course["name"] if course.get("name") else "Access Restricted By Time"
            courses.append((name, course["id"]))
        return courses

    def add_course_nickname(self, id, nickname):
        Course = Query()
        self.app.db.table('courses').upsert(Document({"nickname" : nickname}, doc_id=id))

    def get_course_name(self, id):
        Course = Query()
        course = self.app.db.table("courses").get(Course.id == id) #["name"]
        return course["name"]

    def get_grade(self, assignment):
        # The type of grading the assignment receives; one of:
        #'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'
        grading_type = assignment["grading_type"]
        ret = "N/A"
        if grading_type == "points": 
            score,out_of = 0.0, assignment["points_possible"]
            if out_of.is_integer():
                out_of = int(out_of)
            if assignment.get("submission") and assignment.get("submission").get("score"):
                score = assignment["submission"]["score"]
                if score.is_integer():
                    score = int(score)
            else:
                score = "-"
            ret =  str(score) + "/" + str(out_of)
        else:
            if assignment.get("submission"):
                if assignment.get("submission").get("grade"):
                    ret = assignment["submission"]["grade"]
        # how to update result in table
        self.app.db.table("assignment_groups").update({"grade_str" : ret}, Query().assignments.any(Query().id == assignment["id"]))
        return ret

    def search_for_assignment(assignment):
        # Field = Query()
        # Assignment = Query().search(Field.name.search(assignment, flags = re.IGNORECASE) | Field.)
        # Course = Query().assignment_groups.any(AssignmentGroup.assignments.any(Assignment.name.search(assignment, flags=IGNORECASE)))
        pass
