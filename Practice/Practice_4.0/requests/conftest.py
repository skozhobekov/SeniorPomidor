import pytest
import requests

@pytest.fixture(scope="session")
def session_create():
    return requests.session()
