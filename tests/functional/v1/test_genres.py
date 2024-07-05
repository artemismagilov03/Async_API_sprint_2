def test_list_genres(client, api_v1_genres, endpoint='/'):
    # list all genres from 0 with size 10
    response = client.get(api_v1_genres + endpoint)
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

    # fetch genres from redis
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200

    # not exists genres, to large page_number
    response = client.get(
        api_v1_genres + endpoint,
        params={
            'sort': 'id',
            'page_number': 99,
            'page_size': 10,
        },
    )
    assert response.status_code == 404


def test_search_genres(client, api_v1_genres, endpoint='/search'):
    # search all genres from 0 with size 10
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200
    assert len(response.json()) == 10

    # search genres with filters, paginate and sorting by title
    response = client.get(
        api_v1_genres + endpoint,
        params={
            'query': 'Action',
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
        },
    )
    assert response.status_code == 200

    # fetch searched genres from redis
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200

    # not exists genres, to large page_number
    response = client.get(
        api_v1_genres + endpoint,
        params={
            'sort': 'id',
            'page_number': 99,
            'page_size': 10,
        },
    )
    assert response.status_code == 404


def test_uuid_genre(client, api_v1_genres, endpoint='/0b105f87-e0a5-45dc-8ce7-f8632088f390'):
    # get genre by uuid
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200

    # fetch genre by uuid from redis
    response = client.get(api_v1_genres + endpoint)
    assert response.status_code == 200

    # not exists genre by uuid
    response = client.get(api_v1_genres + '/0b105f87-e0a5-45dc-8ce7-f8632088f999')
    assert response.status_code == 404
