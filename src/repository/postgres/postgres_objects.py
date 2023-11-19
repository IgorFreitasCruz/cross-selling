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
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow)
    dt_alteracao: datetime = None
    ativo: bool = True

    categorias: List["Category"] = Relationship(back_populates="client")


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    descricao: str
    dt_inclusao: str
    dt_alteracao: str = None
    dt_inclusao: datetime = Field(default_factory=datetime.utcnow)
    dt_alteracao: datetime = None
    ativo: bool = True

    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    client: Optional[Client] = Relationship(back_populates="categorias")
