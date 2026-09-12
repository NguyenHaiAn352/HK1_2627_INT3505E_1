# Path param: part of the url, used for identifying specific resources
# Query string: after ? of the url, used for filtering, sorting, etc. optional
from flask import Flask, jsonify,request
app = Flask(__name__)

books_data = {
    "1": {"name": "The Silent Code", "rate": "4.8"},
    "2": {"name": "Echoes of Tomorrow", "rate": "4.6"},
    "3": {"name": "Whispers in the Library", "rate": "4.9"},
    "4": {"name": "Beyond the Horizon", "rate": "4.7"},
    "5": {"name": "Fragments of Light", "rate": "4.5"},
    "6": {"name": "The Quantum Garden", "rate": "4.3"},
    "7": {"name": "Dreams of Steel", "rate": "4.4"},
    "8": {"name": "The Forgotten Algorithm", "rate": "4.8"},
    "9": {"name": "Voices of the Deep", "rate": "4.6"},
    "10": {"name": "Chronicles of Ember", "rate": "4.9"},
    "11": {"name": "The Infinite Path", "rate": "4.7"},
    "12": {"name": "Shadows of the Mind", "rate": "4.5"},
    "13": {"name": "The Last Equation", "rate": "4.8"},
    "14": {"name": "A Symphony of Stars", "rate": "4.6"},
    "15": {"name": "The Glass Horizon", "rate": "4.4"},
    "16": {"name": "Echo Chamber", "rate": "4.3"},
    "17": {"name": "The Binary Heart", "rate": "4.7"},
    "18": {"name": "Threads of Reality", "rate": "4.9"},
    "19": {"name": "The Crimson Archive", "rate": "4.6"},
    "20": {"name": "Winds of Eternity", "rate": "4.8"},
    "21": {"name": "Python of the Wild", "rate": "4.0"}
}

# /books?limit=10&offset=0&q=Python
@app.route("/books", methods=["GET"])
def list_books():
    limit = int(request.args.get("limit", 20))
    q = str(request.args.get("q","")).strip().lower()
    items = [b for b in books_data.values() if q in b["name"].lower()]
    return jsonify({"items": items})

@app.route("/books/<book_id>", methods=["GET"])
# Can force type by using /<int:book_id>
def books(book_id):
    book = books_data.get(book_id)
    if not book:
        return jsonify({"Error": "Book does not exist."}), 404
    else:
        return jsonify(book), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port= 5000, debug=True)