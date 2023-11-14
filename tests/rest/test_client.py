import json
from unittest import mock

import pytest

from src.domain.client import Client
from src.responses import ResponseFailure, ResponseSuccess, ResponseTypes

client_dict = {
    "code": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
    "razao_social": "My company 1",
    "cnpj": "00.000.000/0000-01",
    "email": "mycompany_1@email.com",
    "ativo": True,
}

clients = [Client.from_dict(client_dict)]


@mock.patch("application.rest.client.client_list_use_case")
def test_get(mock_use_case, client):
    """Test get for client"""
    mock_use_case.return_value = clients

    http_response = client.get("/clients")

    assert json.loads(http_response.data.decode("utf-8")) == [client_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"
