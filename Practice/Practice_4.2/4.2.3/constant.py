base_url = "https://api.pomidor-stage.ru/api/v1"
HEADERS = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
HEADERS_FOR_AUTH = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

data = {
    "username": "sanjarkojobekov@gmail.com",
    "password": "Sanjarbaike96$$$",
    "scope":"",
    "client_id": "",
    "client_secret": ""
}

auth_data = {
    "username": "sanjarkojobekov@gmail.com",
    "password": "Sanjarbaike96$$$"
}
invalid_auth_data = {
    "username": "sanjarkojob@gmail.com",
    "password": "000"
}


put_update_data = {

  "title": "updated_title",
  "description": "updated_description"
}

