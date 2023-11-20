import json

import pytest
from flask import Blueprint, Response, request

from src.repository.in_memory.memrepo_transaction import MemRepoTransaction
from src.requests.transaction_list import build_transaction_list_request
from src.responses import STATUS_CODE
from src.serializers.transaction import TransactionJsonEncoder
from src.use_cases.transaction_list import transaction_list_use_case

blueprint = Blueprint("transactions", __name__)

transactions = [
    {
        "id": 1,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "client_id": 1,
        "produto_id": 1,
        "quantidade": 10,
        "dt_inclusao": "01/01/2023 00:00:00",
        "dt_alteracao": None,
        "ativo": True,
    },
    {
        "id": 2,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "client_id": 1,
        "produto_id": 1,
        "quantidade": 10,
        "dt_inclusao": "01/01/2023 00:00:00",
        "dt_alteracao": None,
        "ativo": True,
    },
    {
        "id": 3,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "client_id": 1,
        "produto_id": 1,
        "quantidade": 10,
        "dt_inclusao": "01/01/2023 00:00:00",
        "dt_alteracao": None,
        "ativo": False,
    },
    {
        "id": 4,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "client_id": 1,
        "produto_id": 1,
        "quantidade": 10,
        "dt_inclusao": "01/01/2023 00:00:00",
        "dt_alteracao": None,
        "ativo": False,
    },
]


@blueprint.route("/transaction", methods=["GET"])
def product_list():
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_transaction_list_request(qrystr_params["filters"])

    # repo = PostgresRepoCategory(postgres_configuration)
    repo = MemRepoTransaction(transactions)
    response = transaction_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=TransactionJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
