"""Module for the category serializer"""
import json


class CategoryJsonEncoder(json.JSONEncoder):
    """Serializer class for the category model

    Args:
        json (object): JSONEncoder

    Returns:
        str: serialized object
    """
    def default(self, o):
        try:
            to_serialize = {
                "descricao": str(o.descricao),
                "dt_inclusao": o.dt_inclusao,
                "client_id": o.client_id,
                "dt_alteracao": o.dt_alteracao,
                "ativo": o.ativo,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
