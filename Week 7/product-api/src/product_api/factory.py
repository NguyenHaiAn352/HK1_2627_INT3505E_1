from flask import Flask
from . import models  # Ensure all SQLAlchemy models are registered.
from .extensions import db, migrate
from .api.products import products_bp
from .api.orders import orders_bp
from .api.healthz import health_bp
from .config import DefaultConfig


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or DefaultConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)
    app.register_blueprint(health_bp)

    if app.config.get("AUTO_CREATE_DB", False):
        with app.app_context():
            db.create_all()

    return app
