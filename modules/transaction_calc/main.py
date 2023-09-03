from datetime import datetime
import json
import sys
from modules.errors import TransactionValidationException
from modules.extensions import config
from modules.models import Transaction
from modules.transaction_calc.rules.discount_limit import DiscountLimit
from modules.transaction_calc.rules.free_shipping import FreeShipping
from modules.transaction_calc.rules.lowest_shipping import LowestShipping


def process_file(transactions_file):
    """Function to read file and print each line after
    Args:
        transactions_file (str): transactions file path
    """

    with open(transactions_file, "r") as file:
        # Create rule instances here
        lowest_shipping = LowestShipping()
        free_shipping = FreeShipping()
        dicount_limit = DiscountLimit()

        # In combination of 'with open' and 'for' loop each line is loaded to the memory separately,  rather than loading the whole file at once, thus saving memory
        for line in file:
            try:
                # Create new instance of Transaction class
                transaction = Transaction()
                # Validate transaction line and assign values to the class instance
                transaction.validate_transaction(line, config["pricing"])

                #### Start: Custom rules applied to the transaction

                lowest_shipping.apply(transaction, config["pricing"], config["lowest"])
                free_shipping.apply(transaction, config["free"])
                # Discount rule should be always applied last, after discounts are already calculated
                dicount_limit.apply(transaction, config["discount"])

                #### End: Custom rules applied to the transaction

                # final step, after all rules have been applied
                print(transaction.print_line())

            except TransactionValidationException as e:
                print(e.ignored_line)
                # print(f"  {e.custom_message}")
