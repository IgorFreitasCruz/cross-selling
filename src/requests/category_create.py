"""Module for structured category requests objects"""
from .validation.invalid_request import InvalidRequest
from .validation.valid_request import ValidRequest


def build_create_category_request(category):
    """Factory for requests

    Args:
        category (dict): Dictionary containing category data

    Returns:
        Object: Return InvalidRequest if errors, otherwise, returns ValidRequest
    """
    invalid_req = InvalidRequest()

    if not isinstance(category["client_id"], list):
        invalid_req.add_error(
            parameter="attribute", message="client_id não é uma lista"
        )

    if not len(category["client_id"]) > 0:
        invalid_req.add_error(
            parameter="attribute", message="client_id não deve estar vazio"
        )

    if invalid_req.has_errors():
        return invalid_req

    return ValidRequest(data=category)
