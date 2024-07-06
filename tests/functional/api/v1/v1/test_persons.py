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
            'actor': 'John Sayles',
            'director': 'John Sayles',
            'writer': 'John Sayles',
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


def test_search_persons(client, api_v1_persons, endpoint='/search'):
    # search all persons from 0 with size 10
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200
    assert len(response.json()) == 10

    # search persons with filters, paginate and sorting
    response = client.get(
        api_v1_persons + endpoint,
        params={
            'query': 'John',
            'sort': 'id',
            'page_number': 0,
            'page_size': 10,
            'actor': 'John Sayles',
            'director': 'John Sayles',
            'writer': 'John Sayles',
        },
    )
    assert response.status_code == 200

    # fetch searched films from redis
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200

    # not exists films after search
    response = client.get(api_v1_persons + endpoint, params={'query': 'fake'})
    assert response.status_code == 404


def test_uuid_person(client, api_v1_persons, fake_uuid, endpoint='/00a770fc-8964-41fa-9d3b-f6c958c9dddb'):
    # get person by uuid
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200

    # fetch person by uuid from redis
    response = client.get(api_v1_persons + endpoint)
    assert response.status_code == 200

    # not exists film by uuid
    response = client.get(api_v1_persons + f'/{fake_uuid}')
    assert response.status_code == 404
