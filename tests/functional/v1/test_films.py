def test_films(client, api_v1_films):
    assert client.get(api_v1_films + "/").status_code == 200

    # list films with filters, paginate and sorting
    response = (
        client.get(
            api_v1_films + "/",
            params={
                "sort": "id",
                "page_number": 1,
                "page_size": 10,
                "genre": "Biography",
                "actor": "Barbara Church",
                "director": "Angela Turner",
                "writer": "Angela Turner",
            },
        )
    )

    print(response)
