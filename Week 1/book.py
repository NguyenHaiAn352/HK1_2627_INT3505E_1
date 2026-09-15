from flask import Flask, jsonify, request
from book_logic import book_create, book_get, book_update, book_delete
app = Flask(__name__)

books_data = {
    "1": {"name": "The Silent Code", "rate": 4.8, "year": 1885},
    "2": {"name": "Echoes of Tomorrow", "rate": 4.6, "year": 2005},
    "3": {"name": "Whispers in the Library", "rate": 4.9, "year": 1872},
    "4": {"name": "Beyond the Horizon", "rate": 4.7, "year": 1972},
    "5": {"name": "Fragments of Light", "rate": 4.5, "year": 1833},
    "6": {"name": "The Quantum Garden", "rate": 4.3, "year": 2001},
    "7": {"name": "Dreams of Steel", "rate": 4.4, "year": 1895},
    "8": {"name": "The Forgotten Algorithm", "rate": 4.8, "year": 2008},
    "9": {"name": "Voices of the Deep", "rate": 4.6, "year": 1855},
    "10": {"name": "Chronicles of Ember", "rate": 4.9, "year": 1999},
    "11": {"name": "The Infinite Path", "rate": 4.7, "year": 1821},
    "12": {"name": "Shadows of the Mind", "rate": 4.5, "year": 1880},
    "13": {"name": "The Last Equation", "rate": 4.8, "year": 2003},
    "14": {"name": "A Symphony of Stars", "rate": 4.6, "year": 1847},
    "15": {"name": "The Glass Horizon", "rate": 4.4, "year": 1969},
    "16": {"name": "Echo Chamber", "rate": 4.3, "year": 1890},
    "17": {"name": "The Binary Heart", "rate": 4.7, "year": 1869},
    "18": {"name": "Threads of Reality", "rate": 4.9, "year": 2007},
    "19": {"name": "The Crimson Archive", "rate": 4.6, "year": 1832},
    "20": {"name": "Winds of Eternity", "rate": 4.8, "year": 2009},
    "21": {"name": "Python of the Wild", "rate": 4.0, "year": 1801}
}

next_book_id = 22

# curl.exe http://127.0.0.1:5000/books?q=Echo%20Chamber
@app.route("/books", methods=["GET"])
def book_list_route():
    filtered_books = [b for b in books_data.values()]
    q = str(request.args.get("q", "").strip().lower())
    sorter = str(request.args.get("sort", "")).strip().lower()
    min_year = int(request.args.get("year", 0))
    if not q and not sorter and min_year == 0: # No querying
        b_list = books_data.values()
        return jsonify(list(b_list)), 200
    if q:
        filtered_books = [b for b in filtered_books if q in b["name"].lower().split()]
    if sorter:
        filtered_books = sorted(filtered_books, key=lambda b: b["name"])
    if min_year:
        filtered_books = [b for b in filtered_books if b["year"] >= min_year]
    return jsonify(filtered_books), 200

@app.route("/books/<book_id>", methods=["GET"])
def book_get_route(book_id):
    book = book_get(books_data, book_id)
    if not book:
        return jsonify({"Error":"Book does not exist."}), 404
    else:
        return jsonify(book), 200

@app.route("/books", methods=["POST"])
def book_create_route():
    global next_book_id
    book = request.get_json(silent=True) or {}
    keys_set = books_data["1"].keys()
    try:
        books_data.update(book_create(book, keys_set, next_book_id))
        next_book_id += 1
        return jsonify(books_data), 201
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

    # if not name or not rate:
    #     return jsonify({"Error":"Invalid book information"}), 400
    # books_data.update({str(next_book_id): {"name":name, "rate":rate}})
    # next_book_id += 1
    # return jsonify(books_data), 201

# curl.exe -X PUT http://127.0.0.1:5000/books/1 -H "Content-Type:application/json" -d '{\"name\":\"The Code\"}'
@app.route("/books/<book_id>", methods=["PUT", "DELETE"])
def book_modify_route(book_id):
    book = book_get(books_data, book_id)
    if not book:
        return jsonify({"Error":"Book does not exist."}), 404
    if request.method == "PUT":
        input_data = request.get_json(silent=True) or {}
        book_update(book, input_data)
        return jsonify(book), 200
    book_delete(books_data, book_id)
    return "", 204

if __name__ == "__main__":
    app.run(host="127.0.0.1", port= 5000, debug=True)