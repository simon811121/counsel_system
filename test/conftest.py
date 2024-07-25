import pytest

from main import create_app
from src.data import Account_Info
from src.data import Counseling_Record

@pytest.fixture
def test_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()

def create_acnt_info(file_name):
    acnt_info = Account_Info(file_name)
    return acnt_info

@pytest.fixture
def test_acnt_info():
    acnt_info = create_acnt_info("account_info_test.csv")
    acnt_info.glb_cfg.update_setting('acnt_info', 'nxt_user_id', 0)
    acnt_info.glb_cfg.save_settings()
    acnt_info._refresh_file()
    yield acnt_info

@pytest.fixture
def test_acnt_info_set_nxt_user_id():
    acnt_info = create_acnt_info("account_info_test.csv")
    acnt_info.glb_cfg.update_setting('acnt_info', 'nxt_user_id', 100)
    acnt_info.glb_cfg.save_settings()
    acnt_info._refresh_file()
    yield acnt_info

def create_cnsl_rcrd(file_name):
    cnsl_rcrd = Counseling_Record(file_name)
    return cnsl_rcrd

@pytest.fixture
def test_cnsl_rcrd():
    cnsl_rcrd = create_cnsl_rcrd("counseling_record_test.xlsx")
    cnsl_rcrd._refresh_file()
    yield cnsl_rcrd