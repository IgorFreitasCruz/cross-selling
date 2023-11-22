"""Module for the client create use case"""
from src.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseTypes,
    build_response_from_invalid_request,
)


def client_create_use_case(repo, request):
    """Use case logic

    Args:
        repo (Object): Repository object
        request (Object): Validated request

    Returns:
        ResponseSuccess: If no errors

    Exceptions:
        ResponseFailure: If errors
    """
    if not request:
        return build_response_from_invalid_request(request)
    try:
        check_client_exists = repo.list_client(filters={"cnpj__eq": request.data["cnpj"]})
        if check_client_exists:
            return ResponseFailure(ResponseTypes.DOMAIN_ERROR, "O CNPJ já existe")
        clients = repo.create_client(request.data)
        return ResponseSuccess(clients)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
