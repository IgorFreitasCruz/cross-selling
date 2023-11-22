"""Module for the Client serializer"""
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
                "id": o.id,
                "code": str(o.code),
                "razao_social": o.razao_social,
                "cnpj": o.cnpj,
                "email": o.email,
                "dt_alteracao": o.dt_alteracao,
                "dt_inclusao": o.dt_inclusao,
                "ativo": o.ativo,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
