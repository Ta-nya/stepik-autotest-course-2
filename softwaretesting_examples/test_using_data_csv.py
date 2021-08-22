import requests
import pytest
import csv


def read_data_from_csv():
    test_data = []
    with open('softwaretesting_examples/csv_data.csv', newline='') as csvfile:
        data = csv.reader(csvfile, delimiter='')
        next(data) #skip header row
        for row in data:
            test_data.append(row)
            return test_data

@pytest.mark.parametrize("country_code, zip_code, expected_place_name", read_data_from_csv())
def test_using_csv_get_locations_data_check_place_name(country_code, zip_code, expected_place_name):
    response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == expected_place_name

