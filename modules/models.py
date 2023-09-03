"""Module containing data models"""

import datetime

from modules.errors import TransactionValidationException


# This class was created for better readability when processing transaction,
# so no string parsing has to be done when creating new rules later on
class Transaction:
    """Transaction class to store and manipulate transaction data"""

    def __init__(
        self,
        date: datetime.date = None,
        size: str = None,
        provider: str = None,
        price: float = 0,
    ):
        """Constructor for Transaction class

        Args:
            date (date, optional): Transaction date. Defaults to None.
            size (str, optional): Transaction size. Defaults to None.
            provider (str, optional): Transaction provider. Defaults to None.
            price (float, optional): Transaction price. Defaults to 0.
        """
        self.date = date
        self.size = size
        self.provider = provider
        self.price = price
        self.discount = 0

    # this was creates to seamlesly send the line from the file and the object
    # creates itsef based on the line validity and values
    def validate_transaction(self, line: str, pricing: dict):
        """Validate transaction line and assign values to the class instance.
        Throws TransactionValidationException if validation fails.
        Vaidation conditions:
        - line contains 3 values
        - date is in correct format which is YYYY-MM-DD

        Example line: '2015-02-01 Size Provider'

        Args:
            line (str): transaction line as a string
            pricing (dict): dictionary containing pricing data

        Raises:
            TransactionValidationException: Line does not contain 3 values
            TransactionValidationException: Size and provider combination does not exist
        """
        parts = line.strip().split()

        # Validate if line contains 3 values, else - raise error
        if len(parts) != 3:
            raise TransactionValidationException("Line does not contain 3 values", line)

        # Validate if date is in correct format which is YYYY-MM-DD
        self.date = datetime.date.fromisoformat(parts[0])
        self.size = parts[1]
        self.provider = parts[2]
        # Validate if size and provider combination can be found in 'pricing' list
        if not any(
            pricing["size"] == parts[1] and pricing["provider"] == parts[2]
            for pricing in pricing
        ):
            # if combination is not found - raise error
            raise TransactionValidationException(
                f"Size and provider combination does not exist: {parts[1]} : {parts[2]}",
                line,
            )
        self.price = next(
            pricing["price"]
            for pricing in pricing
            if pricing["size"] == parts[1] and pricing["provider"] == parts[2]
        )

    def set_discount(self, discount: float, override=False):
        """Set discount to the transaction
        Conditions to apply discount:
        - discount is greater than 0
        - discount is greater than current discount
        - discount is less or equal to price

        Args:
            discount (decimal): discount to be applied
            override (bool, optional): override discount if True. Defaults to False.
        """
        if discount >= 0 and discount >= self.discount:
            self.discount = discount
        if self.discount > self.price and not override:
            self.discount = self.price
        if override:
            self.discount = discount

    def print_line(self, float_point: int = 2):
        """Print line with discount if applicable
        Args:
            float_point (int, optional): floating point to format price and discount. Defaults to 2.
        Returns:
            str: line to be printed (with discount if applicable)
        """
        return (
            f"{self.date} {self.size} {self.provider} "
            f"{self.price - self.discount:.{float_point}f} "
            f"{'-' if self.discount == 0 else f'{self.discount:.{float_point}f}'}"
        )
