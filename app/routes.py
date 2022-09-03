import json
from . import models, db
from flask import current_app as app, request, jsonify

@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())
            return jsonify(result), 200
    elif request.method == "POST":
        user_data = request.json
        new_user = models.User(**user_data)

        db.session.add(new_user)
        db.session.commit()

        result = []
        for user in models.User.query.all():
            result.append(user.to_dict())

        return jsonify(**result), 200
