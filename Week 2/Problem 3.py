from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

DEFAULT_SIZE = 20, MAX_SIZE = 100
books_list = []

# Pagination, Filter, HATEOAS
@app.route("/books")
def book_get():
    try:
        page = request.args.get("page", 1)
        size = request.args.get("size", 20)
    except ValueError:
        return jsonify({"Error":"Page and size must be integers."}), 400
    page = max(page, 1), size = max(min(size, 100), 1)

    filtered = books_list
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

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)