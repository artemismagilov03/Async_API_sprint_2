def test_list_genres(client, api_v1_genres, endpoint='/'):
    # list all genres from 0 with size 10
    response = client.get(api_v1_genres + endpoint, params={'page_number': 0, 'page_size': 10})
    assert response.status_code == 200
    assert len(response.json()) == 10

    # list genres with filters, paginate and sorting
    response = client.get(
        api_v1_genres + endpoint,
        params={
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
        },
    )
    assert response.status_code == 200

    # fetch data from redis
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200

    # not exists data, to large page_number
    response = client.get(
        api_v1_genres + endpoint,
        params={
            'sort': 'id',
            'page_number': 99,
            'page_size': 10,
        },
    )
    assert response.status_code == 404
