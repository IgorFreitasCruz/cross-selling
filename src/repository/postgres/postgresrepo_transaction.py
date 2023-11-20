from typing import Dict

from sqlmodel import select

from src.domain import transaction
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import Transaction as PgTransaction


class PostgresRepoTransaction(BasePostgresRepo):
    """Postgres Transaction repository"""
