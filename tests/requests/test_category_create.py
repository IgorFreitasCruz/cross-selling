from src.requests.category_create import build_create_category_request


def test_build_category_create_request():
    category = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }
    request = build_create_category_request(category)

    assert bool(request) is True


def test_build_category_create_request_without_cliend_id():
    category = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [],
    }
    request = build_create_category_request(category)

    assert bool(request) is False
