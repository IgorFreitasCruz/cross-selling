"""Module for the Postgres database"""
from typing import Optional

from sqlmodel import Column, Field, SQLModel, String


class Client(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(sa_column=Column(String(36)))
    razao_social: str
    cnpj: str
    email: str
    ativo: bool = True


