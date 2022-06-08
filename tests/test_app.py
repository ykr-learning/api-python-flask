from flask import request, jsonify
from numpy import equal

from src.app import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_request_home(client):
    response = client.get("/")
    assert b"Hello, world index.html !" in response.data
    assert response.status_code == 200

def test_request_store(client):
    response = client.get("/store")
    assert b"My wonderful store" in response.data
    assert response.status_code == 200


# res = self.client().post('/update_account', data={[the json your api takes]}
# self.assertEqual(res.status_code, 201)

