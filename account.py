class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up object
        :param name: Account name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit given amount into object's balance
        :param amount: Given amount to be deposited
        :return: Returns True if amount > 0, else returns False
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw given amount from object's balance
        :param amount: Given amount to be withdrawn
        :return: Returns True if amount > 0 but less than current balance, else returns False
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Function to get object's balance
        :return: Object's balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to get object's name
        :return: Object's name
        """
        return aself.__account_name