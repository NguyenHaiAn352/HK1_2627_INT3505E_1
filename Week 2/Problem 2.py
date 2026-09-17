from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

books_list = []
next_book_id = 1

@app.route("/books/<int:id>")
def book_get(id):
    # Iterating through a list, return the first item that satisfies the condition
    book_id = next((k for k,b in enumerate(books_list) if b["id"] == id), None)
    if book_id is None:
        return jsonify({"Error":"Not found."}), 404
    response = make_response(jsonify(books_list[book_id]), 200)
    response.headers["Cache-Control"]="max-age=60"
    return response

@app.put("/books/<int:id>")
def book_put(id):
    book_id = next((k for k,b in enumerate(books_list) if b["id"] == id), None)
    if book_id is None:
        return jsonify({"Error":"Not found."}), 404
    inputted = request.get_json(silent=True) or {}
    author = inputted.get("author")
    title = inputted.get("title")
    if not author or title:
        return jsonify({"Error":"Author and title are required."}), 422
    books_list[id] = {"id": id, "author": author.strip(), "title": title.strip(), "isbn": inputted.get("isbn"), "price": inputted.get("price")}
    return jsonify(books_list[id]), 200

@app.patch("/books/<int:id>")
def book_patch(id):
    book_id = next((k for k,b in enumerate(books_list) if b["id"] == id), None)
    if book_id is None:
        return jsonify({"Error":"Not found."}), 404
    inputted = request.get_json(silent=True) or {}
    if inputted.get("price") <= 0:
        return jsonify({"Error":"Price must be positive."}), 422
    for k in "author title isbn price".split():
        if k in inputted:
            books_list[id][k] = inputted[k]
    return jsonify(books_list[id]), 200

@app.delete("/books/<int:id>")
def book_delete(id):
    book_id = next((k for k,b in enumerate(books_list) if b["id"] == id), None)
    if book_id is None:
        return jsonify({"Error":"Not found."}), 404
    books_list.pop(id)
    return jsonify(""), 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)