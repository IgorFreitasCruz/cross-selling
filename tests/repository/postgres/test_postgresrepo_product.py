import pytest

from src.repository.postgres.postgresrepo_product import PostgresRepoProduct

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration




def test_product_repository_create_from_dictionary(app_configuration):
    repo = PostgresRepoProduct(app_configuration)

    product_dict = {
        "nome": "My product",
        "descricao": "My description",
        "sku": "0123456789",
        "categoria_id": 1,
    }

    product = repo.create_product(product_dict)

    assert product.id == 5


def test_repository_list_product_without_parameters(app_configuration):
    repo = PostgresRepoProduct(app_configuration)

    products = repo.list_product()

    assert len(products) > 0