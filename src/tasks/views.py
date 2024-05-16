from . import tasks_blueprint
from flask import request, redirect, url_for

@tasks_blueprint.route('/')
def index():
    return {'message': 'Welcome to the task management section of the platform!'}
