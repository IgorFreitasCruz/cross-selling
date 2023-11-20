from src.requests.category_create import build_create_category_request


def test_build_category_create_request():
    category = {
        "descricao": "description text",
        "client_id": 1,
    }
    request = build_create_category_request(category)

    assert bool(request) is True


def test_build_category_create_request_without_client_id():
    category = {
        "descricao": "description text",
        "client_id": "",
    }
    request = build_create_category_request(category)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "value"
    assert bool(request) is False


def test_build_category_create_request_with_client_id_as_string():
    category = {
        "descricao": "description text",
        "client_id": "1",
    }
    request = build_create_category_request(category)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "value"
    assert bool(request) is False
