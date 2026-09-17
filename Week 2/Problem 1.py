from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

books_list = []
next_book_id = 1

# curl.exe http://127.0.0.1:5000/books
@app.route("/books")
def book_listing():
    return jsonify({"data":books_list, "len": len(books_list)})

# Support portability
# curl.exe -X POST http://127.0.0.1:5000/books -H "Content-Type:application/json" -d '{\"title\":\"Clean Code\", \"author\":\"R.Martin\"}'
# curl.exe -X POST http://127.0.0.1:5000/books -H "Content-Type:application/json" -d '{\"title1\":\"Clean Code\", \"author\":\"R.Martin\"}'
@app.route("/books", methods = ["POST"])
def book_create():
    global next_book_id

    if not request.is_json:
        return jsonify({"Error": "Representation not supported; Must be JSON."}), 415

    if len(books_list) == 0:
        inputted = request.get_json(silent=True) or {}
        new_book = {"id": next_book_id, "data": inputted}
        books_list.append(new_book)
        next_book_id += 1
        response = make_response(jsonify(new_book), 201)
        response.headers["Location"] = f"/books/{new_book['id']}"
        return response

    keys_set = books_list[0]["data"].keys()
    inputted = request.get_json(silent=True) or {}
    inputted_keys = inputted.keys()

    if keys_set != inputted_keys:
        return jsonify({"Error":"Keys not matched with original set."}), 422

    new_book = {"id": next_book_id, "data": {k:v for k,v in inputted.items()}}
    books_list.append(new_book)
    next_book_id += 1

    response = make_response(jsonify(new_book), 201)
    response.headers["Location"] = f"/books/{new_book['id']}"
    return response
    
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
