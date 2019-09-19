from app.test.fixtures import app, client

def test_app_create(app):
    assert app

def test_app_run(app, client):
    with client:
        r = client.get("/")
        assert r.status_code == 200
        assert r.is_json
        assert r.json == "Youtube Money Calculator"