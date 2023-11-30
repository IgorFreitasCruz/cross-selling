from src.domain import auth_jwt
from src.repository.postgres.base_postgresrepo import BasePostgresRepo
from src.repository.postgres.postgres_objects import AuthJwt as PgAuthJwt


class PostgresRepoToken(BasePostgresRepo):
    """Postgres Token repository"""

    def _create_token_objects(self, t: PgAuthJwt) -> auth_jwt.AuthJwt:
        return auth_jwt.AuthJwt(
            id=t.id,
            jti=t.jti,
            client_id=t.client_id,
            token_type=t.token_type,
            revoked=t.revoked,
            expires=t.expires,
        )

    def create_token(self, new_token: dict) -> auth_jwt.AuthJwt:
        session = self._create_session()

        try:
            pg_token_obj = PgAuthJwt(**new_token)
            session.add(pg_token_obj)
        except:
            session.rollback()
            raise
        else:
            session.commit()

        return self._create_token_objects(pg_token_obj)
