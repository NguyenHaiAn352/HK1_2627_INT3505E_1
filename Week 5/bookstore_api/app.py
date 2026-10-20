from flask import Flask, request, make_response, jsonify
from models import Book, Category, Author, db
import routes.books as BookRoute

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./bookstore.db"
db.init_app(app)

def initialize_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Categories
        fiction = Category(name="Fiction", description="Novels and stories")
        science = Category(name="Science", description="Educational and scientific books")
        history = Category(name="History", description="Historical accounts and biographies")
        fantasy = Category(name="Fantasy", description="Magical and imaginative tales")
        db.session.add_all([fiction, science, history, fantasy])
        db.session.commit()

        # Authors
        author1 = Author(name="George Orwell", role="lead")
        author2 = Author(name="Isaac Newton", role="lead")
        author3 = Author(name="Jane Austen", role="co")
        author4 = Author(name="J.K. Rowling", role="lead")
        author5 = Author(name="Yuval Noah Harari", role="co")
        db.session.add_all([author1, author2, author3, author4, author5])
        db.session.commit()

        # Books — diverse prices, categories, and authors
        books = [
            Book(title="1984", price=9.99, category=fiction, authors=[author1]),
            Book(title="Animal Farm", price=9.99, category=fiction, authors=[author1]),
            Book(title="Principia Mathematica", price=19.99, category=science, authors=[author2]),
            Book(title="Pride and Prejudice", price=12.50, category=fiction, authors=[author3]),
            Book(title="Emma", price=10.00, category=fiction, authors=[author3]),
            Book(title="Harry Potter and the Sorcerer's Stone", price=15.99, category=fantasy, authors=[author4]),
            Book(title="Harry Potter and the Chamber of Secrets", price=16.99, category=fantasy, authors=[author4]),
            Book(title="Sapiens: A Brief History of Humankind", price=18.50, category=history, authors=[author5]),
            Book(title="Homo Deus: A Brief History of Tomorrow", price=10.00, category=history, authors=[author5]),
            Book(title="Opticks", price=14.75, category=science, authors=[author2]),
        ]
        db.session.add_all(books)
        db.session.commit()

@app.get("/books")
def list_books():
    arguments = request.args
    query = Book.query
    return BookRoute.listBooks(arguments, query)

if __name__ == "__main__":
    initialize_database()
    app.run(host="127.0.0.1", port=5000, debug=True)