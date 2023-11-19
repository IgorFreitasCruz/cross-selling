"""Test module for create category"""
from unittest import mock

from src.use_cases.category_create import category_create_use_case
from src.requests.category_create import build_create_category_request

category = {
    "descricao": "description text",
    "dt_inclusao": "18/11/2023, 14:44:12",
    "dt_alteracao": None,
    "ativo": True,
    "client_id": [1],
}


def test_create_category():
    repo = mock.Mock()
    repo.create_category.return_value = category

    request = build_create_category_request(category)

    result = category_create_use_case(repo, request)

    repo.create_category.assert_called_with(category)
    assert result.value == category
