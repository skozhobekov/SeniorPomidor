import faker
import pytest
import requests
from faker import Faker

from constant import HEADERS
from constant import base_url
from constant import data


@pytest.fixture(scope="session")
def auth_session():
    session = requests.session()
    auth_response = session.post(f"{base_url}/login/access-token", data =data, headers=HEADERS)
    token = auth_response.json().get("access_token")
    session.headers.update({"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"})
    yield session

@pytest.fixture()
def auth_with_different_ContentType(auth_session):
    return None


fake = Faker()
@pytest.fixture(scope="package")
def item_data():
    return {
        "title": fake.word(),
        "description": fake.word()
    }
