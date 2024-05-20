class Bill:
    """
    A class to represent a bill.

    Attributes:
    ----------
    amount : float
        The monetary amount of the bill.
    period : str
        The period for which the bill is applicable (e.g., 'January 2024').

    Methods:
    -------
    __repr__():
        Returns a string representation of the Bill instance.
    """

    def __init__(self, amount: float, period: str) -> None:
        self.amount = self._validate_amount(amount)
        self.period = self._validate_period(period)

    def __repr__(self):
        return f"Bill(amount={self.amount}, period='{self.period}')"

    @staticmethod
    def _validate_amount(amount: float) -> float:
        """
        Validates the amount of the bill.

        Parameters:
        ----------
        amount : float
            The monetary amount of the bill.

        Returns:
        -------
        float
            The validated amount.

        Raises:
        ------
        ValueError
            If the amount is not a positive number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        return amount

    @staticmethod
    def _validate_period(period: str) -> str:
        """
        Validates the period of the bill.

        Parameters:
        ----------
        period : str
            The period for which the bill is applicable.

        Returns:
        -------
        str
            The validated period.

        Raises:
        ------
        ValueError
            If the period is not a string.
        """
        if not isinstance(period, str):
            raise ValueError("Period must be a string.")
        return period
