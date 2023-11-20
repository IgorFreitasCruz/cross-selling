"""Test module for create client"""
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
    }

    new_client_created = {
        "id": 1,
        "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
        "razao_social": "New Company",
        "cnpj": "11.111.111/1111-11",
        "email": "new_company@email.com",
        "dt_criacao": "01/01/2023 00:00:00",
        "dt_alteracao": "01/01/2023 00:00:00",
        "ativo": True,
    }

    repo.create_client.return_value = new_client_created

    request = build_create_client_request(new_client)

    result = client_create_use_case(repo, request)

    assert bool(result) is True
    repo.create_client.assert_called_with(new_client)
    assert result.value == new_client_created


@pytest.mark.skip("olhar depois")
def test_create_client_handles_generic_error():
    repo = mock.Mock()
    repo.create_client.side_effect = Exception("Just an error message")

    new_client = {
        "razao_social": "New Company",
        "cnpj": "",
        "email": "new_company@email.com",
    }

    request = build_create_client_request(client=new_client)

    result = client_create_use_case(repo, request)

    assert bool(result) is False
    assert result.value == {
        "type": ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message",
    }


def test_create_client_handles_cnjp_validation_error():
    repo = mock.Mock()

    invalid_client_data = {
        "razao_social": "New Company",
        "cnpj": "invalid_cnpj_format",
        "email": "new_company@email.com",
    }

    request = build_create_client_request(invalid_client_data)

    result = client_create_use_case(repo, request)

    assert bool(result) is False
    assert result.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "value: Invalid CNPJ",
    }


def test_create_client_handles_email_validation_error():
    repo = mock.Mock()

    invalid_client_data = {
        "razao_social": "New Company",
        "cnpj": "11.111.111/1111-11",
        "email": "invalid_email_format",
    }

    request = build_create_client_request(invalid_client_data)

    result = client_create_use_case(repo, request)

    assert bool(result) is False
    assert result.value == {
        "type": ResponseTypes.PARAMETERS_ERROR,
        "message": "value: Invalid e-mail",
    }
