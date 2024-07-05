import sys

import pytest
from fastapi.testclient import TestClient

sys.path.append('movie_service/movies_api')
from movies_api.main import app


@pytest.fixture
def client():
    with TestClient(app) as client_app:
        yield client_app


@pytest.fixture
def api_v1_films():
    return '/api/v1/films'


@pytest.fixture
def api_v1_genres():
    return '/api/v1/genres'


@pytest.fixture
def api_v1_persons():
    return '/api/v1/persons'
