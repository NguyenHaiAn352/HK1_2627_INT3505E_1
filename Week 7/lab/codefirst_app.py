from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Api, Blueprint, abort
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from marshmallow import Schema, fields
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["API_TITLE"] = "Product API"
app.config["API_VERSION"] = "1.0.0"
app.config["OPENAPI_VERSION"] = "3.0.3"
api = Api(app)

products = []

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

blp = Blueprint(
    "products",
    __name__,
    url_prefix="/products",
    description="Product operations"
)

@blp.route("/")
class ProductsResource(MethodView):
    @blp.response(200, ProductSchema)
    def get(self):
        """List products"""
        return jsonify({
            "items": products
        })

    @blp.arguments(ProductSchema)
    @blp.response(201, ProductSchema)
    def post(self, product_data):
        """Create product"""
        if not request.is_json:
            return jsonify({
                "error": "unprocessable content"
            }), 422
        body = request.get_json(force=True)
        
        product = {
            "id": len(products) + 1,
            "name": body.get("name"),
            "price": body.get("price")
        }
    
        products.append(product)
    
        return make_response(jsonify(product))

blp.add_url_rule("", view_func=ProductsResource.as_view("product_list"))
api.register_blueprint(blp)

if __name__ == "__main__":
    app.run(port=5000)