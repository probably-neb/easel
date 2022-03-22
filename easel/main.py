from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from cement.ext import ext_colorlog
from cement.utils import fs

from .core.exc import easelError
from .controllers.base import Base
from .controllers.courses import Courses
from .controllers.assignments import Assignments
# configuration defaults
CONFIG = init_defaults('easel.yml')
CONFIG['easel.yml']['course_structure'] = '~/Dropbox/code/py/easel/course-structure.json'

import os
from tinydb import TinyDB
from BetterJSONStorage import BetterJSONStorage
from pathlib import Path
from .core.db_funcs import DBFuncs
from cement.utils import fs

def extend_tinydb(app):
    app.log.info('using tinydb to store course structure')
    db_file = app.config.get('easel.yml', 'course_structure')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(Path(db_file), indent=2, access_mode="r+", storage=BetterJSONStorage))
    # app.extend('db', TinyDB(db_file, indent=2))

def extend_dbfuncs(app):
    app.extend('dbfuncs', DBFuncs(app))

def close_storage(app):
    app.db.storage.close()

class easel(App):
    """Easel primary application."""

    class Meta:
        hooks = [
                ('post_setup',extend_tinydb),
                ('post_setup', extend_dbfuncs),
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

def extend_tinydb_test(app):
    app.log.info('using tinydb to store course structure')
    db_file = fs.abspath("./tests/test_db.json")
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    app.log.info('tinydb database file is: %s' % db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    app.extend('db', TinyDB(Path(db_file), indent=2, access_mode="r+", storage=BetterJSONStorage))

class EaselTest(TestApp,easel):
    """A sub-class of easel that is better suited for testing."""

    TEST_CONFIG_DEFAULTS = init_defaults('easel.yml')
    TEST_CONFIG_DEFAULTS['easel.yml']['course_structure'] = fs.Tmp().dir
    class Meta:
        label = 'easel'
        hooks = [
                ('post_setup', extend_tinydb_test),
                ('post_setup', extend_dbfuncs),
                ('close_storage', close_storage)
                ]

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
