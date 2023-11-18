"""Test module for postgres database"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository import postgresrepo
from src.repository.postgres_objects import Client

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_clients = repo.list()

    assert set([c.code for c in repo_clients]) == set([c["code"] for c in pg_test_data])


def test_repository_list_with_code_equal_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_clients = repo.list(
        filters={"code__eq": "f853578c-fc0f-4e65-81b8-566c5dffa35a"}
    )

    assert len(repo_clients) == 1
    assert repo_clients[0].code == "f853578c-fc0f-4e65-81b8-566c5dffa35a"


def test_repository_list_with_ativo_true_filter(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_clients = repo.list(filters={"ativo__eq": True})

    assert len(repo_clients) == 2
    assert [c.to_dict() for c in repo_clients] == [
        c for c in pg_test_data if c["ativo"] is True
    ]


def test_repository_create_client_from_dictionary(
    app_configuration, pg_session, pg_test_data
):
    repo = postgresrepo.PostgresRepo(app_configuration)

    client_dict = {
        "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
        "razao_social": "My company 5",
        "cnpj": "00.000.000/0000-05",
        "email": "mycompany_4@email.com",
        "ativo": True,
    }

    repo.create_client(client_dict)

    repo_clients = repo.list()

    assert len(repo_clients) == 5


def test_repository_update_client(app_configuration, pg_session, pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    client_data = {
        "code": "cb6cd5f1-8316-46a4-9916-3db38bce065d",
        "razao_social": "My company 5",
        "cnpj": "00.000.000/0000-05",
        "email": "mycompany_4@email.com",
        "ativo": True,
    }

    repo.create_client(client_data)

    new_client_data = {
        "code": "cb6cd5f1-8316-46a4-9916-3db38bce065d",
        "razao_social": "My company 5",
        "cnpj": "00.000.000/0000-05",
        "email": "mycompany_4@email.com",
        "ativo": False,
    }
    repo.update_client(new_client_data)

    updated_client = repo.list(
        filters={"code__eq": "cb6cd5f1-8316-46a4-9916-3db38bce065d"}
    )

    assert updated_client[0].ativo is False
