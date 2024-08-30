def test_home(test_client):
    resp = test_client.get("/")

    assert resp.status_code == 200
    assert b"Welcome to counsel system main page!" in resp.data