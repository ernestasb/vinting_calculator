from modules.models import Transaction


class LowestShipping:
    def apply(self, transaction: Transaction, pricing: dict, rule_config: dict):
        # Calculate lowest price and discount by 'lowest price' rule
        if transaction.size in rule_config:
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
