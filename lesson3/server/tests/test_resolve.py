import pytest
from datetime import datetime
from actions import resolve


@pytest.fixture
def expected_action():
    return 'echo'


@pytest.fixture
def non_expected_action():
    return ''


def test_valid_resolve(expected_action):
    controller = resolve(expected_action)
    assert controller


def test_invalid_resolve(non_expected_action):
    controller = resolve(non_expected_action)
    assert not controller
