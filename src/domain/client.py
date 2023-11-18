"""Module for the client entity"""
import dataclasses
import uuid
from typing import Dict


@dataclasses.dataclass
class Client:
    """Client entity"""

    code: uuid.UUID
    razao_social: str
    cnpj: str
    email: str
    ativo: bool

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
