from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

book_authors = db.Table(
    "book_authors",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id"), primary_key=True),
)

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "role": self.role}

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("Category")
    authors = db.relationship("Author", secondary=book_authors)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "authors": [a.to_dict() for a in self.authors],
            "category": self.category.to_dict() if self.category else None,
        }