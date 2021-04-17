from datetime import datetime
from flask import jsonify, Response, request
from flask_jwt import jwt_required, current_identity
from bson.objectid import ObjectId
import json

class ProtectedRoutes():

    def __init__(self, app):
        self.app = app
        self.db = app.config["DB"]
        self.bcrypt = app.config["BCRYPT"]

    def routes(self):

        @self.app.route('/protected')
        @jwt_required()
        def protected():
            return jsonify({
                'si se pudo': '%s' % current_identity
            })

        @self.app.route('/update/user', methods=["POST"])
        @jwt_required()
        def update_user():
            try:
                data = request.json

                obj = {
                    "name": data['name'],
                    "lastname": data['lastname'],
                }

                if data.get('password', False):
                    obj["password"] = self.bcrypt.generate_password_hash(
                        data['password'])

                self.db.user.update_one({'_id': ObjectId('%s' % current_identity)}, {"$set": obj })

                return jsonify({"message": "success"})
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")

        @self.app.route('/update/profile', methods=["POST"])
        @jwt_required()
        def update_profile():
            try:
                data = request.json

                obj = {
                    "date_of_birth": datetime.strptime(data['date_of_birth'], '%d-%m-%Y'),
                    "bio": data['bio'],
                    "phone_number": data['phone_number'],
                }

                self.db.user.update_one({'_id': ObjectId('%s' % current_identity)}, {"$set": obj })

                return jsonify({"message": "success"})
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")
