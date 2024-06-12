import pytest

from main import create_app
from main import create_acnt_info

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

@pytest.fixture
def test_acnt_info():
    acnt_info = create_acnt_info()
    acnt_info.glb_cfg.update_setting('acnt_info', 'nxt_user_id', 0)
    acnt_info.glb_cfg.save_settings()
    acnt_info._refresh_file()
    yield acnt_info