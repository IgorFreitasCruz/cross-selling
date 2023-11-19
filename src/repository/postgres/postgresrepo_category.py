# pylint: disable=c0116
from typing import Dict, List

from sqlmodel import select

from src.domain import category
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import Category as PgCategory


class PostgresRepoCategory(BasePostgresRepo):
    def __init__(self, configuration) -> None:
        super().__init__(configuration)

    def _create_category_objects(self, result) -> List[category.Category]:
        return [
            category.Category(
                descricao=c.descricao,
                dt_inclusao=c.dt_inclusao,
                client_id=c.client_id,
                dt_alteracao=c.dt_alteracao,
                ativo=c.ativo,
            )
            for c in result
        ]

    def list_category(self, filters=None) -> None:
        session = self._create_session()

        query = session.query(PgCategory)

        if filters is None:
            return self._create_category_objects(query.all())

        if "ativo__eq" in filters:
            query = query.filter(PgCategory.ativo == filters["ativo__eq"])

        if "id__eq" in filters:
            query = query.filter(PgCategory.id == filters["id__eq"])

        return self._create_category_objects(query.all())

    def create_category(self, new_category: Dict) -> PgCategory.id:
        session = self._create_session()

        pg_category_obj = PgCategory(**new_category)
        session.add(pg_category_obj)
        session.commit()

        return pg_category_obj.id

    def update_category(self, category_id: int, new_category_data: Dict) -> PgCategory:
        session = self._create_session()

        statement = select(PgCategory).where(PgCategory.id == category_id)
        category_obj = session.exec(statement).one()

        for field, value in new_category_data.items():
            setattr(category_obj, field, value)

        session.commit()

        return category_obj
