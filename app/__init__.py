from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.init_app(app)
        from . import routes
        db.create_all()

        from . import migrate
        migrate.load_users('data/users.json')
        migrate.load_orders('data/orders.json')
        migrate.load_offers('data/offers.json')


    return app
