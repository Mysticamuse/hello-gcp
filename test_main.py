from main import app

def test_hello():
    resp = app.test_client().get("/")
    assert resp.status_code == 200
    assert b"Hello, World" in resp.data