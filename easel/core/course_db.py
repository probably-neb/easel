from cement import App

def get_courses():
    Course = app.db.Query()
    return app.db.search(Course)

with App('easel') as app:
    app.hook.define('db_hook')
    app.hook.defined('db_hook')
    app.hook.register('db_hook', get_courses)

