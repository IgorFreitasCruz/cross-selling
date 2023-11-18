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

from src.repository.postgres_objects import Client


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
def pg_test_data():
    return [
        {
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "razao_social": "My company 1",
            "cnpj": "00.000.000/0000-01",
            "email": "mycompany_1@email.com",
            "ativo": True,
        },
        {
            "code": "fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a",
            "razao_social": "My company 2",
            "cnpj": "00.000.000/0000-02",
            "email": "mycompany_2@email.com",
            "ativo": True,
        },
        {
            "code": "913694c6-435a-4366-ba0d-da5334a611b2",
            "razao_social": "My company 3",
            "cnpj": "00.000.000/0000-03",
            "email": "mycompany_3@email.com",
            "ativo": False,
        },
        {
            "code": "eed76e77-55c1-41ce-985d-ca49bf6c0585",
            "razao_social": "My company 4",
            "cnpj": "00.000.000/0000-04",
            "email": "mycompany_4@email.com",
            "ativo": False,
        },
    ]


@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    """Fills the database with Postgress objects created with the test data for
    every test that is run. These are not entities, but Postgress objects we
    create to map them.
    """
    for c in pg_test_data:
        new_client = Client(
            code=c["code"],
            razao_social=c["razao_social"],
            cnpj=c["cnpj"],
            email=c["email"],
            ativo=c["ativo"],
        )
        pg_session_empty.add(new_client)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(Client).delete()
