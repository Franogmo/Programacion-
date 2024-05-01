"""
Goal of the program: a bank account class (now with dictionaries)
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""
from __future__ import annotations

from abc import ABC
from typeguard import typechecked
from random import randint


@typechecked
class Movement(ABC):

    def __init__(self):
        pass


@typechecked
class InternalMovement(Movement):

    ALLOWED_INTERNAL_MOVEMENTS = ["Ingreso", "Retirada", "Creación de cuenta"]

    def __init__(self, movement_type: str, amount: float, final_balance: float, source_account: str):
        super().__init__()
        self.__movement_type = self.__errorcheck(movement_type)
        self.__amount = amount
        self.__final_balance = final_balance
        self.__source_account = source_account

    @property
    def movement_type(self):
        return self.__movement_type

    @property
    def amount(self):
        return self.__amount

    @property
    def final_balance(self):
        return self.__final_balance

    @property
    def source_account(self):
        return self.__source_account

    def __errorcheck(self, checked_value):
        if checked_value not in InternalMovement.ALLOWED_INTERNAL_MOVEMENTS:
            raise InternalMovementError
        return checked_value

    def __str__(self):
        return (f"{self.__movement_type}. Importe: {self.__amount}€. Cuenta {self.__source_account}."
                f" Saldo resultante: {self.__final_balance}€")

    def __repr__(self):
        return f"{self.__movement_type}"


@typechecked
class Transference(Movement):

    def __init__(self, amount: float, source_account: str,
                 receiving_account: str, this_account: str, this_accounts_final_balance: float):
        super().__init__()
        self.__movement_type = "Transferencia"
        self.__amount = amount
        self.__source_account = source_account
        self.__receiving_account = receiving_account
        self.__this_account = this_account
        self.__this_accounts_final_balance = this_accounts_final_balance

    @property
    def movement_type(self):
        return self.__movement_type

    @property
    def amount(self):
        return self.__amount

    @property
    def source_account(self):
        return self.__source_account

    @property
    def receiving_account(self):
        return self.__receiving_account

    @property
    def this_account(self):
        return self.__this_account

    @property
    def this_accounts_final_balance(self):
        return self.__this_accounts_final_balance

    def __str__(self):
        return (f"{self.__movement_type} de la cuenta {self.__source_account} hacia la cuenta "
                f"{self.__receiving_account}. Importe: {self.__amount}€. Saldo resultante de la cuenta "
                f"{self.__this_account}: {self.__this_accounts_final_balance}€")

    def __repr__(self):
        return f"Transferencia"


@typechecked
class BankAccount:  # I notice the warnings, but I consider that neither of those methods must be static.

    __EXISTING_ACCOUNT_NUMBERS = []
    __MOVEMENTS_REGISTER = {}

    def __init__(self, balance: float = 0):
        self.__balance = self.__errorproof(balance)
        self.__account_number = self.__generate_account_number()
        BankAccount.__MOVEMENTS_REGISTER[self.__account_number] = [InternalMovement("Creación de cuenta",
                                                                                    self.__balance, self.__balance,
                                                                                    self.__account_number)]

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

    def __generate_account_number(self):
        while True:
            aspiring_number = str(10000000000 + randint(0, 99999999999))[1:]
            if aspiring_number not in BankAccount.__EXISTING_ACCOUNT_NUMBERS:
                BankAccount.__EXISTING_ACCOUNT_NUMBERS.append(aspiring_number)
                return aspiring_number

    def __errorproof(self, amount: float):
        if amount < 0:
            raise NegativeBalanceError
        return amount

    def deposit(self, amount: float,  transference_warning: bool = False):
        self.__balance += self.__errorproof(amount)
        if not transference_warning:
            self.__register_movement(1, amount)

    def withdraw(self, amount: float,  transference_warning: bool = False):
        self.__errorproof(amount)
        if amount > self.__balance:
            raise ExcessiveWithdrawalError
        self.__balance -= amount
        if not transference_warning:
            self.__register_movement(2, amount)
        return amount

    def transfer(self, receiver: BankAccount, amount: float):
        receiver.deposit(self.withdraw(amount, True), True)
        self.__register_transference(receiver, amount)

    def __register_movement(self, operation_code: int, amount: float = 0):
        if operation_code == 1:
            BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(InternalMovement("Ingreso",
                                                                                            amount, self.__balance,
                                                                                            self.__account_number,
                                                                                            ))
        elif operation_code == 2:
            BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(InternalMovement("Retirada",
                                                                                            amount, self.__balance,
                                                                                            self.__account_number))
        else:
            raise RegisterMovementError

    def __register_transference(self, other: BankAccount, amount: float):
        BankAccount.__MOVEMENTS_REGISTER[self.__account_number].append(Transference(amount, self.__account_number,
                                                                                    other.__account_number,
                                                                                    self.__account_number,
                                                                                    self.__balance))

        BankAccount.__MOVEMENTS_REGISTER[other.__account_number].append(Transference(amount, self.__account_number,
                                                                                     other.__account_number,
                                                                                     other.__account_number,
                                                                                     other.__balance))

    def __str__(self):
        return f"Account {self.__account_number}. Balance: {self.__balance}€"

    def __del__(self):
        BankAccount.__EXISTING_ACCOUNT_NUMBERS.remove(self.__account_number)

    def __has_spaces(self, text):
        for n in range(len(text)):
            if text[n] == " ":
                return True
        return False

    def print_movements(self):
        exit_key = ""
        while exit_key != "0":
            filename = input("Introduce un nombre para tu fichero (sin espacios): ")
            if not self.__has_spaces(filename):
                with open(f"{filename}.csv", "wt", encoding="utf8") as movements_csv:
                    print("cuenta,tipo,cantidad,receptortransferencia",file=movements_csv)
                    for n in BankAccount.__MOVEMENTS_REGISTER[self.__account_number]:
                        if isinstance(n,InternalMovement):
                            print(f"{n.source_account},{n.movement_type},{n.amount},", file=movements_csv)
                        elif isinstance(n,Transference):
                            print(f"{n.source_account},{n.movement_type},{n.amount},{n.receiving_account}"
                                  , file=movements_csv)
                            exit_key = "0"
            else:
                print("Este nombre contiene espacios.")
                exit_key = input("Introduce 0 si quieres salir.")




class InternalMovementError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Tipo de movimiento interno no válido.")


class NegativeBalanceError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Accounts are not allowed to have a negative balance.")


class ExcessiveWithdrawalError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Withdrawal exceeds this account's balance.")


class RegisterMovementError(ValueError):

    def __init__(self):
        super().__init__("ERROR: Invalid operation code.")


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
    cuenta1.print_movements()


if __name__ == "__main__":
    main()
