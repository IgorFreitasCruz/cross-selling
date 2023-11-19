"""Base class for PostgresRepo"""
from sqlmodel import Session, SQLModel, create_engine


class BasePostgresRepo:
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

    def _create_session(self):
        return Session(bind=self.engine)
