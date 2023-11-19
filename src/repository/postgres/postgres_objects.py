"""Module for the Postgres database"""
from typing import List, Optional

from sqlmodel import Column, Field, Relationship, SQLModel, String


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    razao_social: str
    cnpj: str
    email: str
    ativo: bool = True
    # categorias: List["Category"] = Relationship(back_populates="client")
    # FIXME work on this relationship later


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descricao: str
    dt_inclusao: str
    dt_alteracao: str = None
    ativo: bool = True
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")