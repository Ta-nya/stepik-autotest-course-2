import requests


def test_get_locations_for_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/us/90210")
    assert response.status_code == 200

def test_get_locations_for_90210_check_content_type_equals_json():
    resource = requests.get("http://api.zippopotam.us/us/90210")
    assert resource.headers['Content-Type'] == "application/json"

def test_get_locations_for_90210_check_country_equals_USA():
    resource = requests.get("http://api.zippopotam.us/us/90210")
    resource_body = resource.json()
    assert resource_body['country'] == "United States"

def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Beverly Hills"

def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert len(response_body["places"]) == 1

def test_get_location_state_name():
    respose = requests.get("http://api.zippopotam.us/us/90210")
    response_body = respose.json()
    assert response_body["places"][0]['state'] == "California"

