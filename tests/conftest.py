import pytest
from modules.transaction_calc.rules.discount_limit import DiscountLimit

from modules.transaction_calc.rules.free_shipping import FreeShipping


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


@pytest.fixture(scope="function")
def pricing1():
    return [
        {"provider": "LP", "size": "S", "price": 1},
        {"provider": "LP", "size": "M", "price": 2},
        {"provider": "LP", "size": "L", "price": 3},
        {"provider": "MR", "size": "S", "price": 3},
        {"provider": "MR", "size": "M", "price": 1},
        {"provider": "MR", "size": "L", "price": 1},
    ]


@pytest.fixture(scope="function")
def default_config():
    return {
        "pricing": [
            {"provider": "LP", "size": "S", "price": 1.50},
            {"provider": "LP", "size": "M", "price": 4.90},
            {"provider": "LP", "size": "L", "price": 6.90},
            {"provider": "MR", "size": "S", "price": 2},
            {"provider": "MR", "size": "M", "price": 3},
            {"provider": "MR", "size": "L", "price": 4},
        ],
        "lowest_rule": ["S"],
        "free_shipping_rule": {
            "provider": ["LP"],
            "size": ["L"],
            "every_nth_free": 3,
            "limit_per_period": 1,
            "period_size": "MM",
            "period_interval": 1,
        },
        "discount_limit_rule": {
            "provider": "*",
            "size": "*",
            "limit_per_period": 10,
            "period_size": "MM",
            "period_interval": 1,
        },
    }


@pytest.fixture(scope="class")
def free_shipping_instance():
    return FreeShipping()


@pytest.fixture(scope="class")
def discount_limit_instance():
    return DiscountLimit()
