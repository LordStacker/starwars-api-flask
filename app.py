import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Vehicles, Planets, Characters, Favorite
from flask_migrate import Migrate

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(BASEDIR, "test.db") 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['ENV'] = "development"
app.config['DEBUG'] = True

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "GET":
        user = User.query.get(1)
        if user is not None:
            return jsonify(user.serialize_just_username())
    else:
        user = User()
        user.name = request.json.get("name")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        user.isActive = request.json.get("isActive")

        db.session.add(user)
        db.session.commit()

    return jsonify(user.serialize()), 200

@app.route("/vehicles", methods=["POST", "GET"])
def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serializa_just_name_manufacturer())
    else:
        vehicles = Vehicles()
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.crew = request.json.get("crew")
        vehicles.consumables = request.json.get("consumables")
        vehicles.manufacturer = request.json.get("manufacturer")

        db.session.add(vehicles)
        db.session.commit()

    return jsonify(vehicles.serialize())
@app.route("/characters", methods=["POST", "GET"])
def characters():
    if request.method == "GET":
        characters = Characters.query.get(1)
        if characters is not None:
            return jsonify(characters.serializa_just_name_gender())
    else:
        characters = Characters()
        characters.name = request.json.get("name")
        characters.gender = request.json.get("gender")
        characters.height = request.json.get("height")
        characters.skin_color = request.json.get("skin_color")

        db.session.add(characters)
        db.session.commit()

    return jsonify(characters.serialize())
@app.route("/planets", methods=["POST", "GET"])
def planets():
    if request.method == "GET":
        planets = Planets.query.get(1)
        if planets is not None:
            return jsonify(planets.serialize_name_terrain())
    else:
        planets = Planets()
        planets.name = request.json.get("name")
        planets.population = request.json.get("population")
        planets.terrain = request.json.get("terrain")
        planets.climate = request.json.get("climate")
        planets.gravity = request.json.get("gravity")

        db.session.add(planets)
        db.session.commit()

    return jsonify(planets.serialize())
@app.route("/favorites", methods=["POST", "GET"])
def favorites():
    if request.method == "GET":
        favorites = Favorite.query.get(1)
        if favorites is not None:
            return jsonify(favorites.serialize_just_user_fav())
    else:
        favorites = Favorite()
        favorites.fav_name = request.json.get("fav_name")
        favorites.fav_Section = request.json.get("fav_section")

        db.session.add(favorites)
        db.session.commit()

    return jsonify(favorites.serialize())

if __name__ == "__main__":
    app.run(host='localhost', port=8080)