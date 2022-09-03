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
