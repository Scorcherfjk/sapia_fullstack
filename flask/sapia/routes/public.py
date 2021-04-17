import json
import hashlib
from datetime import datetime
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
                    id=None,
                    name=data['name'],
                    lastname=data['lastname'],
                    phone_number=data['phone_number'],
                    date_of_birth=datetime.strptime(data['date_of_birth'], '%Y-%m-%d'),
                    email=data['email'],
                    password=self.bcrypt.generate_password_hash(
                        data['password']),
                    headquarter=data.get('headquarter', None),
                    program=data.get('program', None),
                )
                obj = user.toDict()

                self.db.user.insert_one(obj)

                return jsonify({"message": "success"})
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")
