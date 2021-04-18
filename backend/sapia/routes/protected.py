from datetime import datetime
from flask import jsonify, Response, request
from flask_jwt import jwt_required, current_identity
from bson.objectid import ObjectId
import json
from sapia.models.user import User

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
                    "date_of_birth": datetime.strptime(data['date_of_birth'], '%Y-%m-%d'),
                    "bio": data['bio'],
                    "phone_number": data['phone_number'],
                    "headquarter": data['headquarter'],
                    "program": data['program'], 
                }

                self.db.user.update_one({'_id': ObjectId('%s' % current_identity)}, {"$set": obj })

                return jsonify({"message": "success"})
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")

        @self.app.route('/get/user', methods=["GET"])
        @jwt_required()
        def get_user():
            db_user = self.db.user.find_one({'_id': ObjectId('%s' % current_identity)})
            user = User.from_query(db_user)
            return jsonify(user.toDictRespose())

        @self.app.route('/get/detail/<id>', methods=["GET"])
        @jwt_required()
        def get_detail(id):
            try:
   
                db_user = self.db.user.find_one({ "_id": ObjectId(id) })
                user = User.from_query(db_user)

                return jsonify(user.toDictRespose())
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")

        @self.app.route('/get/all', methods=["GET"])
        @jwt_required()
        def get_all_users():
            try:
                user_list = []
                db_users = self.db.user.find({})

                for db_user in db_users:
                    user = User.from_query(db_user)
                    user_list.append(user.toDictRespose()) 

                return jsonify(user_list)
            except Exception as e:
                return Response(json.dumps({"message": str(e)}), status=400, content_type="application/json")