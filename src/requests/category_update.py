from typing import Dict

from src.requests.validation.invalid_request import InvalidRequest
from src.requests.validation.valid_request import ValidRequest


def build_update_category_request(category: Dict):
    """Factory for requests

    Args:
        client (dict): Dictionary containing client data

    Returns:
        Object: Return ClientCreateInvalidRequest if errors, otherwise, returns
        ClientCreateValidRequest,
    """
    invalid_req = InvalidRequest()

    # TODO o que validar?

    if invalid_req.has_errors():
        return invalid_req

    return ValidRequest(data=category)
