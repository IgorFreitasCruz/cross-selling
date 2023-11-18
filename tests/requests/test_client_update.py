from src.requests.client_update import build_update_client_request


def test_build_client_update_request():
    new_client = {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company",
        "cnpj": "00.000.000/0000-00",
        "email": "mycompany@email.com",
        "ativo": True,
    }
    request = build_update_client_request(new_client)

    assert bool(request) is True