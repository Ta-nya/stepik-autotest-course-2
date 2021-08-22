import responses
import requests


@responses.activate
def test_simulate_data_cannot_be_found():
    responses.add(
        responses.GET,
        'http://api.zippopotam.us/us/90210',
        json={"error": "No data exists for US zip code 90210"},
        status=404
    )
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.status_code == 404
    response_body = response.json()
    assert response_body['error'] == 'No data exists for US zip code 90210'
