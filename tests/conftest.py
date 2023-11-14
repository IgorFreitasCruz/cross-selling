"""Test module automatically loaded by pytest"""
# pylint: disable=w0621
import pytest

from application.app import create_app


@pytest.fixture
def app():
    """Factory for application

    Returns:
        Object: Application configuration
    """
    app = create_app("testing")

    return app
