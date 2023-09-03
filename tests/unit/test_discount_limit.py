import pytest

from modules.models import Transaction


class Testas:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.3, "2015-02-05 S LP 0.20 1.30"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.5, "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", 1.02, "2015-02-05 S LP 0.48 1.02"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", 1.99, "2015-02-05 S MR 0.82 1.18"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1.6, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1.4, "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1.26, "2015-03-05 S LP 0.24 1.26"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1.46, "2015-03-05 S LP 0.04 1.46"),
            ("2015-03-05 S LP", 1.12, "2015-03-05 S LP 0.38 1.12"),
            ("2015-03-05 S LP", 1.49, "2015-03-05 S LP 0.01 1.49"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is applied correctly when limit is 10"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "*",
            "size": "*",
            "limit_per_period": 10,
            "period_size": "MM",
            "period_interval": 1,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()


class TestDiscountLimit5:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.3, "2015-02-05 S LP 0.20 1.30"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.5, "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", 1.02, "2015-02-05 S LP 1.30 0.20"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1.6, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1.4, "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1.32, "2015-03-05 S LP 0.18 1.32"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1.11, "2015-03-05 S LP 0.39 1.11"),
            ("2015-03-05 S LP", 1.2, "2015-03-05 S LP 0.93 0.57"),
            ("2015-03-05 S LP", 1.56, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is applied correctly when limit is 5"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "*",
            "size": "*",
            "limit_per_period": 5,
            "period_size": "MM",
            "period_interval": 1,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()


class TestDiscountLimitProvider:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.3, "2015-02-05 S LP 0.20 1.30"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S LP", 1.5, "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", 1.02, "2015-02-05 S LP 1.30 0.20"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S MR", 1.1, "2015-02-05 S MR 0.90 1.10"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1.2, "2015-03-05 S LP 0.30 1.20"),
            ("2015-03-05 S LP", 1.49, "2015-03-05 S LP 0.01 1.49"),
            ("2015-03-05 S LP", 1.18, "2015-03-05 S LP 0.32 1.18"),
            ("2015-03-05 S LP", 1.12, "2015-03-05 S LP 0.38 1.12"),
            ("2015-03-05 S LP", 1.15, "2015-03-05 S LP 1.49 0.01"),
            ("2015-03-05 S LP", 1.24, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is applied correctly when provider is LP"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "LP",
            "size": "*",
            "limit_per_period": 5,
            "period_size": "MM",
            "period_interval": 1,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()


class TestDiscountLimitSize:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 M LP", 0, "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", 1.3, "2015-02-05 M LP 3.60 1.30"),
            ("2015-02-05 M LP", 0, "2015-02-05 M LP 4.90 -"),
            ("2015-02-05 M LP", 1.5, "2015-02-05 M LP 3.40 1.50"),
            ("2015-02-05 M LP", 1.02, "2015-02-05 M LP 3.88 1.02"),
            ("2015-02-05 M LP", 1, "2015-02-05 M LP 3.90 1.00"),
            ("2015-02-05 M MR", 2, "2015-02-05 M MR 1.82 1.18"),
            ("2015-02-05 M MR", 2, "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", 1, "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", 1.6, "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", 1, "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 M MR", 1.4, "2015-02-05 M MR 3.00 -"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 1.00 1.00"),
            ("2015-02-05 S MR", 1.6, "2015-02-05 S MR 0.40 1.60"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 1.00 1.00"),
            ("2015-02-05 S MR", 1.4, "2015-02-05 S MR 0.60 1.40"),
            ("2015-03-05 M LP", 1, "2015-03-05 M LP 3.90 1.00"),
            ("2015-03-05 M LP", 2, "2015-03-05 M LP 2.90 2.00"),
            ("2015-03-05 M LP", 1, "2015-03-05 M LP 3.90 1.00"),
            ("2015-03-05 M LP", 1.7, "2015-03-05 M LP 3.20 1.70"),
            ("2015-03-05 M LP", 1.9, "2015-03-05 M LP 4.60 0.30"),
            ("2015-03-05 M LP", 1.56, "2015-03-05 M LP 4.90 -"),
            ("2015-03-05 M LP", 1, "2015-03-05 M LP 4.90 -"),
            ("2015-03-05 M LP", 1, "2015-03-05 M LP 4.90 -"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is applied correctly when size is M"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "*",
            "size": "M",
            "limit_per_period": 6,
            "period_size": "MM",
            "period_interval": 1,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()


class TestDiscountLimitInvalidPeriod:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 S LP", 0, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", 1.3, "2015-02-05 S LP 0.20 1.30"),
            ("2015-02-05 S LP", 0, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", 1.5, "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", 1.02, "2015-02-05 S LP 0.48 1.02"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 1.00 1.00"),
            ("2015-02-05 S MR", 1.6, "2015-02-05 S MR 0.40 1.60"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 1.00 1.00"),
            ("2015-02-05 S MR", 1.4, "2015-02-05 S MR 0.60 1.40"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 2, "2015-03-05 S LP -0.50 2.00"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1.12, "2015-03-05 S LP 0.38 1.12"),
            ("2015-03-05 S LP", 1.15, "2015-03-05 S LP 0.35 1.15"),
            ("2015-03-05 S LP", 1.36, "2015-03-05 S LP 0.14 1.36"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 0.50 1.00"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is not applied when period is YY"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "*",
            "size": "*",
            "limit_per_period": 10,
            "period_size": "YY",
            "period_interval": 1,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()


class TestDiscountLimitInterval2:
    @pytest.mark.parametrize(
        "transaction_line,discount,expected",
        [
            ("2015-02-05 S LP", 0, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", 1.3, "2015-02-05 S LP 0.20 1.30"),
            ("2015-02-05 S LP", 0, "2015-02-05 S LP 1.50 -"),
            ("2015-02-05 S LP", 1.5, "2015-02-05 S LP 0.00 1.50"),
            ("2015-02-05 S LP", 1.02, "2015-02-05 S LP 0.48 1.02"),
            ("2015-02-05 S LP", 1, "2015-02-05 S LP 0.50 1.00"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", 2, "2015-02-05 S MR 0.00 2.00"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 1.00 1.00"),
            ("2015-02-05 S MR", 1.6, "2015-02-05 S MR 1.82 0.18"),
            ("2015-02-05 S MR", 1, "2015-02-05 S MR 2.00 -"),
            ("2015-02-05 S MR", 1.4, "2015-02-05 S MR 2.00 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 2, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1.12, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1.15, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1.36, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-03-05 S LP", 1, "2015-03-05 S LP 1.50 -"),
            ("2015-04-05 L LP", 3.12, "2015-04-05 L LP 3.78 3.12"),
            ("2015-04-05 L LP", 3.15, "2015-04-05 L LP 3.75 3.15"),
            ("2015-04-05 L LP", 3.36, "2015-04-05 L LP 3.54 3.36"),
            ("2015-06-05 L LP", 3.12, "2015-06-05 L LP 3.78 3.12"),
            ("2015-06-05 L LP", 3.15, "2015-06-05 L LP 3.75 3.15"),
            ("2015-06-05 L LP", 3.36, "2015-06-05 L LP 3.54 3.36"),
            ("2015-07-05 L LP", 3.12, "2015-07-05 L LP 6.53 0.37"),
            ("2015-07-05 L LP", 3.15, "2015-07-05 L LP 6.90 -"),
            ("2015-07-05 L LP", 3.36, "2015-07-05 L LP 6.90 -"),
        ],
    )
    def test_discount_limit(
        self, transaction_line, discount, expected, discount_limit_instance, pricing
    ):
        """Test if discount limit is applied correctly when interval is 2"""
        transaction = Transaction()
        transaction.validate_transaction(transaction_line, pricing)
        transaction.discount = discount
        config = {
            "provider": "*",
            "size": "*",
            "limit_per_period": 10,
            "period_size": "MM",
            "period_interval": 2,
        }
        discount_limit_instance.apply(
            transaction,
            config,
        )
        assert expected == transaction.print_line()
