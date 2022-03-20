from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal

from .core.exc import easelError
from .controllers.base import Base
from .controllers.courses import Courses
from .controllers.assignments import Assignments
# configuration defaults
CONFIG = init_defaults('easel.yml')
CONFIG['easel.yml']['course_structure'] = '~/Dropbox/code/py/easel/course-structure.json'

import os
from tinydb import TinyDB
from .core.utils import EaselUtils
from cement.utils import fs

def extend_tinydb(app):
    # app.log.info('using tinydb to store course structure')
    db_file = app.config.get('easel.yml', 'course_structure')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    # app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(db_file, indent=2))

def extend_utils(app):
    app.extend('utils', EaselUtils(app))

class easel(App):
    """Easel primary application."""

    class Meta:
        hooks = [
                ('post_setup',extend_tinydb),
                ('post_setup', extend_utils)
        ]
        label = 'easel'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'jinja2',
            'colorlog',
            'json'
        ]

        # configuration handler
        config_handler = 'yaml'

        #plugins 
        # plugin_dirs = ['./plugins']

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base,
            Courses,
            Assignments,
        ]

class easelTest(TestApp,easel):
    """A sub-class of easel that is better suited for testing."""

    class Meta:
        label = 'easel'


def main():
    with easel() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except easelError as e:
            print('easelError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
