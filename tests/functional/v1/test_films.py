def test_films(client, api_v1_films):
    assert client.get(api_v1_films + '/').status_code == 200
