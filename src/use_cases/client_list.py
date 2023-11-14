"""Module for the client list use case"""
from src.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseTypes,
    build_response_from_invalid_request,
)


def client_list_use_case(repo, request):
    """Client list use case

    Args:
        repo (Object): Client respository

    Returns:
        List: List of clients
    """
    if not request:
        return build_response_from_invalid_request(request)
    try:
        clients = repo.list(filters=request.filters)
        return ResponseSuccess(clients)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
