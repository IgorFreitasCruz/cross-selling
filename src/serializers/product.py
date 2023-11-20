"""Module for the Product serializer"""
import json


class ProductJsonEncoder(json.JSONEncoder):
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
                "code": o.code,
                "nome": o.nome,
                "descricao": o.descricao,
                "sku": o.sku,
                "categoria_id": o.categoria_id,
                "dt_inclusao": o.dt_inclusao,
                "dt_alteracao": o.dt_alteracao,
                "ativo": o.ativo,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
