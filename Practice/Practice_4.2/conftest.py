import pytest
import requests
from constants import HEADERS
from constants import base_url
from constants import json
from faker import Faker

faker = Faker()
@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    response = requests.post(f"{base_url}/auth", headers=HEADERS, json=json)
    token = response.json().get("token")
    assert token is not None, "token is empty"
    session.headers.update(HEADERS)
    session.headers.update({"Cookie": f"token = {token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname" : faker.first_name(),
        "lastname" : faker.last_name(),
        "totalprice" : faker.random_int(min=50, max=1000),
        "depositpaid" : True,
        "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
        }