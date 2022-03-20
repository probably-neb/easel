from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
import json
import config
import asyncio
import timeit
import aiohttp
import aiofile
from ..core.api import get_course_structure
from tinydb import Query, table
from pprint import pprint
import time
from re import IGNORECASE

VERSION_BANNER = """
Canvas api cli app %s
%s
""" % (get_version(), get_version_banner())


class Assignments(Controller):
    class Meta:
        label = 'assignments'
        stacked_type="nested"
        stacked_on="base"
        arguments=[
            ( [ '-l', '--list' ],
                { 'help' : 'flag to list all assignments',
                    'action'  : 'store_true',
                    'dest' : 'list' } ),
                ]

    def _default(self):
        """Default action if no sub-command is passed."""
        if self.app.pargs.list is not None:
            self.list()
        else:
            self.app.args.print_help()

    @ex(
        help='command to list all assignments',

        arguments=[
            ( [ '-n', '--no-grades' ],
                { 'help' : 'hide grades',
                    'action'  : 'store_true',
                    'dest' : 'grades' } ),
            ( [ '-g', '--group' ],
                { 'help' : 'hide grades',
                    'action'  : 'store',
                    'dest' : 'group' } ),
                ]
    )
    def list(self):
        """list courses"""
        if self.app.pargs.group is not None:
            group = self.app.pargs.group
            print(group)
            Group = Query()
            AssignmentGroup = Query()
            # group = self.app.db.search(Group.name.exists())
            # print(group)
            # courses_with_group = self.app.db.search(Group["assignment_groups"].any(AssignmentGroup.name.search(group, flags=IGNORECASE)))
            # courses_with_group = self.app.db.search(Group["assignment_groups"].name.matches(group, flags=IGNORECASE))
            # courses_with_group = self.app.db.search(Group.assignment_groups.matches(r".*")) #.any(AssignmentGroup.name.exists()))
            for course in courses_with_group:
                print(course["name"])
                # pprint(course["assignment_groups"][])
            print(len(courses_with_group))
        else: 
            documents = self.app.db.all()
            for document in documents:
                if document.doc_id != 0:
                    course_name = document["name"]
                    for assignment_group in document["assignment_groups"]:
                        longest = 0
                        assignments = []
                        # if self.app.pargs.group is not None and self.app.pargs.group.lower() != assignment_group["name"].lower():
                        #     continue
                        print(f"{' '*2}{assignment_group['name']}:")
                        for assignment in assignment_group["assignments"]:
                            grade = ""
                            if not self.app.pargs.grades:
                                grade = "(" + get_grade(assignment) + ")"
                            assignments.append({"name" : assignment["name"], "grade" : grade})
                            if len(assignment["name"]) > longest:
                                longest = len(assignment["name"])
                        for assignment in assignments:
                            print(f"{course_name:<24}  => {assignment['name']:<{longest}}\t{assignment['grade']:<}")
                        print("\n")

def print_assignment_group(group, group_name):
    print(f"{' '*2}{group_name}:")
    for assignment in group:
        print(f"{course_name:<24}  => {assignment['name']:<{longest}}\t{assignment['grade']:<}")


def get_grade(assignment):
    # The type of grading the assignment receives; one of:
#'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'
    grading_type = assignment["grading_type"]
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
        return str(score) + "/" + str(out_of)
    else:
        if assignment.get("submission").get("grade"):
            return assignment["submission"]["grade"]
    return "N/A"
