from http.client import responses

import requests
from constant import base_url
from constant import data
from constant import put_update_data
from constant import auth_data
from constant import invalid_auth_data
from constant import HEADERS
from constant import HEADERS_FOR_AUTH


class TestCases:

    def test_valid_auth(self, auth_session):
        response = auth_session.post(f"{base_url}/login/access-token", headers=HEADERS_FOR_AUTH, data=auth_data)
        assert response.status_code == 200, "unexpected status code"
        assert "access_token" in response.json()
        json_data = response.json()
        assert json_data["token_type"] == "bearer"

    def test_invalid_auth(self, auth_session):
        response = auth_session.post(f"{base_url}/login/access-token", headers=HEADERS, data=invalid_auth_data, )
        assert response.status_code == 400, "incorrect login or password"
        assert "detail" in response.json()

    def test_sort_by_fields(self, auth_session):
        responses

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(f"{base_url}/items/", json=item_data)
        assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
        item_id = response.json().get("id")
        assert item_id is not None, "Ошибка: item_id не получен!"

    def test_create_item_with_invalid_fields(self, auth_session, invalid_data):
        response = auth_session.post(f"{base_url}/items/", json=invalid_data)
        assert response.status_code == 422, "unexpected status code"

    def test_create_item_with_empty_fields(self, auth_session, invalid_data):
        response = auth_session.post(f"{base_url}/items/")
        assert response.status_code == 422, "unexpected status code"

    def test_create_item_without_token(self, item_data):
        response = requests.post(f"{base_url}/items/", json=item_data)
        assert response.status_code == 401, "token required"


    def test_get_items_list(self, auth_session):
        params = {"skip":0, "limit":100}
        response = auth_session.get(f"{base_url}/items/",params=params)
        json_data = response.json()
        assert response.status_code==200, "unexpected status code"
        assert "count" in json_data, "'count' key missing in response"
        assert "data" in json_data, "'data' key missing in response"
        assert isinstance(json_data["data"], list), "'data' should be a list"
        assert isinstance(json_data["count"], int), "'count' should be an integer"
        assert len(json_data["data"]) <= 100, "More items than limit returned"


    def test_pagination(self, auth_session):
        scip = 0
        limit = 50
        response1 = requests.get(f"{base_url}/items/?scip = {scip}&limit={limit}")
        data = response1.json().get("data", [])
        scip +=limit
        response2 = requests.get(f"{base_url}/items/&scip={scip}&limit={limit}")
        data1 = response2.json().get("data", [])
        items = {item["id"] for item in data}
        items1 = {item["id"] for item in data1}
        assert not items.intersection(items1)


    def test_get_item_by_id(self, auth_session, item_data):
        create_item = auth_session.post(f"{base_url}/items/", json=item_data)
        id = create_item.json().get("id")
        print(id)
        get_item = auth_session.get(f"{base_url}/items/{id}")
        print(get_item.json())
        assert get_item.status_code == 200, "statuscode isn't 200"
        assert get_item.json().get("title") is not None
        assert get_item.json().get("description") is not None
        assert get_item.json().get("owner_id") is not None

    def test_delete_item(self, auth_session, item_data):
        create_item = auth_session.post(f"{base_url}/items", json=item_data)
        id = create_item.json().get("id")
        auth_session.delete(f"{base_url}/items{id}")
        get_deleted_item = auth_session.get(f"{base_url}/items/{id}")
        assert get_deleted_item.status_code != 200

    def test_delete_not_existed_item(self, auth_session):
        response = auth_session.delete(f"{base_url}/items{-145}")
        assert response.status_code == 404, "item not found"



    def test_full_update_item(self, auth_session, item_data):
        create_item = auth_session.post(f"{base_url}/items/", json=item_data)
        item_id = create_item.json().get("id")
        response = auth_session.put(f"{base_url}/items/{item_id}", json=put_update_data)
        assert response.status_code == 200, "unexpected status code"
        assert response.json().get("title") == "updated_title",  "not updated"
        assert response.json().get("title") == put_update_data.get("title"),  "not updated"
        assert response.json().get("description") == put_update_data["description"],  "not updated"

