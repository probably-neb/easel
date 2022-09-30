from cement import Controller, ex
from cement.utils.version import get_version_banner
from cement.utils import shell
from ..core.version import get_version
import json
import config
import asyncio
import timeit
# from aiohttp import aiofile
from ..core.api import get_course_structure
from pprint import pprint
import time

VERSION_BANNER = """
Canvas api cli app %s
%s
""" % (get_version(), get_version_banner())

class CourseController(Controller):
    class Meta:
        label = 'courses'
        stacked_type="nested"
        stacked_on="base"
        arguments=[
            ( [ '-u', '--update' ],
                { 'help' : 'update course data',
                    'action'  : 'store_true',
                    'dest' : 'update' } ),
                ( ['-c', '--course'],
                {'help': 'specify which course',
                'action' : 'store',
                'dest': 'course'})
                ]

    def _default(self):
        """Default action if no sub-command is passed."""
        self.app.args.print_help()

    @ex(
        help='list favorite courses',

        # sub-command level arguments. ex: 'easel command1 --foo bar'
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-n', '--names' ],
              { 'help' : 'only print course names',
                'action'  : 'store_true',
                'dest' : 'names' } ),
              ( [ '-i', '--ids' ],
                  { 'help' : 'only print course ids',
                      'action'  : 'store_true',
                      'dest' : 'ids' } )],
    )
    def list(self):
        """list courses"""
        courses_info = self.app.dbfuncs.get_course_names_and_ids()
        try: 
            ids = self.app.pargs.ids
            names = self.app.pargs.names
        except:
            ids = False
            names = False
        courses = []
        if not ids and not names:
            print("Found Courses: ")
            courses.append({'id' : 'ID','name' : 'NAME'})
        for name,id in courses_info:
            if ids:
                print(id)
            elif names:
                print(name)
            else:
                courses.append({"name" : name, "id" : id})
        self.app.render({"courses" : courses}, "courses.mako")

    def _print_course_column(self, id, name):
        print(f"{' '*3} {id:<6} | {name}")

    @ex(help='update database')
    def update(self):
        self.app.log.info("Beginning Course Structure Update")
        start_time = time.time()
        # import cProfile
        # import pstats
        # profile = cProfile.Profile()
        # profile.enable()
        # type_tables = asyncio.run(get_course_structure(*self.app.api.get_domain_header()))
        self.app.dbfuncs.update_db(types=["courses", "assignments"])
        # profile.disable()
        # ps = pstats.Stats(profile).strip_dirs().sort_stats('cumtime').reverse_order()
        end_time = time.time()
        self.app.log.info(f'Course Structure Update Success! Took {(end_time-start_time):.4} seconds')
        # self.app.log.info(f'api took: {api:<8} | store took: {store}')
        self.list()

    @ex(
        help='add or change a nickname for a course. Makes course specific easel commands much easier (only shows up in easel)',

        # sub-command level arguments. ex: 'easel command1 --foo bar'
        arguments=[
            ( [ '-s', '--search-term' ],
              { 'help' : '',
                'action'  : 'store',
                'dest' : 'sterm' } ),
              ( [ '-i', '--id' ],
                  { 'help' : 'add nickname to course by id',
                      'action'  : 'store',
                      'type' : int,
                      'dest' : 'id' } ),
              ( [ '-p', '--prompt' ],
                  { 'help' : 'prompt for comfirmation before adding nickname when using -i or -s flags',
                      'action'  : 'store_true',
                      'dest' : 'prompt' } ),
              ( [ '-n', '--name' ],
                  { 'help' : 'nickname for new course',
                      'action'  : 'store',
                      'type' : str,
                      'dest' : 'nickname' } )
                  ],
    )
    def name(self):
        search_term = self.app.pargs.sterm
        id = self.app.pargs.id
        nickname = self.app.pargs.nickname
        courses = dict(self.app.dbfuncs.get_course_names_and_ids())
        course = None
        if search_term is None and id is None:
            selection = shell.Prompt("Choose a course to nickname:",
                    options = list(courses.keys()),
                    numbered = True,
                    )
            id = courses[selection.input]
            course = selection.input
        elif search_term is not None and id is None:
            search_term = search_term.lower()
            for course_name in courses.keys():
                # course[0] is the location of the name 
                if search_term in course_name.lower():
                    id = courses[course_name]
                    course = course_name
            if id is None:
                print(f"No course matched search term: {search_term}. Use 'easel courses list' to see course names and try again")
        if id is not None:
            for course_name,course_id in courses.items():
                if course_id == id:
                    course = course_name
            if nickname is None:
                nickname = shell.Prompt(f"Enter a new nickname for {course}:", default=None).input
            
            verification = True
            if self.app.pargs.prompt:
                verification = shell.Prompt(f"Add nickname: \"{nickname}\", to course: {course}?", options=["yes","no"], default='yes').input == "yes"
            if verification:
                self.app.dbfuncs.add_course_nickname(id, nickname)
                print(f"Succesfully added nickname: \"{nickname}\" to course: {course}")
            else:
                print(f"Failed to add nickname: \"{nickname}\" to course: {course}")


    @ex(help="list, modify, or add links for the couse. If multiple options are provided only the first in the order list,add,rename,change-link will be executed",
            arguments=[
                (['--list'],
                    {'action': 'store_true',
                    'dest': 'list'}),
                ([ '--add','-a'],
                    {'action': 'store',
                    'help':"--add [link name] [link]",
                    'dest': 'add',
                    'nargs':2,
                    }),
                ([ '--rename','-r'],
                    {'action': 'store',
                    'dest': 'rename',
                    'help':"--rename [link name] [new link name]",
                    'nargs':2
                    }),
                ([ '--remove','-rm'],
                    {'action': 'store',
                    'dest': 'remove',
                    'help':"--remove [link name]",
                    }),
                ([ '--change-link','-c'],
                    {'action': 'store',
                    'dest': 'change',
                    'help':"--change-link [link name] [new link]",
                    'nargs':2
                    }),
                # (['--name', '-n'],
                #     # ['name'],
                #     {'action': 'store',
                #         # 'dest': 'name',
                #     'default':None,
                #     # 'required':False
                #     }),
                # (['--link', '-l'],
                #     # ['link'],
                #     {'action': 'store',
                #         # 'dest': 'link',
                #     'default':None,
                #     # 'required':False
                #     }),
                ])
                
    def links(self):
        if not self.app.pargs.course:
            print("No course Specified. Please use in the form 'easel courses -c [course name] links [args]")
            return
        course = self.app.dbfuncs.search(type='courses', search_term=self.app.pargs.course)[0]
        list = self.app.pargs.list
        add = self.app.pargs.add
        rename = self.app.pargs.rename
        remove = self.app.pargs.remove
        change = self.app.pargs.change

        if list or (not add and not rename and not remove and not change):
            pprint(course.get('links'))
            return
        # if add and name and link:
        if add:
            name = add[0]
            link = add[1]
            course['links'][name] = link
            print(f"link {name}: {link} added to course {course['name']}")
        elif rename:
            old_name = rename[0]
            new_name = rename[1]
            course['links'][new_name] = course['links'][old_name]
            del course['links'][new_name]
            print(f"link: {new_name} reold_named to: {old_name} reold_named for course {course['old_name']}")
        elif remove:
            del course['links'][remove]
        elif change:
            name = change[0]
            new_link = change[1]
            course['links'][name] = new_link
            print(f"link: {name} changed to: {new_link} renamed for course {course['name']}")
        else:
            print("Two arguments required for this command")

        self.app.db.table('courses').upsert(Document(course, doc_id=course['id']))
        
