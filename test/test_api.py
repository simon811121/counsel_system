import json
import time
from src.data import acnt_info
from src.api import _settings_update

def _re_init_acnt_info(set_max=False):
    acnt_info.__init__(file_name="account_info_test.csv")
    acnt_info._refresh_file()
    if set_max == False:
        acnt_info.glb_cfg.update_setting('acnt_info', 'nxt_user_id', 0)
        acnt_info.glb_cfg.save_settings()
    else:
        max_user_id = acnt_info.glb_cfg.get_section('acnt_info')['max_user_id']
        acnt_info.glb_cfg.update_setting('acnt_info', 'nxt_user_id', max_user_id)
        acnt_info.glb_cfg.save_settings()

def test_login_home(test_client):
    resp = test_client.get("/api/v1/hello")

    assert resp.status_code == 200
    assert b"Welcome to counsel system login function!" in resp.data

def test_register_success(test_client):
    # re-init acnt_info
    _re_init_acnt_info()

    # send request
    register_data_file = open("./test/input/register.json")
    req_json_data = json.load(register_data_file)
    resp = test_client.post("/api/v1/register", json=req_json_data)

    assert resp.status_code == 200

def test_register_dup_account(test_client):
    # send request 1st
    test_register_success(test_client)

    # send request 2nd
    register_data_file = open("./test/input/register.json")
    req_json_data = json.load(register_data_file)
    resp = test_client.post("/api/v1/register", json=req_json_data)
    resp_json_data = resp.get_json()

    assert resp.status_code == 400
    assert "Duplicate Account" in resp_json_data["message"]

def test_register_fail(test_client):
    # re-init acnt_info
    _re_init_acnt_info(True)

    # update nxt_user_id
    cfg = acnt_info.glb_cfg
    max_user_id = cfg.get_setting('acnt_info', 'max_user_id')
    cfg.update_setting('acnt_info', 'nxt_user_id', max_user_id)
    cfg.save_settings()

    # send request
    register_data_file = open("./test/input/register.json")
    req_json_data = json.load(register_data_file)
    resp = test_client.post("/api/v1/register", json=req_json_data)
    resp_json_data = resp.get_json()

    assert resp.status_code == 400
    assert "registered failed" in resp_json_data["message"]

def test_login_success(test_client):
    # re-init acnt_info
    _re_init_acnt_info()

    # register first
    test_register_success(test_client)

    # send request
    login_data_file = open("./test/input/login.json")
    req_json_data = json.load(login_data_file)
    resp = test_client.post("/api/v1/login", json=req_json_data)
    resp_json_data = resp.get_json()

    # get user_id from config
    cfg = acnt_info.glb_cfg
    nxt_user_id = cfg.get_setting('acnt_info', 'nxt_user_id')

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "Data received successfully"
    assert (nxt_user_id - 1) == (resp_json_data['user_id'])

def test_login_failed_wrong_password(test_client):
    # re-init acnt_info
    _re_init_acnt_info()

    # register first
    test_register_success(test_client)

    # send request
    req_json_data = json.loads('{"account": "simon_huang", "password": "147258369"}')
    resp = test_client.post("/api/v1/login", json=req_json_data)
    resp_json_data = resp.get_json()

    assert resp.status_code == 401
    assert "wrong password" in resp_json_data["message"]

def test_login_failed_no_account(test_client):
    # re-init acnt_info
    _re_init_acnt_info()

    # register first
    test_register_success(test_client)

    # send request
    req_json_data = json.loads('{"account": "hqazwsxedc", "password": "147258369"}')
    resp = test_client.post("/api/v1/login", json=req_json_data)
    resp_json_data = resp.get_json()

    assert resp.status_code == 401
    assert "account not found" in resp_json_data["message"]

def test_login_failed_no_input(test_client):

    # send request
    resp = test_client.post("/api/v1/login", json="")
    resp_json_data = resp.get_json()

    assert resp.status_code == 400
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "No data received from frontend"

def test_logout(test_client):
    # login first
    test_login_success(test_client)

    # send request
    resp = test_client.get("/api/v1/logout")
    resp_json_data = resp.get_json()

    assert resp.status_code == 200
    assert "message" in resp_json_data
    assert resp_json_data["message"] == "Logout successfully"

def test_chceck_logout(test_client):
    # login first
    test_login_success(test_client)

    _settings_update(2) # 2 seconds
    time.sleep(3)

    # send request
    resp = test_client.get("/api/v1/check_logout")
    resp_json_data = resp.get_json()

    assert "Auto Logout successfully" in resp_json_data["message"]

def test_account_id(test_client):
    # send request
    account_id = 123456789
    resp = test_client.get("/api/v1/account/" + str(account_id))
    resp_json_data = resp.get_json()
    assert resp_json_data["message"] == "Data received successfully"
    assert resp_json_data["account_id"] == str(account_id)

    resp = test_client.put("/api/v1/account/" + str(account_id))
    resp_json_data = resp.get_json()
    assert resp.status_code == 200

def test_password(test_client):
    # send request
    resp = test_client.post("/api/v1/password/forget")
    assert resp.status_code == 200
    resp = test_client.post("/api/v1/password/setup")
    assert resp.status_code == 200
    resp = test_client.get("/api/v1/password/setup")
    assert resp.status_code == 200