"""Test module for catagory postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_category import PostgresRepoCategory

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(app_configuration, pg_session):
    repo = PostgresRepoCategory(app_configuration)

    repo_clients = repo.list_category()

    assert len(repo_clients) == 4


def test_repository_list_with_ativo_true_filter(
    app_configuration, pg_session, pg_category_test_data
):
    repo = PostgresRepoCategory(app_configuration)

    repo_clients = repo.list_category(filters={"ativo__eq": True})

    assert len(repo_clients) == 2
    assert [c.to_dict()["descricao"] for c in repo_clients] == [
        c["descricao"] for c in pg_category_test_data if c["ativo"] is True
    ]


def test_repository_list_with_id_equal_filter(app_configuration):
    repo = PostgresRepoCategory(app_configuration)

    repo_categories = repo.list_category(filters={"id__eq": 25})

    assert len(repo_categories) == 1


def test_repository_create_client_from_dictionary(app_configuration, pg_session):
    repo = PostgresRepoCategory(app_configuration)

    category_dict = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }

    repo.create_category(category_dict)

    all_categories = repo.list_category()

    assert len(all_categories) == 5

@pytest.mark.skip("olhar depois")
def test_repository_update_category(app_configuration):
    repo = PostgresRepoCategory(app_configuration)

    new_category_data = {
        "descricao": "Categoria A",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
    }
    repo.update_category(31, new_category_data)

    updated_client = repo.list_category(filters={"id__eq":31})

    assert updated_client[0].ativo is True
