from flask import Flask, jsonify, request, make_response
from app import app

products = []

@app.route("/products", methods = ["GET"])
def list_products():
    resp = make_response(jsonify({
        "items": products
    }))
    resp.headers["description"] = "ok"
    resp.headers["status_code"] = 200
    return resp

@app.route("/products", methods=["POST"])
def create_product():
    if not request.is_json:
        return jsonify({
            "error": "unprocessable content"
        }), 422
    body = request.get_json(force=True)

    product = {
        "id": len(products) + 1,
        "name": body.get("name"),
        "price": body.get("price")
    }

    products.append(product)
    return make_response(jsonify(product), 201)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)

    if product is None:
        return make_response(
            jsonify({"error": "Product not found"}),
            404
        )
    
    return make_response(jsonify(product), 200)