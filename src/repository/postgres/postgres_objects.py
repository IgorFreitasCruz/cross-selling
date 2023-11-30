"""Module for the Postgres database"""
import uuid
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=True)
    razao_social: str
    cnpj: str
    email: str
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    dt_alteracao: datetime = None
    ativo: bool = True


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=True)
    descricao: str
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    dt_alteracao: datetime = None
    ativo: bool = True

    client_id: Optional[int] = Field(foreign_key="client.id")


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=True)
    nome: str
    descricao: str
    sku: str
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    dt_alteracao: datetime = None
    ativo: bool = True

    categoria_id: Optional[int] = Field(foreign_key="category.id")


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: uuid.UUID = Field(default_factory=uuid.uuid4, nullable=True)
    quantidade: Optional[int]
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    dt_alteracao: datetime = None
    ativo: bool = True

    client_id: int = Field(foreign_key="client.id")
    produto_id: int = Field(foreign_key="product.id")


class AuthJwt(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    jti: str
    token_type: str
    revoked: bool = False
    expires: datetime

    client_id: int = Field(foreign_key="client.id")
