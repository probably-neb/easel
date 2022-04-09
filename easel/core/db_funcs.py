from tinydb import Query
from tinydb.table import Document
import re
import time
from pprint import pprint
import hashlib
# import difflib

class DBFuncs:
    def __init__(self, app):
        self.app = app

    def search(self, type, search_term, return_key:str=None, search_key:str='names', num_results:int=1) -> list:
        results = []
        if type and type[-1] is not 's':
            type += 's'
        if search_key is 'names':
            results = self.app.db.table(type).search(Query().names.any(Query().name.matches(search_term, flags=re.IGNORECASE)))
        if not return_key:
            return results[:num_results]
        else:
            results = results[:num_results]
            result_keys = []
            for result in results:
                key = result.get(return_key)
                if not key:
                    raise KeyError(f"Key: {return_key} is not a valid key for type: {type}. Please Search again with a valid key")
                result_keys.append(key) 
            return result_keys

    def update_db(self, api: bool=True, types:list=[]):
        if api and types:
            self.app.api.sync_with_api(types)
            
        if self.app.config.keys('courses'):
            custom_courses = self.app.config.get_section_dict('courses')
            courses = []
            for course in custom_courses.keys():
                hash = hashlib.sha256(course.encode('utf-8')).hexdigest()
                #6 because canvas ids are 5 so make sure they can't match
                id = int(str(int(hash, 16))[:6])
                if not custom_courses[course].get('names'):
                    custom_courses[course]['names'] = []
                # remove if duplicate
                default_name = {'name':course} 
                if default_name not in custom_courses[course]['names']:
                    custom_courses[course]['names'].append(default_name) 
                for name in custom_courses[course]['names']:
                    if not name.get(type):
                        name['type'] = 'user'
                #TODO: see if can write to config file and store hash so course name can be changed without creating a new course
                custom_courses[course]['hash'] = hash
                custom_courses[course]['id'] = id
                custom_courses[course]['name'] = course
                custom_courses[course]['type'] = 'user'
                courses.append(custom_courses[course])
            self.store_tables({"courses":courses})
            # self.store_tables(custom_courses[course] for course in custom_courses.keys())

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
