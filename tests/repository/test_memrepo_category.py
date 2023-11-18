"""Test module for client list use case"""
# pylint: disable=w0621
# pylint: disable=c0116
import pytest

from src.domain.category import Category
from src.repository.in_memory.memrepo_category import MemRepoCategory


@pytest.fixture
def category_dicts():
    return [
        {
            "descricao": "categoria A",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": True,
            "client_id": [1],
        },
        {
            "descricao": "categoria B",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": True,
            "client_id": [1],
        },
        {
            "descricao": "categoria C",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": False,
            "client_id": [2],
        },
        {
            "descricao": "categoria D",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": False,
            "client_id": [2],
        },
    ]


def test_repository_create_category(category_dicts):
    repo = MemRepoCategory(category_dicts)

    new_category = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }

    repo.create_category(new_category)

    assert len(category_dicts) == 5


def test_repository_list_category_without_params(category_dicts):
    repo = MemRepoCategory(category_dicts)

    result = [Category.from_dict(c) for c in category_dicts]

    assert repo.list_category() == result


# def test_repository_list_with_code_equal_filter(clients_dicts):
#     repo = MemRepo(clients_dicts)

#     clients = repo.list({"code__eq": "f853578c-fc0f-4e65-81b8-566c5dffa35a"})

#     assert len(clients) == 1
#     assert clients[0].code == "f853578c-fc0f-4e65-81b8-566c5dffa35a"


# def test_repository_list_with_ativo_equal_true_filter(clients_dicts):
#     repo = MemRepo(clients_dicts)

#     clients = repo.list({"ativo__eq": "true"})

#     assert len(clients) == 2
#     assert set([c.code for c in clients]) == {
#         "f853578c-fc0f-4e65-81b8-566c5dffa35a",
#         "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
#     }


# def test_repository_list_with_ativo_equal_false_filter(clients_dicts):
#     repo = MemRepo(clients_dicts)

#     clients = repo.list({"ativo__eq": False})

#     assert len(clients) == 2
#     assert set([c.code for c in clients]) == {
#         "913694c6-435a-4366-ba0d-da5334a611b2",
#         "eed76e77-55c1-41ce-985d-ca49bf6c0585",
#     }


# def test_repository_get_client_by_code(clients_dicts):
#     repo = MemRepo(clients_dicts)
#     client = repo.get_client_by_code("fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a")

#     assert client["code"] == "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a"


# def test_repository_update_client(clients_dicts):
#     repo = MemRepo(clients_dicts)

#     new_client_data = {
#         "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
#         "razao_social": "My company 4",
#         "cnpj": "00.000.000/0000-04",
#         "email": "mycompany_4@email.com",
#         "ativo": True,
#     }

#     repo.update_client(new_client_data)

#     updated_client = {}
#     for client in clients_dicts:
#         if client["code"] == "eed76e77-55c1-41ce-985d-ca49bf6c0585":
#             updated_client = client

#     assert len(clients_dicts) == 4
#     assert updated_client["ativo"] is True
