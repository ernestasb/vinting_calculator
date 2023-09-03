from modules.models import Transaction


class FreeShipping:
    free_shipping_limit = 0
    free_shipping_met = 0
    free_shipping_reset_at = None

    def apply(self, transaction: Transaction, class_config: dict):
        # Initial limit set
        if not self.free_shipping_reset_at:
            self.free_shipping_reset_at = transaction.date
        # Calculate free shipping limit reset date
        if transaction.date >= self.free_shipping_reset_at:
            self.free_shipping_limit = 0
            self.free_shipping_met = 0
            if class_config["time"] == "MM":
                self.free_shipping_reset_at = transaction.date.replace(
                    day=1, month=transaction.date.month + class_config["interval"]
                )
            else:
                # if anything but MM
                return
        # Check if conditions are met
        print(
            self.free_shipping_reset_at,
            self.free_shipping_limit,
            self.free_shipping_met,
        )
        if (
            (transaction.size in class_config["size"] or class_config["size"] == "*")
            and (
                transaction.provider in class_config["provider"]
                or class_config["provider"] == "*"
            )
            and self.free_shipping_limit != class_config["limit"]
        ):
            self.free_shipping_met += 1
            if self.free_shipping_met == class_config["every"]:
                self.free_shipping_limit += 1
                self.free_shipping_met = 0
                print("discount")
                transaction.set_discount(transaction.price)
