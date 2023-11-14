"""Test module for client list use case"""
# pylint: disable=w0621
import pytest

from src.domain.client import Client
from src.repository.memrepo import MemRepo


@pytest.fixture
def clients_dicts():
    """Clients Mock"""
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 1",
            "cnpj": "00.000.000/0000-01",
            "email": "mycompany_1@email.com",
            "ativo": True,
        },
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "razao_social": "My company 2",
            "cnpj": "00.000.000/0000-02",
            "email": "mycompany_2@email.com",
            "ativo": True,
        },
        {
            "code": "913694c6-435a-4366-ba0d-da5334a611b2",
            "razao_social": "My company 3",
            "cnpj": "00.000.000/0000-03",
            "email": "mycompany_3@email.com",
            "ativo": False,
        },
        {
            "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "razao_social": "My company 4",
            "cnpj": "00.000.000/0000-04",
            "email": "mycompany_4@email.com",
            "ativo": False,
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


def test_repository_list_with_code_equal_filter(clients_dicts):
    repo = MemRepo(clients_dicts)

    clients = repo.list({"code__eq": "f853578c-fc0f-4e65-81b8-566c5dffa35a"})

    assert len(clients) == 1
    assert clients[0].code == "f853578c-fc0f-4e65-81b8-566c5dffa35a"


def test_repository_list_with_ativo_equal_true_filter(clients_dicts):
    repo = MemRepo(clients_dicts)

    clients = repo.list({"ativo__eq": True})

    assert len(clients) == 2
    assert set([c.code for c in clients]) == {
        "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
    }


def test_repository_list_with_ativo_equal_false_filter(clients_dicts):
    repo = MemRepo(clients_dicts)

    clients = repo.list({"ativo__eq": False})

    assert len(clients) == 2
    assert set([c.code for c in clients]) == {
        "913694c6-435a-4366-ba0d-da5334a611b2",
        "eed76e77-55c1-41ce-985d-ca49bf6c0585",
    }