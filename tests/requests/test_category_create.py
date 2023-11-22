import uuid
from datetime import datetime

from src.requests.category_create import build_create_category_request


def test_build_category_create_request():
    category = {
        "descricao": "description text",
        "client_id": 1,
    }
    request = build_create_category_request(category)

    assert bool(request) is True
    assert "code" in request.data
    assert "dt_inclusao" in request.data
    assert isinstance(category["code"], uuid.UUID)
    assert isinstance(category["dt_inclusao"], datetime)
