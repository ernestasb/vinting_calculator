"""Module containing DiscountLimit class"""
from modules.models import Transaction


class DiscountLimit:
    """DiscountLimit class to apply discount limit rule"""

    discount_limit = 0
    discount_limit_reset_at = None

    def apply(self, transaction: Transaction, rule_config: dict):
        """Apply discount limit rule

        Args:
            transaction (Transaction): transaction object
            rule_config (dict): rule configuration
        """
        # Initial limit set
        if not self.discount_limit_reset_at:
            self.discount_limit_reset_at = transaction.date

        # Calculate free shipping limit reset date when current transaction in next period
        if transaction.date >= self.discount_limit_reset_at:
            self.discount_limit = 0
            if rule_config["period_size"] == "MM":
                self.discount_limit_reset_at = transaction.date.replace(
                    day=1, month=transaction.date.month + rule_config["period_interval"]
                )

        # Check if conditions are met
        if (transaction.size in rule_config["size"] or rule_config["size"] == "*") and (
            transaction.provider in rule_config["provider"]
            or rule_config["provider"] == "*"
        ):
            # Apply discount limit if there is any left
            if self.discount_limit < rule_config["limit_per_period"]:
                discount = (
                    transaction.discount
                    if transaction.discount
                    < rule_config["limit_per_period"] - self.discount_limit
                    else rule_config["limit_per_period"] - self.discount_limit
                )

                transaction.set_discount(discount, True)
                self.discount_limit += discount
            else:
                # When limit is reached, reset discount
                transaction.discount = 0
