"""Module for the application routes"""
import json
import os

from flask import Response, jsonify, request
from pydantic import ValidationError

from application.rest.schema.category import CategorySchema, UpdateCategorySchema
from src.repository.postgres.postgresrepo_category import PostgresRepoCategory
from src.requests.category_create import build_create_category_request
from src.requests.category_list import build_category_list_request
from src.requests.category_update import build_update_category_request
from src.responses import STATUS_CODE
from src.serializers.category import CategoryJsonEncoder
from src.use_cases.category_create import category_create_use_case
from src.use_cases.category_list import category_list_use_case
from src.use_cases.category_update import category_update_use_case

from .adapters.request_adapter import request_adapter, HttpRequest

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


def category_create():
    http_request: HttpRequest = request_adapter(request)
    try:
        category = CategorySchema.parse_raw(http_request.data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    request_obj = build_create_category_request(category.dict())

    repo = PostgresRepoCategory(postgres_configuration)
    response = category_create_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=CategoryJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


def category_list():
    http_request: HttpRequest = request_adapter(request)
    qrystr_params = {
        "filters": {},
    }

    for arg, values in http_request.query_params.items():
        if arg.startswith("filter_"):
            qrystr_params["filters"][arg.replace("filter_", "")] = values

    request_obj = build_category_list_request(filters=qrystr_params["filters"])

    repo = PostgresRepoCategory(postgres_configuration)
    response = category_list_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=CategoryJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )


def category_update():
    http_request: HttpRequest = request_adapter(request)
    try:
        category = UpdateCategorySchema.parse_raw(http_request.data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    request_obj = build_update_category_request(category.dict(exclude_unset=True))

    repo = PostgresRepoCategory(postgres_configuration)
    response = category_update_use_case(repo, request_obj)

    return Response(
        json.dumps(response.value, cls=CategoryJsonEncoder),
        mimetype="application/json",
        status=STATUS_CODE[response.type],
    )
