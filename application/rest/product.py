import json

from flask import Blueprint, Response, jsonify, request
from pydantic import ValidationError

from src.repository.in_memory.memrepo_product import MemRepoProduct
from src.requests.product_create import build_create_product_request
from src.responses import STATUS_CODE
from src.serializers.category import CategoryJsonEncoder
from src.use_cases.product_create import product_create_use_case

from .schema.product import ProductSchema

blueprint = Blueprint("categories", __name__)

products = [
    {
        "nome": "My product A",
        "descricao": "My description A",
        "sku": "0123456789",
        "categoria_id": 1,
    },
    {
        "nome": "My product B",
        "descricao": "My description B",
        "sku": "0123456789",
        "categoria_id": 1,
    },
    {
        "nome": "My product C",
        "descricao": "My description C",
        "sku": "0123456789",
        "categoria_id": 1,
    },
    {
        "nome": "My product D",
        "descricao": "My description D",
        "sku": "0123456789",
        "categoria_id": 1,
    },
]


@blueprint.route("/products", methods=["POST"])
def product_create():
    try:
        category = ProductSchema.parse_raw(request.data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    request_obj = build_create_product_request(category.dict())

    # repo = PostgresRepoCategory(postgres_configuration)
    repo = MemRepoProduct(products)
    response = product_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=CategoryJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
