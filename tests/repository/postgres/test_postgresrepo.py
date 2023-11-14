"""Test module for postgres database"""
import pytest

from src.repository.postgres_objects import Client

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_dummy(pg_session):
    assert len(pg_session.query(Client).all()) == 4
