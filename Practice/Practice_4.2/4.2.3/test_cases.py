from http.client import responses

import requests
from constant import base_url
from constant import data
from constant import put_update_data
from constant import HEADERS


class TestCases:

    def test_create_item(self, item_data, auth_session):
        response = auth_session.post(f"{base_url}/items/", json=item_data)
        assert response.status_code == 200, f"Ошибка: {response.status_code}, {response.text}"
        item_id = response.json().get("id")
        assert item_id is not None, "Ошибка: item_id не получен!"

    def test_get_items_list(self, auth_session):
        response = auth_session.get(f"{base_url}/items/?skip=0&limit=100")
        assert response.status_code==200, "Error, status code isn't 200"
        assert isinstance(response.json().get("data"), list)
        assert len(response.json().get("data", [])) > 0

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


    def test_full_update_item(self, auth_session, item_data):
        response = auth_session.put(f"{base_url}/items", json=put_update_data)
        print(response.json())

        auth_session.headers.update({"Content-Type":"application/json"})
        response = auth_session.put(f"{base_url}/items", json=put_update_data)
        # assert response.json().get("title") == "updated_title"
        # assert response.json().get("description") == "updated_description"
        print(response.json())