"""Module for the application routes"""
import json

from flask import Blueprint, Response, request, jsonify
from pydantic import ValidationError

from src.repository.memrepo import MemRepo
from src.requests.client_create import build_create_client_request
from src.requests.client_list import build_client_list_request
from src.responses import ResponseTypes
from src.serializers.client import ClientJsonEncoder
from src.use_cases.client_create import client_create_use_case
from src.use_cases.client_list import client_list_use_case

from .schema.client import ClientSchema

blueprint = Blueprint("client", __name__)

STATUS_CODE = {
    ResponseTypes.SUCCESS: 200,
    ResponseTypes.RESOURCE_ERROR: 404,
    ResponseTypes.PARAMETERS_ERROR: 400,
    ResponseTypes.SYSTEM_ERROR: 500,
}

clients = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 1",
        "cnpj": "00.000.000/0000-01",
        "email": "mycompany_1@email.com",
        "ativo": True,
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 2",
        "cnpj": "00.000.000/0000-02",
        "email": "mycompany_2@email.com",
        "ativo": True,
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 3",
        "cnpj": "00.000.000/0000-03",
        "email": "mycompany_3@email.com",
        "ativo": False,
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 4",
        "cnpj": "00.000.000/0000-04",
        "email": "mycompany_4@email.com",
        "ativo": False,
    },
]


@blueprint.route("/clients", methods=["GET"])
def repo_list():
    """List clients endpoint

    Returns:
        Response: Object containg the list of clients
    """
    qrystr_params = {
        "filters": {},
    }

    for arg, values in request.args.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_client_list_request(filters=qrystr_params["filters"])

    repo = MemRepo(clients)
    response = client_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


@blueprint.route("/clients", methods=["POST"])
def repo_create():
    """Create client endpoint

    Returns:
        Response: Ok if client created
    """
    try:
        client = ClientSchema.parse_raw(request.data) # Pydantic

        request_obj = build_create_client_request(client.dict())

        repo = MemRepo(clients)
        response = client_create_use_case(repo, request_obj)

        return Response(
            json.dumps(response.value, cls=ClientJsonEncoder),
            mimetype="application/json",
            status=STATUS_CODE[response.type],
        )
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
