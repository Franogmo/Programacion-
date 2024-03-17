"""
Goal of the program: Program that handles fractions. These fractions are objects.
by Fran Ogallas
Development start date: 3rd of February 2024. Last modification date: 4th of February 2024.
"""
from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise ValueError("Has generado un componente de la fracción no entero.")
        elif denominator == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        else:
            gcdivisor = gcd(numerator, denominator)
            self.__numerator = numerator // gcdivisor
            self.__denominator = denominator // gcdivisor

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def result_fraction(self):
        return self.__numerator / self.__denominator

    def __mul__(self, other):
        if type(other) == Fraction:
            return Fraction((self.__numerator * other.__numerator), (self.__denominator * other.__denominator))
        elif type(other) == int:
            return Fraction((self.__numerator * other), self.__denominator)
        else:
            raise TypeError("A fraction can only be multiplied by other fractions or by numbers.")

    def __neg__(self):
        return self * -1

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) == Fraction:
            return Fraction((self.__numerator * other.__denominator), (self.__denominator * other.__numerator))

    def __add__(self, other):
        if type(other) == Fraction:
            if self.__denominator == other.__denominator:
                return Fraction((self.__numerator + other.__numerator), self.__denominator)
            elif self.__denominator != other.__denominator:
                new_num1 = self.__numerator * other.__denominator
                new_num2 = other.__numerator * self.__denominator
                return Fraction((new_num1 + new_num2), (self.__denominator * other.__denominator))

    def __sub__(self, other):
        if type(other) == Fraction:
            return self + (-other)

    def __eq__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() == other.result_fraction():
                return True
            else:
                return False
        else:
            raise TypeError

    def __ne__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() != other.result_fraction():
                return True
            else:
                return False
        else:
            raise TypeError

    def __lt__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() < other.result_fraction():
                return True
            else:
                return False

    def __le__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() <= other.result_fraction():
                return True
            else:
                return False

    def __gt__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() > other.result_fraction():
                return True
            else:
                return False

    def __ge__(self, other):
        if type(other) == Fraction:
            if self.result_fraction() >= other.result_fraction():
                return True
            else:
                return False


    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"



def main():
    fraction_1 = Fraction(1, 2)
    fraction_2 = Fraction(12, 3)
    print(f"Fracción 1: {fraction_1} --- {fraction_1.result_fraction()}")
    print(f"Fracción 2: {fraction_2} --- {fraction_2.result_fraction()}")
    print(f"Resultado de multiplicarlas: {fraction_1 * fraction_2}")
    print(f"Resultado de dividirlas: {fraction_1 / fraction_2}")
    print(f"Resultado de sumarlas: {fraction_1 + fraction_2}")
    print(f"Resultado de restarlas: {fraction_1 - fraction_2}")
    print(f"¿f1 == f2?: {fraction_1 == fraction_2}")
    print(f"¿f1 != f2?: {fraction_1 != fraction_2}")
    print(f"¿f1 < f2?: {fraction_1 < fraction_2}")
    print(f"¿f1 <= f2?: {fraction_1 <= fraction_2}")
    print(f"¿f1 > f2?: {fraction_1 > fraction_2}")
    print(f"¿f1 >= f2?: {fraction_1 >= fraction_2}")




if __name__ == "__main__":
    main()
