def book_get(books_data, book_id):
    return books_data.get(str(book_id))

def book_create(name, rate, next_book_id):
    if not name or rate:
        raise ValueError("Invalid book information.")
    new_book = {str(next_book_id): {"name":name, "rate":rate}}
    return new_book

def book_update(book, input_data):
    filtered = {k: v for k, v in input_data.items() if v}
    book.update(filtered)
    return book

def book_delete(books_data, book_id):
    books_data.pop(str(book_id), None)