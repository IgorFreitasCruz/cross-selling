"""Test module for postgres database"""
# pylint: disable=c0116
import pytest

from src.repository import postgresrepo

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
