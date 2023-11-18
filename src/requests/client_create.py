"""Module for structured client requests objects"""
from collections.abc import Mapping

from src.domain.client import Client
from src.validators.cnpj import is_valid_cnpj
from src.validators.email import is_valid_email


class ClientCreateInvalidRequest:
    """ClientListInvalidRequest"""

    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        """Add request errors if they exists

        Args:
            parameter (str): Type of error found in the request
            message (str): Descript of the error that ocurred

        Returns:
            None: This funcion has no return
        """
        self.errors.append({"parameter": parameter, "message": message})

    def has_errors(self):
        """Checks wether an error exists

        Returns:
            Bool: Boolen filed signaling the existance of errors
        """
        return len(self.errors) > 0

    def __bool__(self):
        return False


class ClientCreateValidRequest:
    """ClientListValidRequest"""

    def __init__(self, client: Client):
        self.client = client

    def __bool__(self):
        return True


def build_create_client_request(client: Client):
    """Factory for requests

    Args:
        client (dict): Dictionary containing client data

    Returns:
        Object: Return ClientCreateInvalidRequest if errors, otherwise, returns
        ClientCreateValidRequest,
    """
    invalid_req = ClientCreateInvalidRequest()

    if not is_valid_cnpj(client["cnpj"]):
        invalid_req.add_error("value", "Invalid CNPJ")

    if not is_valid_email(client["email"]):
        invalid_req.add_error("value", "Invalid e-mail")

    if invalid_req.has_errors():
        return invalid_req

    return ClientCreateValidRequest(client)
