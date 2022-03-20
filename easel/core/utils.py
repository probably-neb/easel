from tinydb import Query
from tinydb.table import Document
class EaselUtils():
    def __init__(self, app):
        self.app = app

    def get_course_names_and_ids(self):
        Course = Query()
        return [( course["name"], course["id"]) for course in self.app.db.search(Course.course==True)]

    def add_course_nickname(self, id, nickname):
        self.app.db.upsert(Document({"nickname" : nickname}, doc_id=id))
