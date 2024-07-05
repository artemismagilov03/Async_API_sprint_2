def test_list_films(client, api_v1_films, endpoint="/"):
    # list all films from 0 with size 10
    response = client.get(
        api_v1_films + endpoint, params={"page_number": 0, "page_size": 10}
    )
    assert response.status_code == 200
    assert len(response.json()) == 10

    # list films with filters, paginate and sorting
    response = client.get(
        api_v1_films + endpoint,
        params={
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
            "genre": "Biography",
            "actor": "Barbara Church",
            "director": "Angela Turner",
            "writer": "Angela Turner",
        },
    )
    assert response.status_code == 200

    # fetch data from redis
    response = client.get(api_v1_films + endpoint)
    assert response.status_code == 200

    # not exists data
    response = client.get(
        api_v1_films + endpoint,
        params={
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
            "genre": "fake",
            "actor": "fake",
            "director": "fake",
            "writer": "fake",
        },
    )
    assert response.status_code == 404


def test_search_films(client, api_v1_films, endpoint="/search"):
    # search all films from 0 with size 10
    response = client.get(
        api_v1_films + endpoint, params={"page_number": 0, "page_size": 10}
    )
    assert response.status_code == 200
    assert len(response.json()) == 10

    # search films with filters, paginate and sorting
    response = client.get(
        api_v1_films + endpoint,
        params={
            "query": "Star",
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
            "genre": "Biography",
            "actor": "Barbara Church",
            "director": "Angela Turner",
            "writer": "Angela Turner",
        },
    )
    assert response.status_code == 200

    # fetch data from redis
    response = client.get(api_v1_films + endpoint)
    assert response.status_code == 200

    # not exists data
    response = client.get(
        api_v1_films + endpoint,
        params={
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
            "genre": "fake",
            "actor": "fake",
            "director": "fake",
            "writer": "fake",
        },
    )
    assert response.status_code == 404


def test_person_films(client, api_v1_films, endpoint='/37c36461-9a0d-4fd9-b257-fae0b2b6e8ad/film'):
    # by person films from 0 with size 10
    response = client.get(
        api_v1_films + endpoint, params={"page_number": 0, "page_size": 10}
    )
    assert response.status_code == 200
    assert len(response.json()) == 1

    # by person films with filters, paginate and sorting
    response = client.get(
        api_v1_films + endpoint,
        params={
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
        },
    )
    assert response.status_code == 200

    # fetch data from redis
    response = client.get(api_v1_films + endpoint)
    assert response.status_code == 200

    # not exists data
    response = client.get(
        api_v1_films + '37c36461-9a0d-4fd9-b257-fae0b2b6e999',
        params={
            "sort": "id",
            "page_number": 0,
            "page_size": 10,
        },
    )
    assert response.status_code == 404
