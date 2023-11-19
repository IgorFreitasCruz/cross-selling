"""Module for the application routes"""
import json
import os

from flask import Blueprint, Response, jsonify, request
from pydantic import ValidationError

from src.repository.in_memory.memrepo_client import MemRepo

from src.repository.postgres.postgresrepo_client import PostgresRepoClient
from src.requests.client_create import build_create_client_request
from src.requests.client_list import build_client_list_request
from src.requests.client_update import build_update_client_request
from src.responses import STATUS_CODE
from src.serializers.client import ClientJsonEncoder
from src.use_cases.client_create import client_create_use_case
from src.use_cases.client_list import client_list_use_case
from src.use_cases.client_update import client_update_use_case

from .schema.client import ClientSchema

blueprint = Blueprint("client", __name__)


clients = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 1",
        "cnpj": "00.000.000/0000-01",
        "email": "mycompany_1@email.com",
        "ativo": True,
    },
    {
        "code": "c16c5d6e-ef36-40ee-9bf0-b290e4f93898",
        "razao_social": "My company 2",
        "cnpj": "00.000.000/0000-02",
        "email": "mycompany_2@email.com",
        "ativo": True,
    },
    {
        "code": "a72e599c-aa5e-41b1-a1f1-ea42f7253002",
        "razao_social": "My company 3",
        "cnpj": "00.000.000/0000-03",
        "email": "mycompany_3@email.com",
        "ativo": False,
    },
    {
        "code": "0c93db92-3fb2-4370-b9d9-5c78aa7ac3c0",
        "razao_social": "My company 4",
        "cnpj": "00.000.000/0000-04",
        "email": "mycompany_4@email.com",
        "ativo": False,
    },
]

postgres_configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}


@blueprint.route("/clients", methods=["POST"])
def repo_create():
    try:
        client = ClientSchema.parse_raw(request.data)  # Pydantic
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    request_obj = build_create_client_request(client.dict())

    repo = PostgresRepoClient(postgres_configuration)
    # repo = MemRepo(clients)
    response = client_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


@blueprint.route("/clients", methods=["GET"])
def repo_list():
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_client_list_request(filters=qrystr_params["filters"])

    repo = PostgresRepoClient(postgres_configuration)
    # repo = MemRepo(clients)
    response = client_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


@blueprint.route("/clients", methods=["PUT"])
def repo_update():
    try:
        client = ClientSchema.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    request_obj = build_update_client_request(client.dict())

    repo = PostgresRepoClient(postgres_configuration)
    # repo = MemRepo(clients)
    response = client_update_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
