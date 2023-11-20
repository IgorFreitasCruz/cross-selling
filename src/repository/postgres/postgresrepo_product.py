from typing import Dict

from sqlmodel import select

from src.domain import product
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import Product as PgProduct


class PostgresRepoProduct(BasePostgresRepo):
    """Postgres Product repository"""

    def _create_product_objects(self, result):
        return [
            product.Product(
                id=p.id,
                code=p.code,
                nome=p.nome,
                descricao=p.descricao,
                sku=p.sku,
                categoria_id=p.categoria_id,
                dt_inclusao=p.dt_inclusao,
                dt_alteracao=p.dt_alteracao,
                ativo=p.ativo,
            )
            for p in result
        ]

    def create_product(self, product: Dict):
        session = self._create_session()

        pg_product_obj = PgProduct(**product)

        session.add(pg_product_obj)
        session.commit()
        session.refresh(pg_product_obj)

        return pg_product_obj

    def list_product(self, filters=None):
        session = self._create_session()

        query = session.query(PgProduct)

        if filters is not None:
            if "id__eq" in filters:
                query = query.filter(PgProduct.id == filters["id__eq"])

            if "code__eq" in filters:
                query = query.filter(PgProduct.code == filters["code__eq"])

            if "ativo__eq" in filters:
                query = query.filter(PgProduct.ativo == filters["ativo__eq"])

        return self._create_product_objects(query.all())

    def update_product(self, new_product_data: Dict) -> PgProduct:
        session = self._create_session()

        statement = select(PgProduct).where(PgProduct.id == new_product_data["id"])
        product_obj = session.exec(statement).one()

        for field, value in new_product_data.items():
            setattr(product_obj, field, value)

        session.commit()

        return product_obj
