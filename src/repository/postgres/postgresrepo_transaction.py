# pylint: disable=c0103
# pylint: disable=c0209
# pylint: disable=c0116
from typing import Dict, List

from sqlmodel import select

from src.domain import transaction
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import Transaction as PgTransaction


class PostgresRepoTransaction(BasePostgresRepo):
    """Postgres Transaction repository"""

    def _create_transaction_objects(self, result) -> List[transaction.Transaction]:
        return [
            transaction.Transaction(
                id=t.id,
                code=t.code,
                dt_inclusao=t.dt_inclusao,
                dt_alteracao=t.dt_alteracao,
                client_id=t.client_id,
                produto_id=t.produto_id,
                quantidade=t.quantidade,
                ativo=t.ativo,
            )
            for t in result
        ]

    def list_transaction(self, filters=None) -> List[transaction.Transaction]:
        session = self._create_session()

        query = session.query(PgTransaction)

        if filters is None:
            return self._create_transaction_objects(query.all())

        if "id__eq" in filters:
            query = query.filter(PgTransaction.id == filters["id__eq"])

        if "code__eq" in filters:
            query = query.filter(PgTransaction.code == filters["code__eq"])

        if "ativo__eq" in filters:
            query = query.filter(PgTransaction.ativo == filters["ativo__eq"])

        if "client__eq" in filters:
            query = query.filter(PgTransaction.code == filters["client__eq"])

        if "produto__eq" in filters:
            query = query.filter(PgTransaction.ativo == filters["produto__eq"])

        return self._create_transaction_objects(query.all())

    def create_transaction(self, new_transaction: Dict) -> transaction.Transaction:
        session = self._create_session()

        pg_transaction_obj = PgTransaction(**new_transaction)
        session.add(pg_transaction_obj)
        session.commit()

        return self._create_transaction_objects([pg_transaction_obj])[0]
