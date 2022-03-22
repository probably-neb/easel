from tinydb import Query
from tinydb.table import Document
import re
import time
class DBFuncs():
    def __init__(self, app):
        self.app = app

    def store_tables(self,tables):
        for table_type in tables.keys():
        # could set "id" field to doc_id (multiple writes per page though)
            if table_type == 'pages':
                Page = Query()
                for page in tables[table_type]:
                    self.app.db.table(table_type).upsert(page,Page.url == page['url'])
            else:
                # could extend tinydb table to get item id itself (faster?)
                # stime = time.time()
                for document in tables[table_type]:
                    self.app.db.table(table_type).upsert(Document(document, doc_id=document["id"]))
                # etime = time.time()
                # self.app.log.info(f"storage of {table_type} took {(etime -stime):.4}") #, to_console=False)

    def get_course_names_and_ids(self):
        Course = Query()
        return [(course["name"], course["id"]) for course in self.app.db.table("courses").all()]

    def add_course_nickname(self, id, nickname):
        Course = Query()
        self.app.db.table('courses').upsert(Document({"nickname" : nickname}, doc_id=id))

    def get_course_name(self, id):
        Course = Query()
        course = self.app.db.table("courses").get(Course.id == id) #["name"]
        return course["name"]

    def search_for_assignment(assignment):
        # Field = Query()
        # Assignment = Query().search(Field.name.search(assignment, flags = re.IGNORECASE) | Field.)
        # Course = Query().assignment_groups.any(AssignmentGroup.assignments.any(Assignment.name.search(assignment, flags=IGNORECASE)))
        pass
