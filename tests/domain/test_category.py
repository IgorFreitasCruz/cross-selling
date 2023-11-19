"""Test module for the category entity"""
# pylint: disable=c0116
from datetime import datetime

from src.domain.category import Category


def test_client_model_init():
    """Test client model initialization"""
    date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    client = Category(
        descricao="description text",
        dt_inclusao=date_time,
        dt_alteracao=None,
        ativo=True,
        client_id=[1],
    )

    assert client.descricao == "description text"
    assert client.dt_inclusao == date_time
    assert client.dt_alteracao is None
    assert client.ativo is True
    assert client.client_id == [1]


def test_category_model_from_dict():
    init_dict = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }

    category = Category.from_dict(init_dict)

    assert category.descricao == "description text"
    assert category.dt_inclusao == "18/11/2023 14:44:12"
    assert category.dt_alteracao is None
    assert category.ativo is True
    assert category.client_id == [1]


def test_category_model_to_dict():
    init_dict = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }

    category = Category.from_dict(init_dict)

    assert category.to_dict() == init_dict


def test_category_model_comparison():
    init_dict = {
        "descricao": "description text",
        "dt_inclusao": "18/11/2023 14:44:12",
        "dt_alteracao": None,
        "ativo": True,
        "client_id": [1],
    }

    category1 = Category.from_dict(init_dict)
    category2 = Category.from_dict(init_dict)

    assert category1 == category2
