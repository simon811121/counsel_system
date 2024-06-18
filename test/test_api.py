import json
from src.data import Config

def test_login_home(test_client):
    resp = test_client.get("/api/v1/hello")

    assert resp.status_code == 200
    assert b"Welcome to counsel system login function!" in resp.data

def test_register(test_client):
    register_data_file = open("./test/input/register.json")
    req_json_data = json.load(register_data_file)

    resp = test_client.post("/api/v1/register", json=req_json_data)

    assert resp.status_code == 200

def test_login_success(test_client):
    # register first
    test_register(test_client)

    login_data_file = open("./test/input/login.json")
    req_json_data = json.load(login_data_file)

    resp = test_client.post("/api/v1/login", json=req_json_data)
    resp_json_data = resp.get_json()

    cfg = Config(False)
    sctn = cfg.get_section('acnt_info')
    nxt_user_id = sctn['nxt_user_id']

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "Data received successfully"
    assert (nxt_user_id - 1) == (resp_json_data['user_id'])

def test_login_failed (test_client):

    resp = test_client.post("/api/v1/login", json="")
    resp_json_data = resp.get_json()

    assert resp.status_code == 400
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "No data received from frontend"


def test_logout (test_client):

    resp = test_client.get("/api/v1/logout")
    resp_json_data = resp.get_json()

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "Logout successfully"

def test_account_id (test_client):
    account_id = 123456789
    resp = test_client.get("/api/v1/account/" + str(account_id))
    resp_json_data = resp.get_json()
    assert resp_json_data["message"] == "Data received successfully"
    assert resp_json_data["account_id"] == str(account_id)

    resp = test_client.put("/api/v1/account/" + str(account_id))
    resp_json_data = resp.get_json()
    assert resp.status_code == 200

def test_password (test_client):
    resp = test_client.post("/api/v1/password/forget")
    assert resp.status_code == 200
    resp = test_client.post("/api/v1/password/setup")
    assert resp.status_code == 200
    resp = test_client.get("/api/v1/password/setup")
    assert resp.status_code == 200