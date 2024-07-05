def test_list_persons(client, api_v1_persons, endpoint='/'):
    # list all persons from 0 with size 10
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200
    assert len(response.json()) == 10

    # list persons with filters, paginate and sorting
    response = client.get(
        api_v1_persons + endpoint,
        params={
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
            'actor': 'Mazzy Star',
            'director': 'Walter C. Miller',
            'writer': 'Tony Cooke',
        },
    )
    assert response.status_code == 200

    # fetch persons from redis
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200

    # not exists persons
    response = client.get(
        api_v1_persons + endpoint,
        params={
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
            'actor': 'fake',
            'director': 'fake',
            'writer': 'fake',
        },
    )
    assert response.status_code == 404


def test_search_films(client, api_v1_persons, endpoint='/search'):
    # search all persons from 0 with size 10
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200
    assert len(response.json()) == 10

    # search persons with filters, paginate and sorting
    response = client.get(
        api_v1_persons + endpoint,
        params={
            'query': 'Mazzy',
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
            'actor': 'Mazzy Star',
            'director': 'Walter C. Miller',
            'writer': 'Tony Cooke',
        },
    )
    assert response.status_code == 200

    # fetch searched films from redis
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200

    # not exists films after search
    response = client.get(api_v1_persons + endpoint, params={'query': 'fake'})
    assert response.status_code == 404
