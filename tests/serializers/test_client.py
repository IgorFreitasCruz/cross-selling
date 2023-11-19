"""Test module for client serializer"""
import json
import uuid

from src.serializers.client import ClientJsonEncoder

from src.domain.client import Client


def test_serialize_domain_client():
    code = uuid.uuid4()
    client = Client(
        id=1,
        code=code,
        razao_social="My company",
        cnpj="00.000.000/0000-00",
        email="mycompany@email.com",
        dt_alteracao=None,
        dt_inclusao="18/11/2023 14:44:12",
        ativo=True,
    )

    excepted_json = f"""
        {{
            "id": 1,
            "code": "{code}",
            "razao_social": "My company",
            "cnpj": "00.000.000/0000-00",
            "email": "mycompany@email.com",
            "dt_alteracao": null,
            "dt_inclusao": "18/11/2023 14:44:12",
            "ativo": true
        }}
        """

    json_client = json.dumps(client, cls=ClientJsonEncoder)

    assert json.loads(json_client) == json.loads(excepted_json)
