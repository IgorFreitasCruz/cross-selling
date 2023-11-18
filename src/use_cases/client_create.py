"""Module for the client create use case"""
from src.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseTypes,
    build_response_from_invalid_request,
)


def client_create_use_case(repo, request):
    """Client create use case

    Args:
        repo (Object): Client respository

    Returns:
        Client: Dictionary of a new client
    """
    if not request:
        return build_response_from_invalid_request(request)
    try:
        clients = repo.create_client(client=request.client)
        return ResponseSuccess(clients)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
