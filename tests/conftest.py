import sys

import pytest
from fastapi.testclient import TestClient

sys.path.append('movie_service/movies_api')
from movies_api.main import app


@pytest.fixture(scope='session')
def client():
    with TestClient(app) as client_app:
        yield client_app


@pytest.fixture
def fake_uuid(scope='session'):
    return '0031feab-8f53-412a-8f53-47098a60a999'


@pytest.fixture
def api_v1_films(scope='session'):
    return '/api/v1/films'


@pytest.fixture
def api_v1_genres(scope='session'):
    return '/api/v1/genres'


@pytest.fixture
def api_v1_persons(scope='session'):
    return '/api/v1/persons'
