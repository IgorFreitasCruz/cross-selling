"""Test module for the client entity"""
import uuid

from src.domain.client import Client


def test_client_model_init():
    """Test client model initialization"""
    code = uuid.uuid4()
    client = Client(
        code,
        razao_social="My company",
        cnpj="00.000.000/0000-00",
        email="mycompany@email.com",
        ativo=True,
    )

    assert client.code == code
    assert client.razao_social == "My company"
    assert client.cnpj == "00.000.000/0000-00"
    assert client.email == "mycompany@email.com"
    assert client.ativo is True


def test_client_model_from_dict():
    """Test client model initialization from a dictionary"""
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "razao_social": "My company",
        "cnpj": "00.000.000/0000-00",
        "email": "mycompany@email.com",
        "ativo": True,
    }

    client = Client.from_dict(init_dict)

    assert client.code == code
    assert client.razao_social == "My company"
    assert client.cnpj == "00.000.000/0000-00"
    assert client.email == "mycompany@email.com"
    assert client.ativo is True


def test_client_model_to_dict():
    """Test client model conversion into a dictionary"""
    init_dict = {
        "code": uuid.uuid4(),
        "razao_social": "My company",
        "cnpj": "00.000.000/0000-00",
        "email": "mycompany@email.com",
        "ativo": True,
    }

    client = Client.from_dict(init_dict)

    assert client.to_dict() == init_dict


def test_client_model_comparison():
    """Test client model comparison"""
    init_dict = {
        "code": uuid.uuid4(),
        "razao_social": "My company",
        "cnpj": "00.000.000/0000-00",
        "email": "mycompany@email.com",
        "ativo": True,
    }

    client1 = Client.from_dict(init_dict)
    client2 = Client.from_dict(init_dict)

    assert client1 == client2
