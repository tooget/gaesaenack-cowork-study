from app.api import apiRestful
from flask_restplus import Resource


@apiRestful.route('/index')
class Index(Resource):

    def get(self):
        return {"result" : "This is a return string of Index page"}, 200