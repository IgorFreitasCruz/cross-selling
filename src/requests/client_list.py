"""Module for structured requests objects"""
from collections.abc import Mapping


class ClientListInvalidRequest:
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


class ClientListValidRequest:
    """ClientListValidRequest"""

    def __init__(self, filters=None) -> None:
        self.filters = filters

    def __bool__(self):
        return True


def build_client_list_request(filters=None):
    """Factory for requests

    Args:
        filters (Dict, optional): Dictionary containing parameter filter and
        value. Defaults to None.

    Returns:
        Object: Return ClientListInvalidRequest if errors, otherwise, returns
        ClientListValidRequest,
    """
    accepted_filters = ["code__eq", "ativo__eq"]
    invalid_req = ClientListInvalidRequest()

    if filters is not None:
        if not isinstance(filters, Mapping):
            invalid_req.add_error("filters", "Is not iterable")
            return invalid_req

        for key, value in filters.items():
            if key not in accepted_filters:
                invalid_req.add_error("filters", f"Key {key} cannot be used")

        if invalid_req.has_errors():
            return invalid_req

    return ClientListValidRequest(filters=filters)
