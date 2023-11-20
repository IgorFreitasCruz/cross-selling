from typing import Dict

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
