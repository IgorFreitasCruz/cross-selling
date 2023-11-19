"""Module for the application routes"""
import json

from flask import Blueprint, Response, jsonify, request
from pydantic import ValidationError

from src.repository.in_memory.memrepo_category import MemRepoCategory
from src.requests.category_create import build_create_category_request
from src.responses import STATUS_CODE
from src.serializers.client import ClientJsonEncoder
from src.use_cases.category_create import category_create_use_case

from .schema.category import CategorySchema

blueprint = Blueprint("category", __name__)

categories = [
    {
        "descricao": "categoria A",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    },
    {
        "descricao": "categoria B",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    },
    {
        "descricao": "categoria C",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": False,
        "client_id": [2],
    },
    {
        "descricao": "categoria D",
        "dt_inclusao": "18/11/2023, 14:44:12",
        "dt_alteracao": None,
        "ativo": False,
        "client_id": [2],
    },
]


@blueprint.route("/categories", methods=["POST"])
def category_create():
    try:
        category = CategorySchema.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    request_obj = build_create_category_request(category.dict())

    repo = MemRepoCategory(categories)
    response = category_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ClientJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )