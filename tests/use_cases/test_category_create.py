"""Test module for create category"""
from unittest import mock
from src.responses import ResponseTypes
from src.use_cases.category_create import category_create_use_case
from src.requests.category_create import build_create_category_request


def test_create_category():
    repo = mock.Mock()

    new_category = {
        "descricao": "description text",
        "client_id": 1,
    }

    new_category_crated = {
        "id": 1,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "descricao": "description text",
        "dt_inclusao": "01/01/2023 00:00:00",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": 1,
    }
    repo.create_category.return_value = new_category_crated

    request = build_create_category_request(new_category)

    result = category_create_use_case(repo, request)

    assert bool(result) is True
    repo.create_category.assert_called_with(new_category)
    assert result.value == new_category_crated


def test_create_category_without_cliend_id():
    repo = mock.Mock()

    new_category = {
        "descricao": "description text",
        "client_id": "",
    }

    request = build_create_category_request(new_category)

    result = category_create_use_case(repo, request)

    assert bool(result) is False
    assert result.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "value: client id must be an integer",
    }
