"""Module for the Product entity"""
import dataclasses
from typing import Dict

from src.domain.base import BaseDomainModel


@dataclasses.dataclass(frozen=True)
class Product(BaseDomainModel):
    """Product entity"""

    nome: str
    descricao: str
    sku: str
    categoria_id: int

    @classmethod
    def from_dict(cls, d: Dict):
        """Initialize an object from a dictionary

        Args:
            d (Dict): dictionary containing all class attributes

        Returns:
            Model: Instance of class object
        """
        return cls(**d)

    def to_dict(self):
        """Returns a dictinary from a class object

        Returns:
            Dict: dictionary containg all class attribute data
        """
        return dataclasses.asdict(self)
