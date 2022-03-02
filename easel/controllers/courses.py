from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from ..core.api import get_course_structure
from ..core import course_db 
import aiohttp
import asyncio
# import aiohttp
from cement import App
from tinydb import Query
from pprint import pprint

VERSION_BANNER = """
Canvas api cli app %s
%s
""" % (get_version(), get_version_banner())


class Courses(Controller):
    
    class Meta:
        label = 'courses'
        stacked_type="nested"
        stacked_on="base"


    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()


    @ex(
        help='list favorite courses',

        # sub-command level arguments. ex: 'easel command1 --foo bar'
        # arguments=[
        #     ### add a sample foo option under subcommand namespace
        #     ( [ '-f', '--foo' ],
        #       { 'help' : 'notorious foo option',
        #         'action'  : 'store',
        #         'dest' : 'foo' } ),
        # ],
    )
    def list(self):
        """list courses"""
        Course = Query()
        data = self.app.db.search(Course.name.exists())
        course_names = [course["name"] for course in data]
        self.app.render({'courses' : course_names}, 'courses.jinja2')
    @ex(help='list')
    @ex(help='update database')
    def update(self):
        res = asyncio.run(get_course_structure())
        course_names = []
        self.app.db.truncate()
        for course in res:
            self.app.db.insert(course)
            course_names.append(course["name"])
        self.app.log.info('Course Structure Update Success!')
        self.app.render({'courses':course_names}, 'courses.jinja2')
