"""Test module for client serializer"""
import json
import uuid

from src.serializers.client import ClientJsonEncoder

from src.domain.client import Client


def test_serialize_domain_client():
    """Test client model serialization"""
    code = uuid.uuid4()
    client = Client(
        code,
        razao_social="My company",
        cnpj="00.000.000/0000-00",
        email="mycompany@email.com",
        ativo= True,
    )

    excepted_json = f"""
        {{
            "code": "{code}",
            "razao_social": "My company",
            "cnpj": "00.000.000/0000-00",
            "email": "mycompany@email.com",
            "ativo": true
        }}
        """

    json_client = json.dumps(client, cls=ClientJsonEncoder)

    assert json.loads(json_client) == json.loads(excepted_json)
