from src.requests.category_update import build_update_category_request


def test_build_category_update_request():
    category_to_update = {
        "descricao": "categoria a",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }
    request = build_update_category_request(category_to_update)

    assert bool(request) is True
