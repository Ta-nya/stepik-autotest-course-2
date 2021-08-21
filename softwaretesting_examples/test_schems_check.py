import requests
import jsonschema
import json
#from jsonschema import validate

schema1 = {
	"definitions": {},
	"$schema": "http://json-schema.org/draft-07/schema#",
	"$id": "https://example.com/object1629569017.json",
	"title": "Root",
	"type": "object",
	"required": [
		"post code",
#        "post code2",
		"country",
		"country abbreviation",
		"places"
	],
	"properties": {
		"post code": {
			"$id": "#root/post code",
			"title": "Post code",
			"type": "string",
			"default": "",
			"examples": [
				"90210"
			],
			"pattern": "^.*$"
		},
		"country": {
			"$id": "#root/country",
			"title": "Country",
			"type": "string",
			"default": "",
			"examples": [
				"United States"
			],
			"pattern": "^.*$"
		},
		"country abbreviation": {
			"$id": "#root/country abbreviation",
			"title": "Country abbreviation",
			"type": "string",
			"default": "",
			"examples": [
				"US"
			],
			"pattern": "^.*$"
		},
		"places": {
			"$id": "#root/places",
			"title": "Places",
			"type": "array",
			"default": [],
			"items":{
				"$id": "#root/places/items",
				"title": "Items",
				"type": "object",
				"required": [
					"place name",
					"longitude",
					"state",
					"state abbreviation",
					"latitude"
				],
				"properties": {
					"place name": {
						"$id": "#root/places/items/place name",
						"title": "Place name",
						"type": "string",
						"default": "",
						"examples": [
							"Beverly Hills"
						],
						"pattern": "^.*$"
					},
					"longitude": {
						"$id": "#root/places/items/longitude",
						"title": "Longitude",
						"type": "string",
						"default": "",
						"examples": [
							"-118.4065"
						],
						"pattern": "^.*$"
					},
					"state": {
						"$id": "#root/places/items/state",
						"title": "State",
						"type": "string",
						"default": "",
						"examples": [
							"California"
						],
						"pattern": "^.*$"
					},
					"state abbreviation": {
						"$id": "#root/places/items/state abbreviation",
						"title": "State abbreviation",
						"type": "string",
						"default": "",
						"examples": [
							"CA"
						],
						"pattern": "^.*$"
					},
					"latitude": {
						"$id": "#root/places/items/latitude",
						"title": "Latitude",
						"type": "string",
						"default": "",
						"examples": [
							"34.0901"
						],
						"pattern": "^.*$"
					}
				}
			}

		}
	}
}





def test_validate_schema():
    response = requests.get("http://api.zippopotam.us/us/90210")
    response_body = response.json()
    validator = jsonschema.Draft7Validator(schema1)
    if validator.is_valid(response_body):
        return
    error_msg = "ответ не соответствует схеме"
    assert False, error_msg


