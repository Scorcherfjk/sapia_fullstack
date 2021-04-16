import hashlib
from flask_jwt import JWT
from bson.objectid import ObjectId
from sapia.models.user import User


def authenticate(username, password):
    db_user = db.user.find_one({"email": username})
    if db_user and bcrypt.check_password_hash(db_user["password"], password):
        user = User.short(str(db_user["_id"]), db_user["email"], db_user["password"])
        return user


def identity(payload):
    user_id = payload['identity']
    db_user = db.user.find_one({"_id": ObjectId(user_id)})
    user = User.short(str(db_user["_id"]), db_user["email"], db_user["password"])
    return user


def connect(app):
    global db
    global bcrypt
    db = app.config["DB"]
    bcrypt = app.config["BCRYPT"]

    JWT(app, authenticate, identity)
