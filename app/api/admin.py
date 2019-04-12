from app.api import apiRestful
from flask_restplus import Resource



class Admin:

    @apiRestful.route('/admin/anotheradmin')
    class AnotherAdminView(Resource):
        
        def get(self):
            return {"return" : "Hello World from AnotherMyAdmin!"}, 200


    @apiRestful.route('/admin/myadminview')
    class MyAdminView(Resource):
        
        def get(self):
            return {"return" : "Hello World from MyAdmin!"}, 200
