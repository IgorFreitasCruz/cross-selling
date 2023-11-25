"""Module for application configuration"""
from flask import Flask
from . import init_app


def create_app(config_name):
    """Application configuration
    Args:
        config_name (Object): Object containing the application configuration

    Returns:
        Object: Instance of application
    """
    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"
    ### Add configuração
    app.config.from_object(config_module)
    ### Registrar rotas
    init_app(app)

    return app
