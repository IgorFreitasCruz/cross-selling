"""Module for the base class for domain models"""
# pylint: disable=c0115
from dataclasses import dataclass, field
from typing import Optional

@dataclass()
class BaseDomainModel:
    ativo: bool = field(default=True, kw_only=True)
    dt_inclusao: str = field(default=None, kw_only=True)
    dt_alteracao: str = field(default=None, kw_only=True)
