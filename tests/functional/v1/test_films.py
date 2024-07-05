def test_films(client, api_v1_films):
    # list all films from 0 with size 10
    response = client.get(api_v1_films + "/", params={"page_number": 0, "page_size": 10})
    assert response.status_code == 200
    assert len(response.json()) == 10

    # list films with filters, paginate and sorting
    response = (
        client.get(
            api_v1_films + "/",
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
    )
    assert response.status_code == 200

    # fetch data from redis
    response = client.get(api_v1_films + "/")
    assert response.status_code == 200
