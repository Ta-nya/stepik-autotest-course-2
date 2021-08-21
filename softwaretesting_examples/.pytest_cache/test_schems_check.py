import requests

schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "post code": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "country abbreviation": {
      "type": "string"
    },
    "places": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "place name": {
              "type": "string"
            },
            "longitude": {
              "type": "string"
            },
            "state": {
              "type": "string"
            },
            "state abbreviation": {
              "type": "string"
            },
            "latitude": {
              "type": "string"
            }
          },
          "required": [
            "place name",
            "longitude",
            "state",
            "state abbreviation",
            "latitude"
          ]
        }
      ]
    }
  },
  "required": [
    "post code",
    "country",
    "country abbreviation",
    "places"
  ]
}

def test_get_locations_for_us_90210_check_schema():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    assert response_body == schema



