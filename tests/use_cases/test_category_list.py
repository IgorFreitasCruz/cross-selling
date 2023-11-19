"""Test module for category list use cases"""
# pylint: disable=w0621
import uuid
from unittest import mock

import pytest

from src.domain.category import Category
from src.requests.category_list import build_category_list_request
from src.responses import ResponseTypes
from src.use_cases.category_list import category_list_use_case


@pytest.fixture
def domain_categories():
    """Clients Mock"""
    category_1 = Category(
        descricao="Categoria A",
        dt_inclusao="18/11/2023, 14:44:12",
        client_id=1,
        dt_alteracao=None,
        ativo=True,
    )
    category_2 = Category(
        descricao="Categoria B",
        dt_inclusao="18/11/2023, 14:44:12",
        client_id=1,
        dt_alteracao=None,
        ativo=True,
    )
    category_3 = Category(
        descricao="Categoria C",
        dt_inclusao="18/11/2023, 14:44:12",
        client_id=1,
        dt_alteracao=None,
        ativo=False,
    )
    category_4 = Category(
        descricao="Categoria D",
        dt_inclusao="18/11/2023, 14:44:12",
        client_id=1,
        dt_alteracao=None,
        ativo=False,
    )

    return [category_1, category_2, category_3, category_4]


def test_category_list_without_parameters(domain_categories):
    """Test client list without parameter use case

    Args:
        domain_clients (Mock): mock of clients
    """
    repo = mock.Mock()
    repo.list_category.return_value = domain_categories

    request = build_category_list_request()

    response = category_list_use_case(repo, request)

    assert bool(response) is True
    repo.list_category.assert_called_with(filters=None)
    assert response.value == domain_categories


def test_category_list_with_filters(domain_categories):
    repo = mock.Mock()
    repo.list_category.return_value = domain_categories

    qry_filters = {"ativo__eq": True}
    request = build_category_list_request(filters=qry_filters)

    response = category_list_use_case(repo, request)

    assert bool(response) is True
    repo.list_category.assert_called_with(filters=qry_filters)
    assert response.value == domain_categories


def test_category_list_handles_generic_error():
    repo = mock.Mock()
    repo.list_category.side_effect = Exception("Just an error message")

    request = build_category_list_request(filters={})

    response = category_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_category_list_handles_bad_request():
    repo = mock.Mock()

    request = build_category_list_request(filters=5)

    response = category_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }
