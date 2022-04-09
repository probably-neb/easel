from cement import Controller, ex
from cement.utils.version import get_version_banner
from cement.utils import fs
from ..core.version import get_version
from ..core import api
from ..controllers.courses import Courses
from pprint import pprint
from tinydb import Query
import asyncio
import time
import os
import webbrowser as browser

VERSION_BANNER = """
Canvas api cli app %s
%s
""" % (get_version(), get_version_banner())

class Base(Controller):
    class Meta:
        label = 'base'

        # text displayed at the top of --help output
        description = 'Canvas api cli app'

        # text displayed at the bottom of --help output
        epilog = 'Usage: easel command1 --foo bar'

        # controller level arguments. ex: 'easel --version'
        arguments = [
            ### add a version banner
            ( [ '-v', '--version' ],
              { 'action'  : 'version',
                'version' : VERSION_BANNER } ),
            (
              [ '-c', '--courses' ],
              { 'action' : 'store_true', 
               'dest' : 'course'}),

            ( [ '-u', '--update' ],
                { 'help' : 'update all canvas data',
                    'action'  : 'store_true',
                    'dest' : 'update' }),
            ( [ '-t', '--truncate' ],
                { 'help' : 'command to clean database. [WARNING] THIS IS NOT REVERSABLE',
                    'action'  : 'store_true',
                    'dest' : 'truncate' } ),
        ]

    def _default(self):
        """Default action if no sub-command is passed."""
        if self.app.pargs.update:
            self.app.handler.resolve('controller', 'courses', setup=True).update()
        elif self.app.pargs.truncate:
            os.remove(fs.abspath(self.app.config.get('easel', 'course_structure')))
        else:
            self.app.args.print_help()

    @ex(help='test a function')
    def test(self):
        print(self.app.hook.defined('utils'))

    @ex(help='print database (mostly used for logging')
    def list(self):
        with self.app.db as db:
            for table in db.tables():
                pprint(db.table(table))

    @ex(help='get an example of a document item',
        arguments = [
            ### add a version banner
            ( ['type'],
              {'choices': ["page","module","course","assignment_group","assignment"]}),    #"all"]
            ( [ '-t', '--template' ],
              {'action' : 'store_true',
               'dest': 'template'}),
            ( [ '-r', '--request' ],
              {'action' : 'store_true',
               'dest': 'request'}),
              ],
        )
    def get(self):
        import random
        type = self.app.pargs.type
        template = self.app.pargs.template
        request = self.app.pargs.request

        # in order to have request probably need better get request methods that takes types to get
        # if request is not None:
        #     item = asyncio.run("api.get_" + type + "s")
        #     pprint(item)
        
        table_type = type + "_groups" if type == "assignment" else type + 's'
        items = self.app.db.table(table_type).search((Query().id.exists()) | (Query().title.exists()))
        item = items[random.randint(0, len(items) - 1)] if len(items) >= 1 else None

        if "assignment" in type:
            if "_group" in type:
                # assignment list often quite long ("thousands of lines") so dont show it
                item["assignments"] = []
            else:
                item = item["assignments"][random.randint(0, len(item["assignments"]) - 1)] if len(item["assignments"]) >= 1 else None

        if not template:
            pprint(item)
        else:
            self.app.render({type : item}, type + '.jinja2')

    @ex(help='list upcoming calendar events')
    def upcoming(self):
        pprint(self.app.api.get_upcoming())
        
    @ex(help='list todo items',
        # arguments=[
        #     ( [ '-l', '--link' ],
        #       { 'action'  : 'store'} ),
        #       ]
        )
    def todo(self):
        ts = time.time()
        pprint(self.app.api.get_todo_items())
        te = time.time()
        self.app.log.info(f'getting todo items took {(te - ts):.4}s')

    @ex(help="open links",
        arguments=[
            ( [ '-l', '--link' ],
              { 'action'  : 'store',
                'dest' : 'link'} ),
            ( ['course'],
                { 'action'  : 'store',
                # 'dest' : 'course',
                # 'required': 'True'} ),
                }),
              ]
        )
    def open(self):
        #TODO course seaching
        course = self.app.pargs.course
        course_id = self.app.dbfuncs.search(type='courses', search_term=course, return_key='id')[0]
        link_name = self.app.pargs.link
        if link_name is None:
            link_name = 'default'
        course_data = self.app.db.table('courses').get(doc_id=course_id)
        link=""
        # pprint(course_data['links'])
        if course_data.get('links').get(link_name):
            link = course_data['links'][link_name]
        if not link:
            raise ValueError(f"No link of type: {link_name} in course {course}. You can add a link of this name to the course or try different search terms")
        browser.open_new_tab(link)
