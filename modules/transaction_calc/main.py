"""Module to process transactions file"""
from datetime import datetime
import json
import sys
from modules.errors import TransactionValidationException
from modules.models import Transaction
from modules.transaction_calc.rules.discount_limit import DiscountLimit
from modules.transaction_calc.rules.free_shipping import FreeShipping
from modules.transaction_calc.rules.lowest_shipping import LowestShipping

# whole calculation logic is done as a function for reusability (assuming this module will be later on used in other projects)
# decission was made to use json files for configuration, so that it is easy to change the configuration without changing the code, such configuration as size or provider names, prices, discounts, etc.

# I've attemted to separate the code as much as possible, while coding my firstpriority was to separate potentially reusable code. While developing this task for the whole time i was thinking that it will be used within another project as a module, so i tried to make it as reusable as possible.

# I had limited time, therefore i did not complete everything like i wanted, will mention couple of things
# TODO: configuration validation (to handle incorrect configuration json), YY and DD time periodvalidation (currently it works with MM which was a requirement for this task)


def process_file(transactions_file, config: dict):
    """Function to read file and print each line after
    Args:
        transactions_file (str): transactions file path
        config (dict): configuration dictionary
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

                lowest_shipping.apply(
                    transaction, config["pricing"], config["lowest_rule"]
                )
                free_shipping.apply(transaction, config["free_shipping_rule"])
                # Discount rule should be always applied last, after discounts are already calculated
                dicount_limit.apply(transaction, config["discount_limit_rule"])

                #### End: Custom rules applied to the transaction

                # final step, after all rules have been applied
                print(transaction.print_line())

            except TransactionValidationException as e:
                print(e.ignored_line)
                # print(f"  {e.custom_message}")
