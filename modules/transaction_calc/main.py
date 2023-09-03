from datetime import datetime
import json
import sys
from modules.errors import TransactionValidationException
from modules.extensions import config
from modules.models import Transaction
from modules.transaction_calc.rules import Rule


def process_file(transactions_file):
    """Function to read file and print each line after
    Args:
        transactions_file (str): transactions file path
    """
    with open(transactions_file, "r") as file:
        # In combination with 'for' loop each line is loaded to the memory separately,  rather than loading whole file at once, thus saving memory
        rules = Rule()
        for line in file:
            try:
                # Create new instance of Transaction class
                transaction = Transaction()
                # Validate transaction line and assign values to the class instance
                transaction.validate_transaction(line, config["pricing"])

                # Start: Custom rules applied to the transaction
                rules.apply_lowest_shipping(transaction, config["pricing"])
                rules.apply_free_shipping(transaction)
                rules.apply_discount_limit(transaction)
                # End: Custom rules applied to the transaction

                # final step, after all rules have been applied
                print(transaction.print_line())

            except TransactionValidationException as e:
                print(e.ignored_line)
                # print(f"  {e.custom_message}")
