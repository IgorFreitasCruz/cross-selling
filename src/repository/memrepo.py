""""Module for the Client in memory repository"""
import uuid
from typing import List

from src.domain.client import Client


class MemRepo:
    """Class for the Client in memory repository"""

    def __init__(self, data) -> None:
        self.data = data

    def list(self, filters=None) -> List:
        """List all clients

        Returns:
            List: List of client objectcs
        """
        result = [Client.from_dict(c) for c in self.data]

        if filters is None:
            return result

        if "code__eq" in filters:
            result = [c for c in result if c.code == filters["code__eq"]]

        if "ativo__eq" in filters:

            result = [c for c in result if c.ativo is (filters["ativo__eq"] == 'true')]

        return result

    def create(self, client: Client) -> None:
        """Creates a client

        Args:
            client (Client): Client object
        """
        client.update({"code": str(uuid.uuid4())})
        self.data.append(client)

        return client
