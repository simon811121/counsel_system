import pytest

from main import create_app
from src.data import Account_Info

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
