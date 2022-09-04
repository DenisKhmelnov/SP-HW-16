import json
from . import models, db
from flask import current_app as app, request, jsonify, redirect


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        result = []
        for user in db.session.query(models.User).all():
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

        return jsonify(result), 200


@app.route("/users/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user(uid):
    with db.session.begin():
        user = models.User.query.get(uid)

        if request.method == "GET":
            return jsonify(user.to_dict())

        elif request.method == "PUT":
            user_data = request.json
            user.first_name = user_data["first_name"]
            user.last_name = user_data["last_name"]
            user.age = user_data["age"]
            user.email = user_data["email"]
            user.role = user_data["role"]
            user.phone = user_data["phone"]

            db.session.add(user)
            return redirect(f"/users/{uid}", code=302)

        elif request.method == "DELETE":
            db.session.delete(user)
            return redirect("/users", code=302)


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())
        return jsonify(result)
    elif request.method == "POST":
        order_data = request.json
        new_order = models.Order(**order_data)

        db.session.add(new_order)
        db.session.commit()

        result = []
        for order in models.Order.query.all():
            result.append(order.to_dict())

        return jsonify(result), 200


@app.route("/orders/<int:oid>", methods=["GET", "PUT", "DELETE"])
def order(oid):
    with db.session.begin():
        order = models.Order.query.get(oid)
        if request.method == "GET":
            return jsonify(order.to_dict())
        elif request.method == "PUT":
            user_data = request.json
            order.name = user_data["name"]
            order.description = user_data["description"]
            order.start_date = user_data["start_date"]
            order.end_date = user_data["end_date"]
            order.address = user_data["address"]
            order.price = user_data["price"]
            order.customer_id = user_data["customer_id"]
            order.executor_id = user_data["executor_id"]

            db.session.add(order)
            return redirect(f"/orders/{oid}", code=302)
        elif request.method == "DELETE":
            db.session.delete(order)
            return redirect("/orders", code=302)


@app.route("/offers", methods=["GET", "POST"])
def offers():
    if request.method == "GET":
        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())
        return jsonify(result)
    elif request.method == "POST":
        offer_data = request.json
        new_offer = models.Offer(**offer_data)

        db.session.add(new_offer)
        db.session.commit()

        result = []
        for offer in models.Offer.query.all():
            result.append(offer.to_dict())

        return jsonify(result), 200


@app.route("/offers/<int:oid>", methods=["GET", "PUT", "DELETE"])
def offer(oid):
    with db.session.begin():
        offer = models.Offer.query.get(oid)
        if request.method == "GET":
            return jsonify(offer.to_dict())
        elif request.method == "PUT":
            offer_data = request.json
            offer.order_id = offer_data["order_id"]
            offer.executor_id = offer_data["executor_id"]

            db.session.add(offer)
            return redirect(f"/offers/{oid}")

        elif request.method == "DELETE":
            db.session.delete(offer)
            return redirect("/offers", code=302)
