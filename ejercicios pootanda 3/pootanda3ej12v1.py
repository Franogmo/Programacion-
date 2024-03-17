"""
Goal of the program: a mobile class, a daughter of the previous terminal class
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""

from pootanda3ej11v1 import Terminal

class Mobile(Terminal):

    __RATA_FARE = 0.06
    __MONO_FARE = 0.12
    __BISONTE_FARE = 0.3
    __FARES_NAMES = ["rata", "mono", "bisonte"]

    def __init__(self, number, fare):
        super().__init__(number)
        if self.check_fare(fare):
            self.__fare = fare
        else:
            raise ValueError("Invalid fare.")
        self.__bill = 0.00

    @staticmethod
    def check_fare(fare: str):
        return fare in Mobile.__FARES_NAMES

    @property
    def fare(self):
        return self.__fare

    @property
    def bill(self):
        return self.__bill

    @property
    def fare_cost(self):
        if self.__fare == "rata":
            return Mobile.__RATA_FARE
        elif self.__fare == "mono":
            return Mobile.__MONO_FARE
        elif self.__fare == "bisonte":
            return Mobile.__BISONTE_FARE

    def call(self, other: Terminal, seconds: int):
        super().call(other, seconds)
        self.__bill += (seconds / 60) * self.fare_cost

    def __str__(self):
        return super().__str__() + f" - tarificados {round(self.bill, 2)} euros"

def main():
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)


if __name__ == "__main__":
    main()





