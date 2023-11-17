from unittest import mock

import pytest

from src.requests.client_create import build_create_client_request
from src.responses import ResponseTypes
from src.use_cases.client_create import client_create_use_case


def test_create_client_success():
    repo = mock.Mock()

    new_client = {
        "razao_social": "New Company",
        "cnpj": "11.111.111/1111-11",
        "email": "new_company@email.com",
        "ativo": True,
    }

    repo.create.return_value = new_client

    request = build_create_client_request(new_client)

    response = client_create_use_case(repo, request)

    assert bool(response) is True
    repo.create.assert_called_with(client=new_client)
    assert response.value == new_client


def test_create_client_handles_generic_error():
    repo = mock.Mock()
    repo.create.side_effect = Exception("Just an error message")

    new_client = {
        "razao_social": "New Company",
        "cnpj": "11.111.111/1111-11",
        "email": "new_company@email.com",
        "ativo": True,
    }

    request = build_create_client_request(client=new_client)

    response = client_create_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_create_client_handles_cnjp_validation_error():
    repo = mock.Mock()

    invalid_client_data = {
        "razao_social": "New Company",
        "cnpj": "invalid_cnpj_format",
        "email": "new_company@email.com",
        "ativo": True,
    }

    request = build_create_client_request(invalid_client_data)
    response = client_create_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "value: Invalid CNPJ",
    }


def test_create_client_handles_email_validation_error():
    repo = mock.Mock()

    invalid_client_data = {
        "razao_social": "New Company",
        "cnpj": "11.111.111/1111-11",
        "email": "invalid_email_format",
        "ativo": True,
    }

    request = build_create_client_request(invalid_client_data)
    response = client_create_use_case(repo, request)

    assert bool(response) is False
    assert response.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "value: Invalid e-mail",
    }
