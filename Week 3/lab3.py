from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean
import random
app = Flask(__name__)

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab3.db'
db.init_app(app)

class Order(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str]

statuses = ["paid", "pending"]
orders = []

with app.app_context():
    db.drop_all()
    db.create_all()

    # statuses = ["paid", "pending"]
    # orders = []
    # for i in range(3, 13):  # starting from id=3 to id=12
    #   status = random.choice(statuses)
    #   order = Order(id=i, status=status)
    #   orders.append(order)

    order1 = Order(id=1, status='paid')
    order2 = Order(id=2, status='pending')
    order3 = Order(id=3, status='paid')
    order4 = Order(id=4, status='pending')
    order5 = Order(id=5, status='paid')
    order6 = Order(id=6, status='pending')
    order7 = Order(id=7, status='paid')
    order8 = Order(id=8, status='pending')
    order9 = Order(id=9, status='paid')
    order10 = Order(id=10, status='pending')

    # db.session.add_all(orders)
    db.session.add_all([
        order1, order2, order3, order4, order5,
        order6, order7, order8, order9, order10
    ])

    db.session.commit()

# curl.exe 'http://127.0.0.1:5000/orders?status=paid'

@app.route('/orders', methods=['GET'])
def get_order():
  # Cursor-based
  cursor = request.args.get('cursor')
  limit = request.args.get('limit', 10)

  query = Order.query.order_by(Order.id)

  if not cursor.isdigit():
     return make_response(jsonify({"status": 400}))

  if query.count() < int(cursor):
     return make_response(jsonify({"status": 400}))

  if cursor:
    query = query.filter(Order.id > cursor)

  # Filtering
  status = request.args.get('status', None)
  customer_id = request.args.get('customer_id', 0)

  if status:
     query = query.filter_by(status= status)
  if customer_id:
     query = query.filter_by(id= customer_id)

  # Sorting
  sort = request.args.get('sort', None)
  if sort:
     query = query.order_by(getattr(Order, 'id'))

  # Sparsed Fieldsets
  fields = request.args.get('fields', None)
  if fields:
     items = fields.split(',')

  orders = query.limit(limit).all()
  results = []
     
  for order in orders:
    if fields:
      data = {field: getattr(order, field) for field in items if hasattr(order, field)}
    results.append(data)

  # results = [{"id": order.id, "status": order.status} for order in orders]

  next_cursor = results[-1]["id"] if results else None
  # dict_result = [{"id": order.id, "status": order.status} for order in results]

  response = make_response(jsonify({"orders": results, "next_cursor": next_cursor}))
  return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)