"""Test module for product postgres repository"""
# pylint: disable=c0116
# pylint: disable=w0613
import pytest

from src.repository.postgres.postgresrepo_product import PostgresRepoProduct

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_product_repository_create_from_dictionary(app_configuration, pg_session):
    repo = PostgresRepoProduct(app_configuration)

    product_dict = {
        "nome": "My product",
        "descricao": "My description",
        "sku": "0123456789",
        "categoria_id": 1,
    }

    product = repo.create_product(product_dict)

    assert product.id == 5


def test_repository_list_product_without_parameters(app_configuration, pg_session):
    repo = PostgresRepoProduct(app_configuration)

    products = repo.list_product()

    assert len(products) > 0


def test_repository_update_product(app_configuration, pg_session):
    repo = PostgresRepoProduct(app_configuration)

    product_data_to_update = {"id": 1, "ativo": False}

    product = repo.update_product(product_data_to_update)

    assert product.ativo is False
