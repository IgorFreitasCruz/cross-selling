"""Test module for client list use cases"""
# pylint: disable=w0621
import uuid
from unittest import mock

import pytest

from src.domain.client import Client
from src.use_cases.client_list import client_list_use_case


@pytest.fixture
def domain_clients():
    """Clients Mock"""
    client_1 = Client(
        code=uuid.uuid4(),
        razao_social="My company 1",
        cnpj="00.000.000/0000-01",
        email="mycompany_1@email.com",
    )
    client_2 = Client(
        code=uuid.uuid4(),
        razao_social="My company 2",
        cnpj="00.000.000/0000-02",
        email="mycompany_1@email.com",
    )
    client_3 = Client(
        code=uuid.uuid4(),
        razao_social="My company 3",
        cnpj="00.000.000/0000-03",
        email="mycompany_1@email.com",
    )
    client_4 = Client(
        code=uuid.uuid4(),
        razao_social="My company 4",
        cnpj="00.000.000/0000-04",
        email="mycompany_1@email.com",
    )

    return [client_1, client_2, client_3, client_4]


def test_client_list_without_parameters_use_case(domain_clients):
    """Test client list without parameter use case

    Args:
        domain_clients (Mock): mock of clients
    """
    repo = mock.Mock()
    repo.list.return_value = domain_clients

    result = client_list_use_case(repo)

    repo.list.assert_called_with()
    assert result == domain_clients
