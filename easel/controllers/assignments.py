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
            ( [ '-c', '--course' ],
                { 'help' : 'select course to filter by',
                    'action'  : 'store',
                    'dest' : 'course' } ),
                ]

    def _default(self):
        """Default action if no sub-command is passed."""
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
        AssignmentGroup = Query()
        if self.app.pargs.group is not None:
            group = self.app.pargs.group
            print(group)
            groups = self.app.db.table("assignment_groups").search(AssignmentGroup.name.search(group, flags=IGNORECASE))
            for group in groups:
                course_name = self.app.dbfuncs.get_course_name(group["course_id"])
                print(course_name)
                print_assignment_group(group, group["name"], course_name)
        else: 
            groups = self.app.db.table("assignment_groups").all()
            for group in groups:
                print(group['name'])
                course_name = self.app.dbfuncs.get_course_name(group["course_id"])
                longest = 0
                assignments = []
                # if self.app.pargs.group is not None and self.app.pargs.group.lower() != assignment_group["name"].lower():
                #     continue
                # print(f"{' '*2}{group['name']}:")
                for assignment in group["assignments"]:
                    grade = ""
                    if not self.app.pargs.grades:
                        grade = "(" + self.app.dbfuncs.get_grade(assignment) + ")"
                    assignments.append({"name" : assignment["name"], "grade" : grade, "position" : assignment["position"]})
                    if len(assignment["name"]) > longest:
                        longest = len(assignment["name"])
                position = group["position"]
                assignments.sort(key=sort_by_position)
                print_assignment_group(assignments, group['name'],course_name, position, longest)

#TODO: move to utils
#throws type error without dicts on purpose
def sort_by_position(item):
    return item["position"]

def print_assignment_group(group, group_name, course_name, position=1, longest=0):
    if position == 1:
        print(course_name)
    print(f"{' '*2}{group_name}:")
    for assignment in group:
        print(f"  => {assignment['name']:<{longest}}\t{assignment['grade']:<}")
    print('-'*longest)

