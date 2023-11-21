"""Module for the Transaction serializer"""
import json


class TransactionJsonEncoder(json.JSONEncoder):
    """Serializer class for the transaction model

    Args:
        json (object): JSONEncoder

    Returns:
        str: serialized object
    """
    def default(self, o):
        try:
            to_serialize = {
                "id": o.id,
                "code": o.code,
                "client_id": o.client_id,
                "produto_id": o.produto_id,
                "quantidade": o.quantidade,
                "dt_inclusao": o.dt_inclusao,
                "dt_alteracao": o.dt_alteracao,
                "ativo": o.ativo,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)