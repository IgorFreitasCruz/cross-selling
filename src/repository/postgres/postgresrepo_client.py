"""Module for Postgres repository"""
# pylint: disable=c0103
# pylint: disable=c0209
# pylint: disable=c0116
from typing import Dict

from sqlmodel import select

from src.domain import client
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import Client as PgClient


class PostgresRepoClient(BasePostgresRepo):
    """Postgres Client repository"""

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
        session = self._create_session()

        query = session.query(PgClient)

        if filters is None:
            return self._create_client_objects(query.all())

        if "code__eq" in filters:
            query = query.filter(PgClient.code == filters["code__eq"])

        if "ativo__eq" in filters:
            query = query.filter(PgClient.ativo == filters["ativo__eq"])

        return self._create_client_objects(query.all())

    def create_client(self, new_client: Dict) -> PgClient.id:
        session = self._create_session()

        pg_client_obj = PgClient(
            razao_social=new_client["razao_social"],
            cnpj=new_client["cnpj"],
            email=new_client["email"],
        )

        session.add(pg_client_obj)
        session.commit()
        session.refresh(pg_client_obj)

        return pg_client_obj

    def update_client(self, data: Dict):
        session = self._create_session()

        statement = select(PgClient).where(PgClient.id == data["id"])
        client_obj = session.exec(statement).one()

        for field, value in data.items():
            setattr(client_obj, field, value)

        session.commit()

        return client_obj
