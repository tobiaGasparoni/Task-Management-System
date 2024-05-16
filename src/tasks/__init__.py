# This bluepint will deal with all task management functionality 

from flask import Blueprint

tasks_blueprint = Blueprint('tasks', __name__)

from . import views