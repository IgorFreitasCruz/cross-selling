"""Test module for Category serializer"""
import json

from src.domain.transaction import Transaction
from src.serializers.transaction import TransactionJsonEncoder


def test_serialize_domain_transaction():
    transaction = Transaction(
        id=1,
        code='f853578c-fc0f-4e65-81b8-566c5dffa35a',
        client_id=1,
        produto_id=1,
        quantidade=10,
        dt_inclusao='01/01/2023 00:00:00',
        dt_alteracao=None,
        ativo=True,
    )

    expected_json = """
        {
            "id": 1,
            "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "client_id": 1,
            "produto_id": 1,
            "quantidade": 10,
            "dt_inclusao": "01/01/2023 00:00:00",
            "dt_alteracao": null,
            "ativo": true
        }
        """
    json_transaction = json.dumps(transaction, cls=TransactionJsonEncoder)

    assert json.loads(json_transaction) == json.loads(expected_json)
