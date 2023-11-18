"""Module for application configuration"""
from flask import Flask
from application.rest import client
from application.rest import category


def create_app(config_name):
    """Application configuration
    Args:
        config_name (Object): Object containing the application configuration

    Returns:
        Object: Instance of application
    """
    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(client.blueprint)
    app.register_blueprint(category.blueprint)

    return app
