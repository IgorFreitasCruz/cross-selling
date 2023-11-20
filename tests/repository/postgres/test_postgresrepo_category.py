"""Test module for catagory postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_category import PostgresRepoCategory

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_repository_list_category_without_parameters(app_configuration, pg_session):
    repo = PostgresRepoCategory(app_configuration)

    repo_clients = repo.list_category()

    assert len(repo_clients) == 4


def test_repository_list_category_with_ativo_true_filter(
    app_configuration, pg_session, pg_category_test_data
):
    repo = PostgresRepoCategory(app_configuration)

    repo_clients = repo.list_category(filters={"ativo__eq": True})

    assert len(repo_clients) == 2


def test_repository_list_category_with_id_equal_filter(app_configuration):
    repo = PostgresRepoCategory(app_configuration)

    repo_categories = repo.list_category(filters={"id__eq": 1})

    assert len(repo_categories) == 1


def test_repository_create_category_from_dictionary(app_configuration, pg_session):
    repo = PostgresRepoCategory(app_configuration)

    category_dict = {
        "descricao": "description text",
        "client_id": 1,
    }

    repo.create_category(category_dict)

    all_categories = repo.list_category()

    assert len(all_categories) == 5


def test_repository_update_category(app_configuration):
    repo = PostgresRepoCategory(app_configuration)

    category_data_to_update = {
        "id": 2,
        "descricao": "Categoria B",
        "dt_inclusao": "01/01/2023, 00:00:00",
        "dt_alteracao": "01/01/2023, 00:00:00",
        "ativo": False,
    }
    repo.update_category(category_data_to_update)

    updated_client = repo.list_category(filters={"id__eq": 2})

    assert updated_client[0].dt_inclusao == "01/01/2023, 00:00:00"
    assert updated_client[0].dt_alteracao == "01/01/2023, 00:00:00"
    assert updated_client[0].ativo is False
