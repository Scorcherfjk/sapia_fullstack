# Python
from datetime import timedelta
from os import urandom

# Flask
from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required, current_identity

# Internal
from sapia.routes import public, protected
from sapia.config.jwt import connect

app = Flask(__name__)
app.secret_key = urandom(24)

# Bcrypt
bcrypt = Bcrypt(app)
app.config["BCRYPT"] = bcrypt

# Mongo
mongodb_client = PyMongo(app, uri="mongodb://root:example@localhost:27017/sapia?authSource=admin")
db = mongodb_client.db
app.config["DB"] = db

# Instance JWT
jwt = connect(app)

# Routes
public.PublicRoutes(app).routes()
protected.ProtectedRoutes(app).routes()

if __name__ == '__main__':
	app.run(port=5000, debug=True)