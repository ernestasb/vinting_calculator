import pytest
from datetime import date
from modules.errors import TransactionValidationException
from modules.models import Transaction


@pytest.mark.parametrize(
    "transaction_obj_data",
    [
        {
            "date": "2015-02-01",
            "size": "S",
            "provider": "LP",
            "price": 1.5,
        },
        {
            "date": "2015-02-01",
            "size": "X",
            "provider": "LP",
            "price": 1.5,
        },
        {
            "date": "2015-02-01",
            "size": "S",
            "provider": "52",
            "price": 1.5,
        },
        {
            "date": "2015-02-01",
            "size": "S",
            "provider": "LP",
            "price": 100,
        },
    ],
)
def test_create_class_success(transaction_obj_data):
    """Test if class is created successfully using constructor"""
    transaction = Transaction(**transaction_obj_data)
    assert transaction.date == transaction_obj_data["date"]
    assert transaction.size == transaction_obj_data["size"]
    assert transaction.provider == transaction_obj_data["provider"]
    assert transaction.price == transaction_obj_data["price"]
    assert transaction.discount == 0


@pytest.mark.parametrize(
    "transaction_line",
    [
        "2015-02-01 S MR",
        "2015-02-02 S MR",
        "2015-02-03 L LP",
        "2015-02-05 S LP",
        "2015-02-06 S MR",
        "2015-02-06 L LP",
        "2015-02-07 L MR",
        "2015-02-08 M MR",
        "2015-02-09 L LP",
        "2015-02-10 L LP",
        "2015-02-10 S MR",
        "2015-02-10 S MR",
        "2015-02-11 L LP",
        "2015-02-12 M MR",
        "2015-02-13 M LP",
        "2015-02-15 S MR",
        "2015-02-17 L LP",
        "2015-02-17 S MR",
        "2015-02-24 L LP",
    ],
)
def test_validate_line_success(transaction_line, pricing):
    """Test if line is validated successfully, when data is correct"""
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing)
    assert transaction.date == date.fromisoformat(transaction_line.split()[0])
    assert transaction.size == transaction_line.split()[1]
    assert transaction.provider == transaction_line.split()[2]
    assert transaction.discount == 0
    assert transaction.price == next(
        pricing["price"]
        for pricing in pricing
        if pricing["size"] == transaction_line.split()[1]
        and pricing["provider"] == transaction_line.split()[2]
    )


@pytest.mark.parametrize(
    "transaction_line",
    [
        "2015-02-01 S ",
        "2015-02-02  MR",
        "2015-02-03 x LP",
        "2015-02-05 S x",
        "2015-02- S MR",
        "2015-02 L LP",
        "2015 L MR",
        "MR",
        "L ",
        "2015-02-10",
        "2015-02-10 S MR GG",
        "2015-02-10 S MR XD DX",
        "CC L LP",
    ],
)
def test_validate_line_fail(transaction_line, pricing):
    """Test if line is validated successfully, when data is incorrect"""
    with pytest.raises((TransactionValidationException, ValueError)):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)


@pytest.mark.parametrize("discount", [10, 5, 1, 8, 0.1, 50, 100, 0.5, 0.01, 0.001])
def test_set_discount(discount):
    """Test if discount is set successfully"""
    transaction = Transaction()
    transaction.price = 20
    transaction.set_discount(discount)
    assert transaction.discount == discount if discount <= 20 else 20


@pytest.mark.parametrize(
    "transaction_obj_data,discount,expected",
    [
        (
            {
                "date": "2015-02-01",
                "size": "S",
                "provider": "LP",
                "price": 1.5,
            },
            10,
            "2015-02-01 S LP 0.00 1.50",
        ),
        (
            {
                "date": "2015-02-01",
                "size": "X",
                "provider": "LP",
                "price": 1.5,
            },
            0,
            "2015-02-01 X LP 1.50 -",
        ),
        (
            {
                "date": "2015-02-01",
                "size": "S",
                "provider": "52",
                "price": 1.5,
            },
            1.3,
            "2015-02-01 S 52 0.20 1.30",
        ),
        (
            {
                "date": "2015-02-01",
                "size": "S",
                "provider": "LP",
                "price": 100,
            },
            98,
            "2015-02-01 S LP 2.00 98.00",
        ),
    ],
)
def test_print_line(transaction_obj_data, discount, expected):
    """Test if class is created successfully using constructor"""
    transaction = Transaction(**transaction_obj_data)
    transaction.set_discount(discount)

    assert transaction.print_line() == expected
