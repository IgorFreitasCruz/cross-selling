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
        """Initialize a Client object from a dictionary

        Args:
            d (Dict): dictionary containing all Client attributes

        Returns:
            Client: Instance of Client object
        """
        return cls(**d)

    def to_dict(self):
        """Returns a dictinary from a Client object

        Returns:
            Dict: dictionary containg all Client attributes data
        """
        return dataclasses.asdict(self)
