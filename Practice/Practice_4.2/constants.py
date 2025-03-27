import pytest
import requests

base_url = "https://restful-booker.herokuapp.com"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}
json={"username": "admin", "password": "password123"}

update_data = {
    "firstname": "Sanjar",
    "lastname": "Kojobekov",
    "totalprice": 100,
    "depositpaid": False,
    "bookingdates": {"checkin": "2022-01-01", "checkout": "2022-01-10"},
    "additionalneeds": "Dinner"
}

patch_data = {
    "firstname": "Sanjar",
    "lastname": "Kojobekov",
}

without_additional_needs = {

  "firstname": "Sanjar",
  "lastname": "Kojobekov",
  "totalprice": 211,
  "depositpaid": False,
  "bookingdates": {
      "checkin": "2023-05-01",
      "checkout": "2023-05-10"
  }
}

negative_price_data = {
    "firstname": "Sanjar",
    "lastname": "Kojobekov",
    "totalprice": 100,
    "depositpaid": False,
    "bookingdates": {"checkin": "2022-01-01", "checkout": "2022-01-10"},
    "additionalneeds": "Dinner"
    }
