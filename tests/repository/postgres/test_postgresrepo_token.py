from datetime import datetime

import pytest
from sqlalchemy.exc import IntegrityError

from src.domain.auth_jwt import AuthJwt, TokenTypeEnum
from src.repository.postgres.postgresrepo_token import PostgresRepoToken

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_token_repository_create_from_dictionary(app_configuration, pg_session):
    repo = PostgresRepoToken(app_configuration)

    token_dict = {
        "jti": "a;dfsjklhgvna;dfjkbalkdfjbvakdfnvaoakl;dfsjnvanvdf;kl",
        "client_id": 3,
        "token_type": TokenTypeEnum.REFRESH.value,
        "revoked": False,
        "expires": datetime.now(),
    }

    token = repo.create_token(token_dict)

    assert token.id == 1
    assert token.client_id == 3
    assert token.revoked is False
    assert isinstance(token, AuthJwt)
    assert isinstance(token.jti, str)
    assert isinstance(token.expires, datetime)


def test_token_repository_create_error(app_configuration, pg_session):
    repo = PostgresRepoToken(app_configuration)

    token_dict = {}

    with pytest.raises(IntegrityError):
        repo.create_token(token_dict)
