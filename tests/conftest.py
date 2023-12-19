from core import get_production_app

from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest


@pytest.fixture
def app() -> FastAPI:
    return get_production_app()


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)
