"""
Goal of the program: terminal class
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""
from __future__ import annotations
from typeguard import typechecked

PHONE_NUMBER_LENGTH = 9

@typechecked
class Terminal:
    __numbers_register = []

    def __init__(self, number: str):
        if not Terminal.__validate_phone_number(number):
            raise ValueError("El número de teléfono es erróneo")
        if number in Terminal.__numbers_register:
            raise ValueError("El número de teléfono ya ha sido dado de alta")
        Terminal.__numbers_register.append(number)
        self.__number = number
        self.__talk_time = 0

    @property
    def number(self):
        return self.__number[:3] + " " + self.__number[3:5] + " " + self.__number[5:7] + " " + self.__number[7:9]

    @property
    def talk_time(self):
        return self.__talk_time

    def call(self, other: Terminal, seconds: int):
        if seconds < 0:
            raise ValueError("El tiempo de conversación no puede ser negativo")
        if other.number == self.number:
            raise ValueError("Un teléfono no se puede llamar a sí mismo")
        self.__talk_time += seconds
        other.__talk_time += seconds

    def __str__(self):
        return f"Nº {self.number} - {self.__talk_time}s de conversación"

    @staticmethod
    def __validate_phone_number(number: str):
        return len(number) == PHONE_NUMBER_LENGTH and number[0] in "967" and number.isdigit()


def main():
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)


if __name__ == "__main__":
    main()