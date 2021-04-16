from flask import jsonify
import hashlib

class PublicRoutes():
    def __init__(self, app):
        self.app = app
        self.db = app.config["DB"]
        self.bcrypt = app.config["BCRYPT"]

    def routes(self):

        @self.app.route('/')
        def index():
            return jsonify({
                'hola': "mundo"
            })

        @self.app.route('/create', methods=["POST"])
        def create():
            obj = {
                'name': "user1",
                'password': self.bcrypt.generate_password_hash('abcxyz')
            }

            self.db.user.insert_one(obj)

            return jsonify(obj)
