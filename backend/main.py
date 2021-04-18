# Python
from datetime import timedelta
from os import environ

# Flask
from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_jwt import JWT, jwt_required, current_identity

# Internal
from sapia.routes import public, protected
from sapia.config.jwt import connect

app = Flask(__name__)
app.secret_key = 'supersecretkey'

#CORS
CORS(app)

# Bcrypt
bcrypt = Bcrypt(app)
app.config["BCRYPT"] = bcrypt

# Mongo
app.config["MONGO_URI"] = 'mongodb://' + environ['MONGODB_USERNAME'] + ':' + environ['MONGODB_PASSWORD'] + '@' + environ['MONGODB_HOSTNAME'] + ':27017/' + environ['MONGODB_DATABASE']
mongodb_client = PyMongo(app)
db = mongodb_client.db
app.config["DB"] = db

# Instance JWT
app.config["JWT_EXPIRATION_DELTA"] = timedelta(hours=1)
jwt = connect(app)

# Routes
public.PublicRoutes(app).routes()
protected.ProtectedRoutes(app).routes()

if __name__ == '__main__':
	app.run(port=5000, debug=True)