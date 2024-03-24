"""
Goal of the program: a bank account class (now with dictionaries)
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""
from __future__ import annotations
from typeguard import typechecked
from random import randint


@typechecked
class BankAccount:  # I notice the warnings, but I consider that neither of those methods must be static.

    __EXISTING_ACCOUNT_NUMBERS = []
    __MOVEMENTS_REGISTER = {}

    def __init__(self, balance: float = 0):
        self.__balance = self.__errorproof(balance)
        self.__account_number = self.generate_account_number()
        BankAccount.__MOVEMENTS_REGISTER[self.__account_number] = []

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @property
    def movements(self):
        movements = f"Movimientos de la cuenta {self.__account_number}:\n-----------------------\n"
        for n in range(len(BankAccount.__MOVEMENTS_REGISTER[self.__account_number])):
            movements += f"{BankAccount.__MOVEMENTS_REGISTER[self.__account_number][n]}\n"
        return movements

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

    def deposit(self, amount: float,  transference_warning: bool = False):
        self.__balance += self.__errorproof(amount)
        if not transference_warning:
            self.__register_movement(1, amount)

    def withdraw(self, amount: float,  transference_warning: bool = False):
        self.__errorproof(amount)
        if amount > self.__balance:
            raise ValueError("Withdrawal exceeds this account's balance.")
        self.__balance -= amount
        if not transference_warning:
            self.__register_movement(2, amount)
        return amount

    def transfer(self, receiver: BankAccount, amount: float):
        receiver.deposit(self.withdraw(amount, True), True)
        self.__register_transference(receiver, amount)

    def __register_movement(self, operation_code: int, amount: float = 0):
        if operation_code == 1:
            BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(f"Ingreso de {amount}€."
                                                                           f" Saldo: {self.__balance}€")
        elif operation_code == 2:
            BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(f"Cargo de {amount}€."
                                                                           f" Saldo: {self.__balance}€")
        else:
            raise SyntaxError("Invalid operation code.")

    def __register_transference(self, other: BankAccount, amount: float):
        BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(f"Transferencia emitida de {amount}€ a la "
                                                                       f"cuenta {other.account_number}."
                                                                       f" Saldo: {self.__balance}€")

        BankAccount.__MOVEMENTS_REGISTER[other.__account_number].append(f"Transferencia de {amount}€ recibida desde la "
                                                                        f"cuenta {other.account_number}€."
                                                                        f" Saldo: {other.__balance}€")

    def __str__(self):
        return f"Account {self.__account_number}. Balance: {self.__balance}€"

    def __del__(self):
        BankAccount.__EXISTING_ACCOUNT_NUMBERS.remove(self.__account_number)


def main():
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    cuenta1.deposit(2000)
    cuenta1.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta1, 100)
    cuenta1.transfer(cuenta3, 250)
    cuenta3.transfer(cuenta1, 22)
    print(cuenta1.movements)


if __name__ == "__main__":
    main()
