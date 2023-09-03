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
        """Test if free shipping rule applied correctly"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "S",
                "every_nth_free": 3,
                "limit_per_period": 1,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule not applied when size is incorrect"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "X",
                "every_nth_free": 3,
                "limit_per_period": 1,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule not applied when supplier is incorrect"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "XX",
                "size": "S",
                "every_nth_free": 3,
                "limit_per_period": 1,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule is applied correctly for multiple providers with different limit"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S",
                "every_nth_free": 3,
                "limit_per_period": 3,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule is applied correctly for multiple providers and sizes"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S,M",
                "every_nth_free": 3,
                "limit_per_period": 3,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule is applied correctly for wildcard size"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP",
                "size": "*",
                "every_nth_free": 1,
                "limit_per_period": 20,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule is applied correctly for wildcard size and provider"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "*",
                "size": "*",
                "every_nth_free": 1,
                "limit_per_period": 20,
                "period_size": "MM",
                "period_interval": 1,
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
        """Test if free shipping rule is not applied for year time"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "*",
                "size": "*",
                "every_nth_free": 2,
                "limit_per_period": 32,
                "period_size": "YY",
                "period_interval": 1,
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
        """Test if free shipping rule is applied correctly for every 2 months"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        free_shipping_instance.apply(
            transaction,
            {
                "provider": "LP,MR",
                "size": "S,M",
                "every_nth_free": 3,
                "limit_per_period": 3,
                "period_size": "MM",
                "period_interval": 2,
            },
        )
        assert expected == transaction.print_line()
