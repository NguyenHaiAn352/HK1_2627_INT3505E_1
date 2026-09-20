from flask import Flask, jsonify, request, make_response
import sqlite3
import hashlib
app = Flask(__name__)

DEFAULT_SIZE = 20
MAX_SIZE = 100

def fetch_books():
    con = sqlite3.connect("books.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    books_list = [dict(row) for row in rows]
    con.close()
    return books_list

# Pagination, Filter, HATEOAS
@app.route("/books")
def book_get():
    try:
        page = request.args.get("page", 1)
        size = request.args.get("size", DEFAULT_SIZE)
    except ValueError:
        return jsonify({"Error":"Page and size must be integers."}), 400
    page = max(int(page), 1)
    size = max(min(int(size), 100), 1)

    filtered = fetch_books()
    author = request.args.get("author", "") 
    query = request.args.get("q", "").lower()
    if author:
        filtered = [b for b in filtered if b["author"].lower() == author.lower()]
    if query:
        filtered = [b for b in filtered if query in b["title"].lower()]

    start = (page - 1) * size
    end = start + size
    items = filtered[start:end]
    last_page = (len(filtered) + size - 1) / size

    def page_link(page): return f"/books?page={page}&size={size}"
    link = {"self": {"href": page_link(page)}
            , "first": {"href": page_link(1)}
            , "last": {"href": page_link(max(last_page, 1))}}
    if page > 1:
        link["prev"] = {"href": page_link(page-1)}
    if end < len(filtered):
        link["next"] = {"href": page_link(page+1)}


    body = {"data": items, "pagination":{"page": page, "size": size, "total": len(filtered),
                                         "number of pages": last_page}
            , "_links": link}
    result = make_response(jsonify(body), 200)
    result.headers["Cache-Control"] = "max-age=30, public"
    return result

# curl.exe http://127.0.0.1:5000/books/1
# curl.exe -H "If-None-Match:-ETag-" http://127.0.0.1:5000/books/1
@app.route("/books/<int:id>")
def book_tag(id):
    books_list = fetch_books()
    book = books_list[id]
    etag = hashlib.md5(book["name"].encode()).hexdigest()

    if request.headers.get("If-None-Match") == etag:
        return make_response("Unchanged"), 304

    response = make_response(book)
    response.headers["ETag"] = etag
    return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)