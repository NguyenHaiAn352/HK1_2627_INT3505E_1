"""LAB 1 — add your five tests here. Do not delete the smoke tests.

A. GET /books, empty database -> HTTP 200 and []
B. GET /books/9999 -> HTTP 404, JSON code == NOT_FOUND
C. POST /books with only author -> HTTP 400, errors contains title
D. POST valid book, DELETE it, GET same id -> HTTP 404
BONUS. Validate a Book response using JSON Schema; add an unknown
       field to a *copy* of the response and assert ValidationError.

Useful imports:
    from jsonschema import validate, ValidationError
    import pytest
    from tools import get_book_schema

Do not depend on test execution order. Fixtures: client, app, sample_book.
"""

from jsonschema import validate, ValidationError
import pytest
from tools import get_book_schema

def test_get_empty_list(client):
    response = client.get("/books")
    
    assert response.status_code == 200
    assert response.content_type == "applcation/json"
    assert response.get_json() == []

def test_get_invalid_book(client):
    response = client.get("/books/9999")

    assert response.status_code == 404
    assert response.content_type == "applcation/json"
    assert response.get_json()["code"] == "NOT_FOUND"

def test_post_invalid_book(client):
    payload = {
        "author": "Placeholder",
        "year": 1987,
        "isbn": "Placeholder"
    }
    
    response = client.post("/books", json = payload)
    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert response.get_json()["code"] == "VALIDATION_ERROR"
    assert response.get_json()["errors"][0]["field"] == "title"
    
def test_post_delete_book(client):
    payload = {
        "title": "Placeholder",
        "author": "Placeholder",
        "year": 1987,
        "isbn": "Placeholder"
    }

    response = client.post("/books", json = payload)
    response = client.delete("/books/1")
    response = client.get("/books/1")

    assert response.status_code == 404
    assert response.content_type == "applcation/json"
    assert response.get_json()["code"] == "NOT_FOUND"