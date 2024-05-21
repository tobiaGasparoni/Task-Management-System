"""
This contains the application factory for creating flask application instances.
Using the application factory allows for the creation of flask applications configured 
for different environments based on the value of the CONFIG_TYPE environment variable
"""

from flask import Flask
from sqlalchemy import create_engine


### Application Factory ###
def create_app():

    app = Flask(__name__)

    # Register blueprints
    register_blueprints(app)

    # Configure logging
    configure_logging(app)

    # Register error handlers
    register_error_handlers(app)

    return app


### Helper Functions ###
def register_blueprints(app):
    from src.auth import auth_blueprint
    from src.tasks import tasks_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(tasks_blueprint, url_prefix='/tasks')

def register_error_handlers(app):
    # 400 - Bad Request
    @app.errorhandler(400)
    def bad_request(e):
        return {
            'status': 400,
            'error': str(e)
        }

    # 403 - Forbidden
    @app.errorhandler(403)
    def forbidden(e):
        return {
            'status': 403,
            'error': str(e)
        }

    # 404 - Page Not Found
    @app.errorhandler(404)
    def page_not_found(e):
        return {
            'status': 404,
            'error': str(e)
        }

    # 405 - Method Not Allowed
    @app.errorhandler(405)
    def method_not_allowed(e):
        return {
            'status': 405,
            'error': str(e)
        }

    # 500 - Internal Server Error
    @app.errorhandler(500)
    def server_error(e):
        return {
            'status': 500,
            'error': str(e)
        }


def configure_logging(app):
  pass
