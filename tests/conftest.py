import pytest as pytest


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


class GlobalClassToken:
    access_token = None
