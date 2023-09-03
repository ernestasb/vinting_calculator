import pytest

from modules.models import Transaction
from modules.transaction_calc.rules.lowest_shipping import LowestShipping


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 S LP", "2015-02-01 S LP 1.50 -"),
        ("2015-02-01 S MR", "2015-02-01 S MR 1.50 0.50"),
    ],
)
def test_lowest_shipping_s(transaction_line, pricing, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing)
    rule = LowestShipping().apply(transaction, pricing, "S")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 M LP", "2015-02-01 M LP 3.00 1.90"),
        ("2015-02-01 M MR", "2015-02-01 M MR 3.00 -"),
    ],
)
def test_lowest_shipping_m(transaction_line, pricing, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing)
    rule = LowestShipping().apply(transaction, pricing, "M")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 L LP", "2015-02-01 L LP 4.00 2.90"),
        ("2015-02-01 L MR", "2015-02-01 L MR 4.00 -"),
    ],
)
def test_lowest_shipping_l(transaction_line, pricing, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing)
    rule = LowestShipping().apply(transaction, pricing, "L")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 S LP", "2015-02-01 S LP 1.00 -"),
        ("2015-02-01 S MR", "2015-02-01 S MR 1.00 2.00"),
    ],
)
def test_lowest_shipping_s1(transaction_line, pricing1, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing1)
    rule = LowestShipping().apply(transaction, pricing1, "S")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 M LP", "2015-02-01 M LP 1.00 1.00"),
        ("2015-02-01 M MR", "2015-02-01 M MR 1.00 -"),
    ],
)
def test_lowest_shipping_m1(transaction_line, pricing1, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing1)
    rule = LowestShipping().apply(transaction, pricing1, "M")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 L LP", "2015-02-01 L LP 1.00 2.00"),
        ("2015-02-01 L MR", "2015-02-01 L MR 1.00 -"),
    ],
)
def test_lowest_shipping_l1(transaction_line, pricing1, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing1)
    rule = LowestShipping().apply(transaction, pricing1, "L")

    assert transaction.print_line() == expected


@pytest.mark.parametrize(
    "transaction_line, expected",
    [
        ("2015-02-01 L LP", "2015-02-01 L LP 1.00 2.00"),
        ("2015-02-01 S MR", "2015-02-01 S MR 1.00 2.00"),
    ],
)
def test_lowest_shipping_multi(transaction_line, pricing1, expected):
    transaction = Transaction()
    transaction.validate_transaction(transaction_line, pricing1)
    rule = LowestShipping().apply(transaction, pricing1, ["L", "S"])

    assert transaction.print_line() == expected
