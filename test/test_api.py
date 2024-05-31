import json

def test_login_home(client):
    resp = client.get("/api/v1/hello")

    assert resp.status_code == 200
    assert b"Welcome to counsel system login function!" in resp.data

def test_login_success(client):

    login_data_file = open("./test/input/login.json")
    req_json_data = json.load(login_data_file)

    resp = client.post("/api/v1/login", json=req_json_data)
    resp_json_data = resp.get_json()

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert "data" in resp_json_data
    assert resp_json_data["message"] == "Data received successfully"
    assert resp_json_data["data"]["account_id"] == req_json_data["account_id"]
    assert resp_json_data["data"]["password"] == req_json_data["password"]

def test_login_failed (client):

    resp = client.post("/api/v1/login", json="")
    resp_json_data = resp.get_json()

    assert resp.status_code == 400
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "No data received from frontend"


def test_logout (client):

    resp = client.get("/api/v1/logout")
    resp_json_data = resp.get_json()

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "Logout successfully"

