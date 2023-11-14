"""Test module for postgres database"""
import pytest

# The module attribute pytestmark labels every test in the module with the tag integration
pytestmark = pytest.mark.integration


def test_dummy():
    ...