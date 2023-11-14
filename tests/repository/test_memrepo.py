"""Test module for client list use case"""
# pylint: disable=w0621
import pytest
from src.repository.memrepo import MemRepo

from src.domain.client import Client


@pytest.fixture
def clients_dicts():
    """Clients Mock"""
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 1",
            "cnpj": "00.000.000/0000-01",
            "email": "mycompany_1@email.com",
        },
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 2",
            "cnpj": "00.000.000/0000-02",
            "email": "mycompany_2@email.com",
        },
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 3",
            "cnpj": "00.000.000/0000-03",
            "email": "mycompany_3@email.com",
        },
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 4",
            "cnpj": "00.000.000/0000-04",
            "email": "mycompany_4@email.com",
        },
    ]


def test_repository_list_without_parameters(clients_dicts):
    """Test client list without parameter use case

    Args:
        clients_dicts (_type_): _description_
    """
    repo = MemRepo(clients_dicts)

    clients = [Client.from_dict(c) for c in clients_dicts]

    assert repo.list() == clients
