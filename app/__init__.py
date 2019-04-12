from app.api import apiBlueprint
from flask import Flask


app = Flask(__name__)
app.register_blueprint(apiBlueprint)
app.debug = True

@apiBlueprint.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response