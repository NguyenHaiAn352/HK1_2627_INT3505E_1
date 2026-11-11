def test_product_create(client):
    payload = {
        "sku": "book-001",
        "name": "Leather Notebook",
        "price_cents": 100,
        "qty_in_stock": 100,
    }
    response = client.post("/api/v1/products", json=payload)

    assert response.status_code == 201
    assert response.json["sku"] == "book-001"
    assert response.json["name"] == "Leather Notebook"
    assert response.json["price_cents"] == 100
