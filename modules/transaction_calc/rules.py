import datetime
import json
from datetime import timedelta
from modules.models import Transaction
from modules.extensions import config


class Rule:
    free_shipping_limit = 0
    free_shipping_met = 0
    free_shipping_reset_at = None

    discount_limit = 0
    discount_limit_reset_at = None

    @classmethod
    def apply_free_shipping(cls, transaction: Transaction):
        # Initial limit set
        if not cls.free_shipping_reset_at:
            cls.free_shipping_reset_at = transaction.date

        # Calculate free shipping limit reset date
        if transaction.date >= cls.free_shipping_reset_at:
            cls.free_limit = 0
            cls.free_shipping_met = 0
            if config["free"]["time"] == "MM":
                cls.free_shipping_reset_at = transaction.date.replace(
                    day=1, month=transaction.date.month + 1
                )
        # Check if conditions are met
        if (
            (
                transaction.size in config["free"]["size"]
                or config["free"]["size"] == "*"
            )
            and (
                transaction.provider in config["free"]["provider"]
                or config["free"]["provider"] == "*"
            )
            and cls.free_limit != config["free"]["limit"]
        ):
            cls.free_shipping_met += 1
            if cls.free_shipping_met == config["free"]["every"]:
                cls.free_limit += 1
                transaction.set_discount(transaction.price)

    @classmethod
    def apply_discount_limit(cls, transaction: Transaction):
        # Initial limit set
        if not cls.discount_limit_reset_at:
            cls.discount_limit_reset_at = transaction.date

        # Calculate free shipping limit reset date
        if transaction.date >= cls.discount_limit_reset_at:
            cls.free_limit = 0
            if config["discount"]["time"] == "MM":
                cls.discount_limit_reset_at = transaction.date.replace(
                    day=1, month=transaction.date.month + 1
                )

        # Check if conditions are met
        if (
            transaction.size in config["discount"]["size"]
            or config["discount"]["size"] == "*"
        ) and (
            transaction.provider in config["discount"]["provider"]
            or config["discount"]["provider"] == "*"
        ):
            if cls.discount_limit < config["discount"]["limit"]:
                discount = (
                    transaction.discount
                    if transaction.discount
                    < config["discount"]["limit"] - cls.discount_limit
                    else config["discount"]["limit"] - cls.discount_limit
                )

                transaction.set_discount(discount, True)
                cls.discount_limit += discount

    def apply_lowest_shipping(self, transaction: Transaction, pricing: dict):
        # Calculate lowest price and discount by 'lowest price' rule
        if transaction.size in config["lowest"]:
            # calculates the lowest available price for the given size
            lowest_price = min(
                [
                    entry["price"]
                    for entry in pricing
                    if entry["size"] == transaction.size
                ]
            )
            # calculates the discount for the given size and provider
            discount = (
                next(
                    (
                        entry["price"]
                        for entry in pricing
                        if entry["size"] == transaction.size
                        and entry["provider"] == transaction.provider
                    ),
                    0,
                )
                - lowest_price
            )
            transaction.set_discount(discount)
