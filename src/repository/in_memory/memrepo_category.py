""""Module for the Category in memory repository"""
from typing import Dict, List

from src.domain.category import Category


class MemRepoCategory:
    """Class for the Client in memory repository"""

    def __init__(self, data: List[Dict]) -> None:
        self.data = data

    def list_category(self, filters=None) -> List:
        """List all categories

        Returns:
            List: List of category objectcs
        """
        result = [Category.from_dict(c) for c in self.data]

        if filters is None:
            return result

        if "code__eq" in filters:
            result = [c for c in result if c.code == filters["code__eq"]]

        if "ativo__eq" in filters:
            result = [c for c in result if c.ativo is (filters["ativo__eq"] == "true")]

        return result

    def create_category(self, category: Category) -> None:
        """Creates a client

        Args:
            client (Client): Client object
        """
        self.data.append(category)

        return category

    def update_client(self, new_category_data: Dict) -> Dict:
        """Updates client information

        Args:
            client (Client): Client object

        Returns:
            Client: Updated client object
        """
        for client in self.data:
            if client["code"] == new_category_data["code"]:
                client.update(new_category_data)

                return client
