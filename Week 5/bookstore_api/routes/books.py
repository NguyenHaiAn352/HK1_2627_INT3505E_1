from models import Book, Category, Author
from sqlalchemy import asc, desc
from flask import jsonify, make_response

def error_response(type_, title, status, detail, instance):
    body = {
        "type": type_,
        "title": title,
        "status": status,
        "detail": detail or None,
        "instance": instance or None
    }

    response = make_response(jsonify(body))
    response.status_code = status
    response.headers["Content-Type"] = "application/problem+json"
    return response

def listBooks(arguments, query):
        genre = arguments.get("genre")
        strategy = arguments.get("strategy", "offset")
        limit = int(arguments.get("limit", 10))
        sort_keys = arguments.getlist("sort") or ["id"]
        # sort_keys.reverse()
    
        query = Book.query
    
        # Filter by genre
        if genre:
            query = query.join(Category).filter(Category.name.ilike(f"%{genre}%"))
    
        # Sorting
        for key in sort_keys:
            direction = desc if key.startswith("-") else asc
            attr_name = key.lstrip("-")

            if hasattr(Book, attr_name):
                query = query.order_by(direction(getattr(Book, attr_name)))
            elif attr_name.startswith("authors."):
                sub_attr = attr_name.split(".", 1)[1]
                query = query.join(Book.authors).order_by(direction(getattr(Author, sub_attr)))
    
        # Pagination
        if strategy == "offset":
            offset = int(arguments.get("offset", 0))
            books = query.offset(offset).limit(limit).all()
        elif strategy == "cursor":
            cursor = arguments.get("cursor")
            if cursor:
                query = query.filter(Book.id > int(cursor))
            books = query.limit(limit).all()
        else:
            # return jsonify({"error": "Invalid pagination strategy"}), 400
            book = query
    
        result = [book.to_dict() for book in books]
        response = make_response(jsonify(result))
        if strategy == "cursor" and books:
            next_cursor = books[-1].id + 1
            response.headers['next-cursor'] = next_cursor
            # return jsonify({"data": result, "next_cursor": next_cursor})

        response.headers["Content-Type"] = "application/json"
        response.headers["status-code"] = 200
        return response

