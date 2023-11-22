"""Module for structured client requests objects"""
import uuid
from datetime import datetime
from typing import Dict

from src.requests.validation.invalid_request import InvalidRequest
from src.requests.validation.valid_request import ValidRequest
from src.validators.cnpj import is_valid_cnpj
from src.validators.email import is_valid_email


def build_create_client_request(client: Dict):
    """Factory for requests

    Args:
        client (dict): Dictionary containing client data

    Returns:
        Object: Return InvalidRequest if errors, otherwise, returns
        ValidRequest,
    """
    invalid_req = InvalidRequest()

    if not is_valid_cnpj(client["cnpj"]):
        invalid_req.add_error("value", "Invalid CNPJ")

    if not is_valid_email(client["email"]):
        invalid_req.add_error("value", "Invalid e-mail")

    if invalid_req.has_errors():
        return invalid_req

    client.update({"code": uuid.uuid4()})
    return ValidRequest(data=client)
