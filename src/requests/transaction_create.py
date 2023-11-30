import uuid
from typing import Dict

from src.requests.validation.invalid_request import InvalidRequest
from src.requests.validation.valid_request import ValidRequest


def build_transaction_create_request(transaction: Dict):
    """Factory for requests

    Args:
        client (dict): Dictionary containing client data

    Returns:
        Object: Return InvalidRequest if errors, otherwise, returns
        ValidRequest,
    """
    invalid_req = InvalidRequest()

    # FIXME o que validar?

    if invalid_req.has_errors():
        return invalid_req

    transaction.update({'code': uuid.uuid4()})
    return ValidRequest(data=transaction)
