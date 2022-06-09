from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from cement.core.output import OutputHandler
from cement.core.template import TemplateHandler
from cement.utils import fs
from typing import Mapping
from .core.exc import easelError
from .controllers.base import Base
from .controllers.courses import Courses
from .controllers.assignments import Assignments
import rich
import mako
from mako.template import Template
# configuration defaults
CONFIG = init_defaults('easel')
CONFIG['easel']['course_structure'] = '~/Dropbox/code/py/easel/course-structure.json'

import os
from tinydb import TinyDB
from BetterJSONStorage import BetterJSONStorage
from pathlib import Path
from .core.db_funcs import DBFuncs
from .core.api import CanvasApi
from cement.utils import fs
from cement.ext.ext_colorlog import ColorLogHandler

def extend_tinydb(app):
    db_file = app.config.get('easel', 'course_structure')
    
    # ensure that we expand the full path
    db_file = fs.abspath(db_file)
    
    # ensure our parent directory exists
    db_dir = os.path.dirname(db_file)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # app.extend('db', TinyDB(Path(db_file), access_mode="r+", storage=BetterJSONStorage))
    app.extend('db', TinyDB(Path(db_file), access_mode="r+", indent=3))
    app.log.info('App extended with TinyDB: [%s]' % vars(app.db))
    app.log.info('Database file is: %s' % db_file)

def extend_dbfuncs(app):
    app.extend('dbfuncs', DBFuncs(app))

def extend_api(app):
    app.extend('api', CanvasApi(app))

def close_storage(app):
    app.log.info("Closing Storage")
    app.db.storage.close()

class MakoTemplateHandler(TemplateHandler):
    class Meta:
        label = 'mako_template_handler'

    def load(self, template_path: str):
        return super().load(template_path)

    def render(self, content:str, data:Mapping):
        template = Template(content)
        render = template.render(data)
        print(render)
        return render

class MakoOutputHandler(OutputHandler):
    class Meta:
        label = 'mako_output_handler'

    def render(self, data: Mapping, *args, **kwargs) -> str:
        # print(rich.inspect(args), rich.inspect(kwargs))
        print(rich.inspect(self.app.template))
        if isinstance(kwargs.get('template'), str):
            template = str(kwargs.get('template'))
        else:
            print("ruh roh", rich.inspect(kwargs))
            return ""
        template_contents = self.app.template.load(template)
        render = self.app.template.render(template_contents,data)
        console = rich.console.Console()
        with console.capture() as capture:
            console.print(render)
        output = capture.get()
        return output

class easel(App):
    """Easel primary application."""

    class Meta:
        hooks = [
                ('post_setup',extend_tinydb),
                ('post_setup', extend_dbfuncs),
                ('post_setup', extend_api),
                ('pre_close', close_storage)
        ]

        label = 'easel'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'colorlog',
            'yaml',
            'jinja2',
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
        output_handler = 'mako_output_handler'
        template_handler =  'mako_template_handler'

        # register handlers
        handlers = [
            Base,
            Courses,
            Assignments,
            ColorLogHandler,
            MakoOutputHandler,
            MakoTemplateHandler,
        ]

class EaselTest(TestApp,easel):
    """A sub-class of easel that is better suited for testing."""
    class Meta:
        label = 'easel'

def main():
    with easel() as app:
        try:
            app.run()
            # print(app._meta.template_module.)

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
