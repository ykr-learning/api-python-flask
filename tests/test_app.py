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


def test_request_home(client):
    response = client.get("/")
    assert b"Hello, world index.html !" in response.data
    assert response.status_code == 200


def test_request_store(client):
    response = client.get("/store")
    assert b"My wonderful store" in response.data
    assert response.status_code == 200


def test_request_store_not_exists(client):
    response = client.get("/store/fake")
    assert b'"message":"store not found"' in response.data
    assert response.status_code == 404


def test_request_store_exists(client):
    response = client.get("/store/My wonderful store")
    assert b"My wonderful store" in response.data
    assert response.status_code == 200


def test_add_store(client):
    response = client.post("/store", content_type='application/json',
                           json={"name": "autre store"}, follow_redirects=True)
    assert b"autre store" in response.data
    assert response.status_code == 201
    response2 = client.get("/store")
    assert b"autre store" in response2.data
    assert response2.status_code == 200
