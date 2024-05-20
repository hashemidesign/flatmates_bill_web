from models.bill import Bill


class Flatmate:
    """
    A class to represent a flatmate who lives in the flat and pays
    a share of the bill.

    Attributes:
    ----------
    name : str
        The name of the flatmate.
    days_in_house : int
        The number of days the flatmate has been in the house.

    Methods:
    -------
    pays(bill, flatmate):
        Calculates and returns the share of the bill to be paid by this flatmate.
    """

    def __init__(self, name: str, days_in_house: int) -> None:
        self.name = self._validate_name(name)
        self.days_in_house = self._validate_days_in_house(days_in_house)

    def pays(self, bill: Bill, flatmate: 'Flatmate') -> float:
        """
        Calculates and returns the share of the bill to be paid by this flatmate.

        Parameters:
        ----------
        bill : Bill
            The bill to be shared.
        flatmate : Flatmate
            The other flatmate sharing the bill.

        Returns:
        -------
        float
            The amount to be paid by this flatmate.
        """
        total_days = self.days_in_house + flatmate.days_in_house
        weight = self.days_in_house / total_days
        return bill.amount * weight

    def __repr__(self):
        return f"Flatmate(name='{self.name}', days_in_house={self.days_in_house})"

    @staticmethod
    def _validate_name(name):
        """
        Validates the name of the flatmate.

        Parameters:
        ----------
        name : str
            The name of the flatmate.

        Returns:
        -------
        str
            The validated name.

        Raises:
        ------
        ValueError
            If the name is not a string.
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        return name

    @staticmethod
    def _validate_days_in_house(days_in_house):
        """
        Validates the number of days in house.

        Parameters:
        ----------
        days_in_house : int
            The number of days the flatmate has been in the house.

        Returns:
        -------
        int
            The validated number of days.

        Raises:
        ------
        ValueError
            If the days_in_house is not a positive integer.
        """
        if not isinstance(days_in_house, int) or days_in_house < 0:
            raise ValueError("Days in house must be a non-negative integer.")
        return days_in_house
