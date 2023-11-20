"""Configuratin module for integration testing for Postgres
The fixtures contains code that is specific to Postgres, so it is better to 
keep the code separated in a more specific file conftest.py
"""
# pylint: disable=w0621
# pylint: disable=c0116
# pylint: disable=c0103
# pylint: disable=c0209
import pytest
import sqlmodel

from src.repository.postgres.postgres_objects import Client as PgClient
from src.repository.postgres.postgres_objects import Category as PgCategory
from src.repository.postgres.postgres_objects import Product as PgProduct


@pytest.fixture(scope="session")
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration["POSTGRES_USER"],
        app_configuration["POSTGRES_PASSWORD"],
        app_configuration["POSTGRES_HOSTNAME"],
        app_configuration["POSTGRES_PORT"],
        app_configuration["APPLICATION_DB"],
    )

    engine = sqlmodel.create_engine(conn_str)
    connection = engine.connect()

    sqlmodel.SQLModel.metadata.create_all(engine)
    sqlmodel.SQLModel.metadata.bind = engine

    DBSession = sqlmodel.Session(bind=engine)
    session = DBSession

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope="session")
def pg_client_test_data():
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 1",
            "cnpj": "00.000.000/0000-01",
            "email": "mycompany_1@email.com",
        },
        {
            "razao_social": "My company 2",
            "cnpj": "00.000.000/0000-02",
            "email": "mycompany_2@email.com",
        },
        {
            "razao_social": "My company 3",
            "cnpj": "00.000.000/0000-03",
            "email": "mycompany_3@email.com",
        },
        {
            "razao_social": "My company 4",
            "cnpj": "00.000.000/0000-04",
            "email": "mycompany_4@email.com",
        },
    ]


@pytest.fixture(scope="session")
def pg_category_test_data():
    return [
        {"descricao": "categoria A", "client_id": 1, "ativo": True},
        {"descricao": "categoria B", "client_id": 1, "ativo": True},
        {"descricao": "categoria C", "client_id": 2, "ativo": False},
        {"descricao": "categoria D", "client_id": 2, "ativo": False},
    ]


@pytest.fixture(scope="session")
def pg_product_test_data():
    return [
        {
            "nome": "Produto A",
            "descricao": "descricao A",
            "sku": "0123456789",
            "categoria_id": 1,
            "ativo": True,
        },
        {
            "nome": "Produto B",
            "descricao": "descricao B",
            "sku": "0123456789",
            "categoria_id": 1,
            "ativo": True,
        },
        {
            "nome": "Produto C",
            "descricao": "descricao C",
            "sku": "0123456789",
            "categoria_id": 2,
            "ativo": False,
        },
        {
            "nome": "Produto D",
            "descricao": "descricao D",
            "sku": "0123456789",
            "categoria_id": 2,
            "ativo": False,
        },
    ]


@pytest.fixture(scope="package")
def pg_session(pg_session_empty, pg_client_test_data, pg_category_test_data, pg_product_test_data):
    """Fills the database with Postgress objects created with the test data for
    every test that is run. These are not entities, but Postgress objects we
    create to map them.
    """
    for idx, client in enumerate(pg_client_test_data):

        ### CREATE CLIENTS ###
        new_client = PgClient(**client)
        pg_session_empty.add(new_client)
        pg_session_empty.commit()

        ### CREATE CATEGORIES ###
        # Assuming pg_category_test_data has the same length as pg_client_test_data
        category_data = pg_category_test_data[idx]
        # Assuming the FK relationship between client and category
        category_data.update({"client_id": new_client.id})
        new_category = PgCategory(**category_data)

        pg_session_empty.add(new_category)
        pg_session_empty.commit()

        ### CREATE PRODUCTS ###
        # Assuming the same length of category and product arrays
        product_data = pg_product_test_data[idx]
        # Assuming the FK relationship between category and product
        product_data.update({"categoria_id": new_category.id})
        new_product = PgProduct(**product_data)

        pg_session_empty.add(new_product)
        pg_session_empty.commit()

    yield pg_session_empty

    # Clean up after test
    pg_session_empty.query(PgProduct).delete()
    pg_session_empty.query(PgCategory).delete()
    pg_session_empty.query(PgClient).delete()
