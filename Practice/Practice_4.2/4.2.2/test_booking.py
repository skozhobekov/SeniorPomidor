import json
from http.client import responses
from os import getenv

import faker.generator
import requests
import pytest
import conftest
from constants import base_url
from constants import HEADERS
from constants import json
from constants import update_data
from constants import patch_data
from constants import negative_price_data
from constants import without_additional_needs
from faker import Faker


faker = Faker()
class TestBooking():

    def test_create_booking(self, auth_session, booking_data):
        response = auth_session.post(f"{base_url}/booking", json=booking_data)
        assert response.status_code == 200, f"status code error, status is {response.status_code}"
        booking_id = response.json().get("bookingid")
        assert booking_id is not None, "id is empty"
        assert response.json()["booking"]["firstname"] == booking_data['firstname'], "firstname not matches response"
        assert response.json()["booking"]["totalprice"] == booking_data['totalprice'], "firstname not matches response"
        print(response.json())
        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.status_code == 200 , "ID not found"
        delete_booking = auth_session.delete(f"{base_url}/booking/{booking_id}")
        assert delete_booking.status_code == 201, "booking isn't deleted"
        assert get_booking.status_code == 200, "booking deleted already"

    def test_create_booking_without_additional_options(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{base_url}/booking", json=without_additional_needs)
        assert create_booking.status_code == 200, "error"
        assert create_booking.json().get("bookingid") is not None

    def test_create_booking_with_negative_totalprice(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{base_url}/booking", json=negative_price_data)
        booking_id = create_booking.json().get("bookingid")
        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        new_total_price = get_booking.json().get("totalprice")
        print(new_total_price)
        assert new_total_price is not None
        assert new_total_price == 100, "total price is over 0" #-100



    def test_update_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{base_url}/booking", json=booking_data)
        first_name = update_data['firstname']
        last_name = update_data['lastname']
        total_price = update_data['totalprice']
        booking_id = create_booking.json().get("bookingid")
        update_booking = auth_session.put(f"{base_url}/booking/{booking_id}", json=update_data)
        assert update_booking.json().get("firstname") == first_name, "incorrect firstname"
        assert update_booking.json().get("lastname") == last_name, "incorrect lastname"
        assert update_booking.json().get("totalprice") == total_price, "incorrect lastname"
        delete_booking = auth_session.delete(f"{base_url}/booking/{booking_id}")

    def test_partial_update_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{base_url}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")
        patch_booking = auth_session.patch(f"{base_url}/booking/{booking_id}", json=patch_data)
        assert patch_booking.json().get("firstname") == patch_data.get("firstname")
        assert patch_booking.json().get("lastname") == patch_data.get("lastname")

    def test_get_global_bookings(self, auth_session, booking_data):
        get_bookings = auth_session.get(f"{base_url}/booking")
        assert get_bookings is not None

    def test_get_booking_by_id(self, auth_session,booking_data):
        create_booking = auth_session.post(f"{base_url}/booking", json=booking_data)
        booking_id = create_booking.json().get("bookingid")
        get_booking = auth_session.get(f"{base_url}/booking/{booking_id}")
        assert get_booking.json().get("firstname") is not None
        assert get_booking.json().get("lastname") is not None
        assert get_booking.json().get("totalprice") is not None

    def test_get_booking_negative(self, auth_session):
        fake_id = faker.random_int(min=10000, max=99999)
        get_booking = auth_session.get(f"{base_url}/booking/{fake_id}")
        assert get_booking.status_code == 404, f"status code is: {get_booking.status_code}"
        print(get_booking.status_code)























