def test_product_list_empty(client):
    response = client.get("/api/v1/products")

    assert response.status_code == 200
    assert response.json == {
        "items": [],
        "page": 1,
        "size": 20,
        "total": 0,
    }
