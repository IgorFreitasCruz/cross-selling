"""Module for Postgres repository"""
# pylint: disable=c0103
# pylint: disable=c0209
# pylint: disable=c0116
from typing import Dict

from sqlmodel import Session, SQLModel, create_engine, select

from src.domain import client
from src.repository.postgres_objects import Client as PgClient


class PostgresRepo:
    """Postgres repository"""

    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        SQLModel.metadata.create_all(self.engine)
        SQLModel.metadata.bind = self.engine

    def _create_client_objects(self, results):
        return [
            client.Client(
                code=q.code,
                razao_social=q.razao_social,
                cnpj=q.cnpj,
                email=q.email,
                ativo=q.ativo,
            )
            for q in results
        ]

    def list(self, filters=None):
        DBSession = Session(bind=self.engine)
        session = DBSession

        query = session.query(PgClient)

        if filters is None:
            return self._create_client_objects(query.all())

        if "code__eq" in filters:
            query = query.filter(PgClient.code == filters["code__eq"])

        if "ativo__eq" in filters:
            query = query.filter(PgClient.ativo == filters["ativo__eq"])

        return self._create_client_objects(query.all())

    def create_client(self, new_client: Dict):
        DBSession = Session(bind=self.engine)
        session = DBSession

        pg_client_obj = PgClient(
            code=new_client["code"],
            razao_social=new_client["razao_social"],
            cnpj=new_client["cnpj"],
            email=new_client["email"],
            ativo=new_client["ativo"],
        )

        session.add(pg_client_obj)
        session.commit()

    def update_client(self, data: Dict):
        DBSession = Session(bind=self.engine)
        session = DBSession
        statement = select(PgClient).where(PgClient.code == data["code"])
        client_obj = session.exec(statement).one()

        for field, value in data.items():
            setattr(client_obj, field, value)

        session.commit()
