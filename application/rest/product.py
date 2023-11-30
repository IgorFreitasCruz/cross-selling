import json
import os

from flask import Response, jsonify, request
from pydantic import ValidationError

from application.rest.schema.product import ProductSchema, UpdateProductSchema
from src.repository.postgres.postgresrepo_product import PostgresRepoProduct
from src.requests.product_create import build_create_product_request
from src.requests.product_list import build_product_list_request
from src.requests.product_update import build_update_product_request
from src.responses import STATUS_CODE
from src.serializers.product import ProductJsonEncoder
from src.use_cases.product_create import product_create_use_case
from src.use_cases.product_list import product_list_use_case
from src.use_cases.product_update import product_update_use_case

from .adapters.request_adapter import HttpRequest, request_adapter

try:
    postgres_configuration = {
        'POSTGRES_USER': os.environ['POSTGRES_USER'],
        'POSTGRES_PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'POSTGRES_HOSTNAME': os.environ['POSTGRES_HOSTNAME'],
        'POSTGRES_PORT': os.environ['POSTGRES_PORT'],
        'APPLICATION_DB': os.environ['APPLICATION_DB'],
    }
except Exception:
    ...


def product_create():
    http_request: HttpRequest = request_adapter(request)
    try:
        product = ProductSchema.parse_raw(http_request.data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

    request_obj = build_create_product_request(product.dict())

    repo = PostgresRepoProduct(postgres_configuration)
    response = product_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ProductJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODE[response.type],
    )


def product_list():
    http_request: HttpRequest = request_adapter(request)
    qrystr_params = {
        'filters': {},
    }

    for arg, values in http_request.query_params.items():
        if arg.startswith('filter_'):
            qrystr_params['filters'][arg.replace('filter_', '')] = values

    request_obj = build_product_list_request(qrystr_params['filters'])

    repo = PostgresRepoProduct(postgres_configuration)
    response = product_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ProductJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODE[response.type],
    )


def product_update():
    http_request: HttpRequest = request_adapter(request)
    try:
        product = UpdateProductSchema.parse_raw(http_request.data)
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

    request_obj = build_update_product_request(
        product.dict(exclude_unset=True)
    )

    repo = PostgresRepoProduct(postgres_configuration)
    response = product_update_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=ProductJsonEncoder),
        mimetype='application/json',
        status=STATUS_CODE[response.type],
    )
