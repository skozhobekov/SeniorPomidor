import requests
import pytest

data = {"query": "форд"}
url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/car_brand"


def test_request():
    data = { "query": "форд" }
    token = "d6c5e6df8314eda22b4df2990b0b4f1359b48e03"
    headers = {
        'Authorization': f'Token {token}'
    }
    response = requests.post(url = url, json=data, headers=headers)
    response_json = response.json()
    # print(response.headers)
    print(response.status_code)
    assert response.status_code == 200
    print(response_json)

def test_session(session_create):
    session_create.post(url = url, json=data)
    session_create.headers.update({"new_header":"new_value"})
    print(session_create.headers)
