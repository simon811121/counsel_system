import pytest

from main import create_app

@pytest.fixture
def test_app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture
def client(test_app):
    return test_app.test_client()
