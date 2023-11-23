import json
import os

from flask import Blueprint, Response, jsonify, request
from pydantic import ValidationError

from src.repository.in_memory.memrepo_transaction import MemRepoTransaction
from application.rest.schema.transaction import TransactionSchema
from src.repository.in_memory.memrepo_transaction import MemRepoTransaction
from src.repository.postgres.postgresrepo_transaction import PostgresRepoTransaction
from src.requests.transaction_create import build_transaction_create_request
from src.requests.transaction_list import build_transaction_list_request
from src.responses import STATUS_CODE
from src.serializers.transaction import TransactionJsonEncoder
from src.use_cases.transaction_create import transaction_create_use_case
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

try:
    postgres_configuration = {
        "POSTGRES_USER": os.environ["POSTGRES_USER"],
        "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
        "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
        "APPLICATION_DB": os.environ["APPLICATION_DB"],
    }
except Exception:
    ...


@blueprint.route("/transactions", methods=["POST"])
def transaction_post():
    try:
        transaction = TransactionSchema.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    request_obj = build_transaction_create_request(transaction.dict())

    # repo = PostgresRepoTransaction(postgres_configuration)
    repo = MemRepoTransaction(transactions)
    response = transaction_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=TransactionJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


@blueprint.route("/transactions", methods=["GET"])
def transaction_list():
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_transaction_list_request(qrystr_params["filters"])

    # repo = PostgresRepoTransaction(postgres_configuration)
    repo = MemRepoTransaction(transactions)
    response = transaction_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=TransactionJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
