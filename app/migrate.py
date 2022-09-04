import json
from . import models, db


def load_data(file_path):
    with open(file_path) as file:
        return json.load(file)


def load_users(file_path):
    users = load_data(file_path)

    for user in users:
        new_user = models.User(**user)
        db.session.add(new_user)
    db.session.commit()


def load_orders(file_path):
    orders = load_data(file_path)

    for order in orders:
        new_order = models.Order(**order)
        db.session.add(new_order)
    db.session.commit()


def load_offers(file_path):
    offers = load_data(file_path)
    for offer in offers:
        new_offer = models.Offer(**offer)
        db.session.add(new_offer)
    db.session.commit()
