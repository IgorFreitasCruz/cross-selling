from src.responses import (
    ResponseFailure,
    ResponseSuccess,
    ResponseTypes,
    build_response_from_invalid_request,
)


def category_create_use_case(repo, request):
    if not request:
        return build_response_from_invalid_request(request)
    try:
        client = repo.create_category(category=request.data)
        return ResponseSuccess(client)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
