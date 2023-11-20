"""Test module for transaction postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_transactions import PostgresrepoTransaction

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration

def test_transaction_repository_list_without_parameters(
    app_configuration, pg_session
):
    repo = PostgresrepoTransaction(app_configuration)

    transactions = repo.list_client()

    assert len(transactions) == 4


def test_transaction_repository_list_with_code_equal_filter(
    app_configuration, pg_session
):
    repo = PostgresrepoTransaction(app_configuration)

    transaction = repo.list_client(
        filters={"code__eq": "f853578c-fc0f-4e65-81b8-566c5dffa35a"}
    )

    assert len(transaction) == 1
    assert transaction[0].code == "f853578c-fc0f-4e65-81b8-566c5dffa35a"


def test_transaction_repository_list_with_ativo_false_filter(
    app_configuration, pg_session
):
    repo = PostgresrepoTransaction(app_configuration)

    transaction_inactive = repo.list_client(filters={"ativo__eq": False})

    assert len(transaction_inactive) == 0


