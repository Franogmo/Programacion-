"""
Goal of the program: a bank account class
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""
from __future__ import annotations
from typeguard import typechecked
from random import randint


@typechecked
class BankAccount:

    __EXISTING_ACCOUNT_NUMBERS = []

    def __init__(self, balance: float = 0):
        self.__balance = self.__errorproof(balance)
        self.__account_number = self.generate_account_number()

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def generate_account_number(self):
        while True:
            aspiring_number = str(10000000000 + randint(0, 99999999999))[1:]
            if aspiring_number not in BankAccount.__EXISTING_ACCOUNT_NUMBERS:
                BankAccount.__EXISTING_ACCOUNT_NUMBERS.append(aspiring_number)
                return aspiring_number

    def __errorproof(self, amount: float):
        if amount < 0:
            raise ValueError("Accounts are not allowed to have a negative balance.")
        return amount

    def deposit(self, amount: float):
        self.__balance += self.__errorproof(amount)

    def withdraw(self, amount: float):
        self.__errorproof(amount)
        if amount > self.__balance:
            raise ValueError("Withdrawal exceeds this account's balance.")
        self.__balance -= amount
        return amount

    def transfer(self, receiver: BankAccount, amount: float):
        receiver.deposit(self.withdraw(amount))

    def __str__(self):
        return f"Account {self.__account_number}. Balance: {self.__balance}€"

    def __del__(self):
        BankAccount.__EXISTING_ACCOUNT_NUMBERS.remove(self.__account_number)


def main():
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)


if __name__ == "__main__":
    main()
