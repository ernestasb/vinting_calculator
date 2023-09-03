from modules.models import Transaction


class DiscountLimit:
    discount_limit = 0
    discount_limit_reset_at = None

    def apply(self, transaction: Transaction, rule_config: dict):
        # Initial limit set
        if not self.discount_limit_reset_at:
            self.discount_limit_reset_at = transaction.date

        # Calculate free shipping limit reset date
        if transaction.date >= self.discount_limit_reset_at:
            self.discount_limit = 0
            if rule_config["time"] == "MM":
                self.discount_limit_reset_at = transaction.date.replace(
                    day=1, month=transaction.date.month + 1
                )
        # Check if conditions are met
        if (transaction.size in rule_config["size"] or rule_config["size"] == "*") and (
            transaction.provider in rule_config["provider"]
            or rule_config["provider"] == "*"
        ):
            if self.discount_limit < rule_config["limit"]:
                discount = (
                    transaction.discount
                    if transaction.discount < rule_config["limit"] - self.discount_limit
                    else rule_config["limit"] - self.discount_limit
                )

                transaction.set_discount(discount, True)
                self.discount_limit += discount
            else:
                transaction.discount = 0
