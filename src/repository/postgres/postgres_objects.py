"""Module for the Postgres database"""
from datetime import datetime
from typing import List, Optional

from sqlmodel import Column, Field, Relationship, SQLModel, String


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
    descricao: str
    dt_inclusao: str = None
    dt_alteracao: str = None
    ativo: bool = True

    client_id: Optional[int] = Field(default=None, foreign_key="client.id")


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    sku: str
    dt_inclusao: str = None
    dt_alteracao: str = None
    ativo: bool = True

    categoria_id: Optional[int] = Field(default=None, foreign_key="category.id")
