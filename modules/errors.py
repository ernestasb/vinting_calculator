"""Module containing custom exceptions."""


# this file is created to define custom exceptions that can be used in the application
class TransactionValidationException(Exception):
    """Exception raised for errors when validationg line."""

    def __init__(self, error_message, ignored_line):
        """Constructor for TransactionValidationException class.

        Args:
            error_message (str): Error message.
            ignored_line (str): Line that has to be ignored.
        """
        self.custom_message = error_message
        self.ignored_line = f"{ignored_line.strip()} Ignored"
