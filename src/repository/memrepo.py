""""Module for the Client in memory repository"""
from src.domain.client import Client


class MemRepo:
    """Class for the Client in memory repository"""

    def __init__(self, data) -> None:
        self.data = data

    def list(self):
        """List all clients

        Returns:
            List: List of client objectcs
        """
        return [Client.from_dict(c) for c in self.data]
