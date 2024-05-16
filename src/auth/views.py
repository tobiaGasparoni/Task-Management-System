from . import auth_blueprint
from flask import request, redirect, url_for

@auth_blueprint.route('/')
def index():
    return {'message': 'Welcome to the auth section of the platform!'}
