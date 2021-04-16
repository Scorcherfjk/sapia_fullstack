import json
import hashlib
from flask import jsonify, request, Response

from sapia.models.user import User


class PublicRoutes():
    def __init__(self, app):
        self.app = app
        self.db = app.config["DB"]
        self.bcrypt = app.config["BCRYPT"]

    def routes(self):

        @self.app.route('/create', methods=["POST"])
        def create():
            try:
                data = request.json

                user = User(
                    id = None,
                    name = data['name'],
                    lastname = data['lastname'], 
                    phone_number = data['phone_number'], 
                    date_of_birth = data['date_of_birth'], 
                    email = data['email'], 
                    password = self.bcrypt.generate_password_hash(data['password'])
                    )
                obj = user.toDict()

                self.db.user.insert_one(obj)

                return jsonify({"message": "success"})
            except Exception as e:
                print(e)
                return Response(json.dumps({"message": "error"}), status=400, content_type="application/json")
