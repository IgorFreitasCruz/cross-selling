"""Test module for category serializer"""
import json
from datetime import datetime
from src.serializers.category import CategoryJsonEncoder

from src.domain.category import Category


def test_serialize_domain_client():
    date_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    client = Category(
        descricao="description text",
        dt_inclusao=date_time,
        client_id=[1],
        dt_alteracao=None,
        ativo=True,
    )

    excepted_json = f"""
        {{
            "descricao": "description text",
            "dt_inclusao": "{date_time}",
            "client_id": [1],
            "dt_alteracao": null,
            "ativo": true
        }}
        """

    json_client = json.dumps(client, cls=CategoryJsonEncoder)

    assert json.loads(json_client) == json.loads(excepted_json)
