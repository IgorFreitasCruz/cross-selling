"""Test module for transaction postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_transaction import PostgresRepoTransaction

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_transaction_repository_list_without_parameters(app_configuration, pg_session):
    repo = PostgresRepoTransaction(app_configuration)

    transactions = repo.list_transaction()

    assert len(transactions) == 4


def test_transaction_repository_list_with_code_equal_filter(
    app_configuration, pg_session
):
    repo = PostgresRepoTransaction(app_configuration)

    transaction = repo.list_transaction(filters={"id__eq": 1})

    assert len(transaction) == 1
    assert transaction[0].ativo is True


def test_transaction_repository_list_with_ativo_false_filter(
    app_configuration, pg_session
):
    repo = PostgresRepoTransaction(app_configuration)

    transaction_inactive = repo.list_transaction(filters={"ativo__eq": False})

    assert len(transaction_inactive) == 2


def test_transaction_repository_create_from_dictionary(app_configuration):
    repo = PostgresRepoTransaction(app_configuration)

    transaction_dict = {"client_id": 1, "produto_id": 1, "quantidade": 10}

    transaction = repo.create_transaction(transaction_dict)

    assert transaction.id == 5
    assert transaction.client_id == 1
    assert transaction.produto_id == 1
    assert transaction.quantidade == 10
