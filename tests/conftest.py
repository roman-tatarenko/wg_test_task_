import json

import pytest as pytest
import requests


def pytest_addoption(parser):
    parser.addoption("--client_id", action="store", type=str)
    parser.addoption("--client_secret", action="store", type=str)


@pytest.fixture(scope="session")
def client_id(request):
    """Handler for --additional_value parameter"""
    client_id = request.config.getoption("--client_id")
    return client_id


@pytest.fixture(scope="session")
def client_secret(request):
    """Handler for --additional_value parameter"""
    client_secret = request.config.getoption("--client_secret")
    return client_secret


@pytest.fixture(scope="class")
def get_access_token(client_id, client_secret):
    response = requests.post(
        url="https://www.olx.ua/api/open/oauth/token",
        json={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": "v2 read write"
        }
    )
    content = json.loads(response.content.decode())
    access_token = content['access_token']
    return access_token


class GlobalClassToken:
    access_token = None
