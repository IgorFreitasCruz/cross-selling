"""Module for the Postgres database"""
from datetime import datetime
from typing import List, Optional

from sqlmodel import Column, Field, SQLModel, String


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    razao_social: str
    cnpj: str
    email: str
    dt_inclusao: str = None
    dt_alteracao: str = None
    ativo: bool = True


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    descricao: str
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    dt_alteracao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    ativo: bool = True

    client_id: Optional[int] = Field(default=None, foreign_key="client.id")


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    nome: str
    descricao: str
    sku: str
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    dt_alteracao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    ativo: bool = True

    categoria_id: Optional[int] = Field(default=None, foreign_key="category.id")


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    quantidade: Optional[int] = None
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    dt_alteracao: datetime = Field(default_factory=datetime.utcnow, nullable=True)
    ativo: bool = True

    client_id: int = Field(default=None, foreign_key="client.id")
    produto_id: int = Field(default=None, foreign_key="product.id")
