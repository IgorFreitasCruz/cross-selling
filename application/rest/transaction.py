import json
import os

from flask import Response, jsonify, request
from pydantic import ValidationError

from application.rest.schema.transaction import TransactionSchema
from src.repository.postgres.postgresrepo_transaction import PostgresRepoTransaction
from src.requests.transaction_create import build_transaction_create_request
from src.requests.transaction_list import build_transaction_list_request
from src.responses import STATUS_CODE
from src.serializers.transaction import TransactionJsonEncoder
from src.use_cases.transaction_create import transaction_create_use_case
from src.use_cases.transaction_list import transaction_list_use_case

from .adapters.request_adapter import HttpRequest, request_adapter

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


def transaction_create():
    http_request: HttpRequest = request_adapter(request)
    try:
        transaction = TransactionSchema.parse_raw(http_request.data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    request_obj = build_transaction_create_request(transaction.dict())

    repo = PostgresRepoTransaction(postgres_configuration)
    response = transaction_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=TransactionJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


def transaction_list():
    http_request: HttpRequest = request_adapter(request)
    qrystr_params = {
        "filters": {},
    }

    for arg, values in http_request.query_params.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_transaction_list_request(qrystr_params["filters"])

    repo = PostgresRepoTransaction(postgres_configuration)
    response = transaction_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=TransactionJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
