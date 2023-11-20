"""Test module for client postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_client import PostgresRepoClient

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_client_repository_list_without_parameters(
    app_configuration, pg_session, pg_client_test_data
):
    repo = PostgresRepoClient(app_configuration)

    clients = repo.list_client()

    assert len(clients) == 4


def test_client_repository_list_with_code_equal_filter(
    app_configuration, pg_session, pg_client_test_data
):
    repo = PostgresRepoClient(app_configuration)

    repo_clients = repo.list_client(
        filters={"code__eq": "f853578c-fc0f-4e65-81b8-566c5dffa35a"}
    )

    assert len(repo_clients) == 1
    assert repo_clients[0].code == "f853578c-fc0f-4e65-81b8-566c5dffa35a"


def test_client_repository_list_with_ativo_false_filter(
    app_configuration, pg_session, pg_client_test_data
):
    repo = PostgresRepoClient(app_configuration)

    clients_inactive = repo.list_client(filters={"ativo__eq": False})

    assert len(clients_inactive) == 0


def test_client_repository_create_from_dictionary(app_configuration):
    repo = PostgresRepoClient(app_configuration)

    client_dict = {
        "razao_social": "My company 5",
        "cnpj": "00.000.000/0000-05",
        "email": "mycompany_4@email.com",
    }

    client = repo.create_client(client_dict)

    assert client.id
    assert client.ativo
    assert client.dt_inclusao is None
    assert client.dt_alteracao is None


def test_client_repository_update(app_configuration, pg_session, pg_client_test_data):
    repo = PostgresRepoClient(app_configuration)

    new_client_data = {
        "id": 1,
        "ativo": False,
    }
    repo.update_client(new_client_data)

    updated_client = repo.list_client(filters={"id__eq": 1})

    assert updated_client[0].ativo is False
