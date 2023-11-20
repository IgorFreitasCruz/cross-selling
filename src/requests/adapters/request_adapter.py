from flask import request as FlaskRequest


class HttpRequest:
    def __init__(
        self,
        headers=None,
        body=None,
        query_params=None,
        path_params=None,
        url=None,
        ipv4=None,
    ) -> None:
        self.headers = headers
        self.body = body
        self.query_params = query_params
        self.path_params = path_params
        self.url = url
        self.ipv4 = ipv4


def request_adapter(request: FlaskRequest) -> HttpRequest:
    """Adapter for the request object. The ideia isa to create a layers to
    receive a request object no metter the web framework used: Flask, Django, FastAPI

    Args:
        request (FlaskRequest): The actual web framework request object

    Returns:
        HttpRequest: Instance of HttpRequest
    """
    body = None
    if request.data:
        body = request.json

    http_request = HttpRequest(
        body=body,
        headers=request.headers,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path,
    )

    return http_request
