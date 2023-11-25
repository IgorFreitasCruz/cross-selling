from flask import Blueprint

from .rest.category import category_create, category_list, category_update
from .rest.client import client_create, client_list, client_update
from .rest.product import product_create, product_list, product_update
from .rest.transaction import transaction_create, transaction_list

blueprint = Blueprint("application", __name__)

blueprint.add_url_rule("/clients", view_func=client_create, methods=["POST"])
blueprint.add_url_rule("/clients", view_func=client_list, methods=["GET"])
blueprint.add_url_rule("/clients", view_func=client_update, methods=["PUT"])

blueprint.add_url_rule("/categories", view_func=category_create, methods=["POST"])
blueprint.add_url_rule("/categories", view_func=category_list, methods=["GET"])
blueprint.add_url_rule("/categories", view_func=category_update, methods=["PUT"])

blueprint.add_url_rule("/products", view_func=product_create, methods=["POST"])
blueprint.add_url_rule("/products", view_func=product_list, methods=["GET"])
blueprint.add_url_rule("/products", view_func=product_update, methods=["PUT"])

blueprint.add_url_rule("/transactions", view_func=transaction_create, methods=["POST"])
blueprint.add_url_rule("/transactions", view_func=transaction_list, methods=["GET"])


def init_app(app):
    app.register_blueprint(blueprint)
