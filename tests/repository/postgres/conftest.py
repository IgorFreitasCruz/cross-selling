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
        {
            "descricao": "categoria A",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": True,
            "client_id": [1],
        },
        {
            "descricao": "categoria B",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": True,
            "client_id": [1],
        },
        {
            "descricao": "categoria C",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": False,
            "client_id": [2],
        },
        {
            "descricao": "categoria D",
            "dt_inclusao": "18/11/2023, 14:44:12",
            "dt_alteracao": None,
            "ativo": False,
            "client_id": [2],
        },
    ]


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_client_test_data, pg_category_test_data):
    """Fills the database with Postgress objects created with the test data for
    every test that is run. These are not entities, but Postgress objects we
    create to map them.
    """
    for idx, client in enumerate(pg_client_test_data):
        new_client = PgClient(**client)

        # Creates new client
        pg_session_empty.add(new_client)
        pg_session_empty.commit()

        # Assuming the same length of client and category arrays
        category_data = pg_category_test_data[idx]
        # Assuming category_data_list has the same length as pg_test_data
        category_data.update({"client_id": new_client.id})
        new_category = PgCategory(**category_data)

        pg_session_empty.add(new_category)
        pg_session_empty.commit()

    yield pg_session_empty

    # Clean up after test
    pg_session_empty.query(PgCategory).delete()
    pg_session_empty.query(PgClient).delete()
