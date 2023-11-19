# pylint: disable=c0116
from unittest import mock

import pytest

from src.responses import ResponseTypes
from src.use_cases.category_update import category_update_use_case
from src.requests.category_update import build_update_category_request

@pytest.fixture
def category_to_update():
    return {
        "descricao": "categoria D",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [2],
    }


def test_update_client_success(category_to_update):
    repo = mock.Mock()

    repo.update_category.return_value = category_to_update

    request = build_update_category_request(category_to_update)

    response = category_update_use_case(repo, request)

    repo.update_category.assert_called()
    assert response.value == category_to_update
