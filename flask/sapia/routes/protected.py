from flask import jsonify
from flask_jwt import jwt_required, current_identity



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
