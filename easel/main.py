from typing import Dict,Any, Tuple
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from cement.core.output import OutputHandler
from cement.core.template import TemplateHandler
from cement.utils import fs
from typing import Mapping
# from .core.exc import easelError
from .controllers.base_controller import BaseController
# from .controllers.course_controller import CourseController
# from .controllers.assignment_controller import AssignmentController
import rich
import mako
from mako.template import Template
from mako.lookup import TemplateLookup
import os
import sys
from importlib.machinery import SourceFileLoader
from pathlib import Path
from cement.utils import fs
from cement.ext.ext_colorlog import ColorLogHandler
# from sqlalchemy.orm import sessionmaker, Session
# from sqlalchemy import create_engine, null, Engine
# from .core.items import Base, Course
from itertools import repeat
import logging

from .core.api import CanvasApi

# configuration defaults
CONFIG = init_defaults('easel')
CONFIG['easel']['database'] = '~/Dropbox/code/py/easel/easel.db'

# def extend_sql(app):
#     dbpath: Path = os.path.expanduser(app.config.get('easel', 'database'))
#     # os.remove(dbpath)
#     app.log.info(f"Attempting to connect to database at {dbpath}")
#     dblink: str = 'sqlite+pysqlite:////' + dbpath
#     # TODO: merge engine logger and easel logger 
#     engine: Engine = create_engine(dblink, echo=True, logging_name = app.Meta.label)
#     # TODO: possibly lazy load easel items
#     Base.metadata.create_all(engine)
#     session: Session = Session(engine)
#     session.begin()
#     app.extend('db', session)

# def close_sql(app):
#     app.db.close()

class MakoTemplateHandler(TemplateHandler):
    class Meta:
        label = 'mako_template_handler'

    def load(self, template: str=None, lookup_dirs: list=[], lookup_defaults: bool=False):
        #TODO: differentiate template and template content, and load from file or string respectively (stop using super _load_template_from_file)
        if lookup_defaults:
            lookup_dirs = lookup_dirs + self.app._meta.template_dirs
            # _, app_template_path = super()._load_template_from_module("__init__.py")
            lookup_dirs.append("./easel/templates")
        self.app.log.info(f"Lookup dirs: {lookup_dirs}")
        lookup=TemplateLookup(directories=lookup_dirs)
        # if template: # template takes precedence over content
        #     template_content = open(template, 'r').read()

        template_content, template_type, template_path = super().load(template)
        template_obj = Template(template_content, lookup=lookup)
        return template_obj

    def render(self, data: Dict[str, Any], template: str=None, lookup_dirs: list=[], lookup_defaults: bool=False):
        template_obj = self.load(template, lookup_dirs, lookup_defaults)
        self.app.log.info(f"Rendering template {template} with data: {data.keys()}")
        render = template_obj.render(**data)
        print(render)
        # return render

class MakoOutputHandler(OutputHandler):
    class Meta:
        label = 'mako_output_handler'

    def render(self, data: Dict[str, Any], *args, **kwargs) -> str:
        # print(rich.inspect(args), rich.inspect(kwargs))
        # print(rich.inspect(self.app.template))
        if isinstance(kwargs.get('template'), str):
            template = str(kwargs.get('template'))
            template_contents = self.app.template.load(template)
            render = self.app.template.render(template_contents,data)
        else:
            print("ruh roh", rich.inspect(kwargs))
            return ""
        console = rich.console.Console()
        with console.capture() as capture:
            console.print(render)
        output = capture.get()
        return output

def extend_api(app):
    app.extend('api', CanvasApi(app=app))

def append_local_template_dir(app):
    app.add_template_dir("./easel/templates")

def add_config_hooks(app):
    for hook in app.config.keys('hooks'):
        # hook = app.config.get('hooks', hook_key)
        app.hook.define(hook)
        hook_data = app.config.get('hooks', hook)
        for hook_func_module_str in hook_data.get('register_hooks'):
            hook_func_module = SourceFileLoader("func", hook_func_module_str).load_module()
            hook_func = hook_func_module.hook
            app.hook.register(hook, hook_func)

class easel(App):
    """Easel primary application."""
    class Meta:
        hooks = [
            ('post_setup', add_config_hooks),
            ('post_setup', extend_api),
            ('post_setup', append_local_template_dir),
        #         ('post_setup',extend_sql),
        #         ('post_run', close_sql),
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
            # 'jinja2',
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
            BaseController,
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
