from pytest import raises
from easel.main import EaselTest
from conftest import tmp

def test_easel():
    # test easel without any subcommands or arguments
    with EaselTest() as app:
        app.run()
        assert app.exit_code == 0
        # app.db.storage.close()

def test_easel_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with EaselTest(argv=argv) as app:
        app.run()
        assert app.debug is True
        # app.close()
        # app.db.storage.close()

def test_extensions():
    with EaselTest(argv=[]) as app:
        app.run()
        assert app.ext.list() is not None
        app.log.info(app.ext.list())
        # app.db.storage.close()

def test_api_requests():
    # async with self._session.get(url="http://httpbin.org/headers") as r:
    #         json_body = await r.json()
    #         pprint(json_body)
    #         assert json_body['headers']['Authorization'] == self.headers["Authorization"]
    pass

def test_update():
    argv = ['-u']
    with EaselTest(argv=argv) as app:
        app.run()
        ids = []
        for table in app.db.tables():
            for doc in app.db.table(table).all():
                if table == "pages":
                    assert doc.get("url") is not None
                    assert doc["url"] not in ids
                    ids.append(doc["url"])
                else:
                    assert table != "pages"
                    assert doc.get("id") is not None
                    assert doc["id"] not in ids
                    ids.append(doc["id"])
                    if table != "courses":
                        assert doc.get("course_id") is not None
        # app.db.storage.close()

# def test_assignments(tmp):
#     argv = ['assignments', 'list']
#     with EaselTest(argv=argv) as app:
#         app.run()
        
#         app.db.storage.close()
