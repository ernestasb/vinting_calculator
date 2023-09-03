import pytest

from modules.models import Transaction


class TestFreeShipping:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_free_shipping(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "S",
                "every": 3,
                "limit": 1,
                "time": "MM",
                "interval": 1,
            },
        )
        assert transaction.print_line() == expected


class TestFreeShippingIncorrectSize:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_free_shipping_incorrect_size(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "X",
                "every": 3,
                "limit": 1,
                "time": "MM",
                "interval": 1,
            },
        )
        assert transaction.print_line() == expected


class TestFreeShippingIncorrectSupplier:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_free_shipping_incorrect_supplier(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "XX",
                "size": "S",
                "every": 3,
                "limit": 1,
                "time": "MM",
                "interval": 1,
            },
        )
        assert transaction.print_line() == expected


class TestFreeShippingLimitMultiProvider:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
        ],
    )
    def test_free_shipping_limit_multi_provider(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S",
                "every": 3,
                "limit": 3,
                "time": "MM",
                "interval": 1,
            },
        )
        assert expected == transaction.print_line()


class TestFreeShippingLimitMultiSize:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 M LP", "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 0.00 3.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
        ],
    )
    def test_free_shipping_limit_multi_size(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S,M",
                "every": 3,
                "limit": 3,
                "time": "MM",
                "interval": 1,
            },
        )
        assert expected == transaction.print_line()


class TestFreeShippingWildcardSize:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
        ],
    )
    def test_free_shipping_every_of_lp(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "*",
                "every": 1,
                "limit": 20,
                "time": "MM",
                "interval": 1,
            },
        )
        assert expected == transaction.print_line()


class TestFreeShippingWildcardSizeProvider:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M LP", "2015-02-05 M LP 0.00 4.90"),
            ("2015-02-05 M MR", "2015-02-05 M MR 0.00 3.00"),
            ("2015-02-05 M MR", "2015-02-05 M MR 0.00 3.00"),
            ("2015-02-05 M MR", "2015-02-05 M MR 0.00 3.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 0.00 2.00"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
            ("2015-03-05 S LP", "2015-03-05 S LP 0.00 1.50"),
        ],
    )
    def test_free_shipping_every_of_lp(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "*",
                "size": "*",
                "every": 1,
                "limit": 20,
                "time": "MM",
                "interval": 1,
            },
        )
        assert expected == transaction.print_line()


class TestFreeShippingYearNotImplemented:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 M LP", "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_free_shipping_every_of_lp(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "*",
                "size": "*",
                "every": 2,
                "limit": 32,
                "time": "YY",
                "interval": 1,
            },
        )
        assert expected == transaction.print_line()


class TestFreeShippingEvery2Months:
    @pytest.mark.parametrize(
        "transaction_line,expected",
        [
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", "2015-03-05 S LP 1.50 -"),
            ("2015-04-05 S LP", "2015-04-05 S LP 1.50 -"),
            ("2015-04-05 S LP", "2015-04-05 S LP 1.50 -"),
            ("2015-04-05 S LP", "2015-04-05 S LP 0.00 1.50"),
            ("2015-06-05 S LP", "2015-06-05 S LP 1.50 -"),
            ("2015-06-05 S LP", "2015-06-05 S LP 1.50 -"),
            ("2015-06-05 S LP", "2015-06-05 S LP 0.00 1.50"),
        ],
    )
    def test_free_shipping_every_of_lp(
        self, transaction_line, expected, pricing, free_shipping_instance
    ):
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S,M",
                "every": 3,
                "limit": 3,
                "time": "MM",
                "interval": 2,
            },
        )
        assert expected == transaction.print_line()
