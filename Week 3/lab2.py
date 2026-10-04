from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean

app = Flask(__name__)
app.config['SERVER_NAME'] = "lab2"

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab3.db'
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    def to_dict(self):
       return {
          "id": self.id,
          "name": self.name
       }

with app.app_context():
    db.drop_all()
    db.create_all()
    user1 = User(id= 1, name="Sunder")
    db.session.add(user1)
    db.session.commit()

class APIProblem(Exception):
    def __init__(self, type, title, status, detail=None, instance=None):
       self.type = type
       self.title = title
       self.status = status
       self.detail = detail
       self.instance = instance

@app.errorhandler(APIProblem)
def client_exception_handler(e):
   body = {
      "type": e.type,
      "title": e.title,
      "status": e.status,
      "detail": e.detail or "None",
      "instance": e.instance or "None"
   }

   response = make_response(jsonify(body))
   response.status_code = e.status
   response.headers["Content-Type"] = "application/problem+json"
   return response

@app.get("/users/<int:id>")
def get_user(id):
   user = User.query.get(id)
   if not user:
      raise APIProblem(
         type="user-not-found",
         title="User not found.",
         status=404,
         instance="/users/" + str(id),
      )
   return jsonify(user.to_dict())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)