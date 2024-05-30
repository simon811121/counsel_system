def test_home(client):
    resp = client.get("/")

    assert resp.status_code == 200
    assert b"Welcome to counsel system main page!" in resp.data