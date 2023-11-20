"""Module for the client entity"""
import dataclasses
from typing import Dict

from src.domain.base import BaseDomainModel


@dataclasses.dataclass
class Client(BaseDomainModel):
    """Client entity"""

    cnpj: str
    email: str
    razao_social: str

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
