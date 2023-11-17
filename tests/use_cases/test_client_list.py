"""Test module for client list use cases"""
# pylint: disable=w0621
import uuid
from unittest import mock

import pytest

from src.domain.client import Client
from src.requests.client_list import build_client_list_request
from src.responses import ResponseTypes
from src.use_cases.client_list import client_list_use_case


@pytest.fixture
def domain_clients():
    """Clients Mock"""
    client_1 = Client(
        code=uuid.uuid4(),
        razao_social="My company 1",
        cnpj="00.000.000/0000-01",
        email="mycompany_1@email.com",
        ativo=True,
    )
    client_2 = Client(
        code=uuid.uuid4(),
        razao_social="My company 2",
        cnpj="00.000.000/0000-02",
        email="mycompany_1@email.com",
        ativo=True,
    )
    client_3 = Client(
        code=uuid.uuid4(),
        razao_social="My company 3",
        cnpj="00.000.000/0000-03",
        email="mycompany_1@email.com",
        ativo=True,
    )
    client_4 = Client(
        code=uuid.uuid4(),
        razao_social="My company 4",
        cnpj="00.000.000/0000-04",
        email="mycompany_1@email.com",
        ativo=True,
    )

    return [client_1, client_2, client_3, client_4]


def test_client_list_without_parameters(domain_clients):
    """Test client list without parameter use case

    Args:
        domain_clients (Mock): mock of clients
    """
    repo = mock.Mock()
    repo.list.return_value = domain_clients

    request = build_client_list_request()

    response = client_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_clients


def test_client_list_with_filters(domain_clients):
    repo = mock.Mock()
    repo.list.return_value = domain_clients

    qry_filters = {"code__eq": 5}
    request = build_client_list_request(filters=qry_filters)

    response = client_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response.value == domain_clients


def test_client_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception("Just an error message")

    request = build_client_list_request(filters={})

    response = client_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_client_list_handles_bad_request():
    repo = mock.Mock()

    request = build_client_list_request(filters=5)

    response = client_list_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "filters: Is not iterable",
    }
