import pytest


@pytest.fixture(scope="function")
def pricing():
    return [
        {"provider": "LP", "size": "S", "price": 1.50},
        {"provider": "LP", "size": "M", "price": 4.90},
        {"provider": "LP", "size": "L", "price": 6.90},
        {"provider": "MR", "size": "S", "price": 2},
        {"provider": "MR", "size": "M", "price": 3},
        {"provider": "MR", "size": "L", "price": 4},
    ]
