"""Module for the client serializer"""
import json


class ClientJsonEncoder(json.JSONEncoder):
    """Serializer class for the client model

    Args:
        json (object): JSONEncoder

    Returns:
        str: serialized object
    """
    def default(self, o):
        try:
            to_serialize = {
                "id": 1,
                "code": str(o.code),
                "razao_social": o.razao_social,
                "cnpj": o.cnpj,
                "email": o.email,
                "dt_alteracao": None,
                "dt_inclusao": "18/11/2023 14:44:12",
                "ativo": o.ativo,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
