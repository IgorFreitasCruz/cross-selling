"""Module for the application routes"""
import json

from flask import Blueprint, Response

from src.repository.memrepo import MemRepo
from src.serializers.client import ClientJsonEncoder
from src.use_cases.client_list import client_list_use_case

blueprint = Blueprint("client", __name__)

clients = [
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 1",
        "cnpj": "00.000.000/0000-01",
        "email": "mycompany_1@email.com",
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 2",
        "cnpj": "00.000.000/0000-02",
        "email": "mycompany_2@email.com",
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 3",
        "cnpj": "00.000.000/0000-03",
        "email": "mycompany_3@email.com",
    },
    {
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "My company 4",
        "cnpj": "00.000.000/0000-04",
        "email": "mycompany_4@email.com",
    },
]


@blueprint.route("/clients", methods=["GET"])
def repo_list():
    """List clients endpoint

    Returns:
        Response: Object containg the list of clients
    """
    repo = MemRepo(clients)
    result = client_list_use_case(repo)

    return Response(
        json.dumps(result, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=200,
    )
