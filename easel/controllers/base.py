from cement import Controller, ex
from cement.utils.version import get_version_banner
from ..core.version import get_version
from ..controllers.courses import Courses
from pprint import pprint
from tinydb import Query

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
            self.app.db.drop_tables()
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
              {#'action'  : 'store',
              'choices': ["page","module","course","assignment_group"]}),
              ],
        )
    def get(self):
        type = self.app.pargs.type + 's'
        print(self.app.db.table(type).get((Query().id.exists()) | (Query().title.exists())))
        
        
        

    # class Meta:
    #     label = 'courses'
    #     stacked_type="nested"
    #     stacked_on="base"
    #     arguments=[
    #         ( [ '-u', '--update' ],
    #             { 'help' : 'update course data',
    #                 'action'  : 'store_true',
    #                 'dest' : 'update' } ),
    #             ]

    # def _default(self):
    #     """Default action if no sub-command is passed."""
    #     if self.app.pargs.update is not None:
    #         self.list()
    #     else:
    #         self.app.args.print_help()
