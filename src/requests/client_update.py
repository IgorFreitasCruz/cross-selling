"""Module for factory of update client requests"""
from src.domain.client import Client
from src.validators.cnpj import is_valid_cnpj
from src.validators.email import is_valid_email

from .validation.invalid_request import InvalidRequest
from .validation.valid_request import ValidRequest


def build_update_client_request(client: Client):
    """Factory for requests

    Args:
        client (dict): Dictionary containing client data

    Returns:
        Object: Return ClientCreateInvalidRequest if errors, otherwise, returns
        ClientCreateValidRequest,
    """
    invalid_req = InvalidRequest()

    if not is_valid_cnpj(client["cnpj"]):
        invalid_req.add_error("value", "Invalid CNPJ")

    if not is_valid_email(client["email"]):
        invalid_req.add_error("value", "Invalid e-mail")

    if invalid_req.has_errors():
        return invalid_req

    return ValidRequest(data=client)
