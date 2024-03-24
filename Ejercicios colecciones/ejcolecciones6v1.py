"""
Goal of the program: A program which tells capitals of countries. New countries and capitals can be added.
By Fran Ogallas
Project start date: 16th of March 2024. Last update: 18th of March 2024.
"""
from typeguard import typechecked


class CapitalsMachine:

    def __init__(self):
        self.__capitals = {"España": "Madrid", "Portugal": "Lisboa", "Francia": "París"}

    def __add_capital(self, key, value):
        if key not in self.__capitals:
            self.__capitals[key] = value
        else:
            raise ValueError("the add_capital_city method is not allowed to add existent countries to the database.")

    def interface(self):
        print("Consultor de capitales de países.")
        exit_key = "anything"
        while exit_key != "salir":
            country = input("\nIntroduce el nombre del país del que quieras saber la capital: ")
            if country in self.__capitals:
                print(f"La capital de {country} es {self.__capitals[country]}.")
            else:
                country_addition_key = input("Ese país no está en la base de datos. Introduce X si quieres añadirlo: ")
                if country_addition_key == "x" or country_addition_key == "X":
                    capital = input(f"Introduce la capital de {country}: ")
                    self.__add_capital(country, capital)
                    print("Su capital se ha guardado con éxito.")
            exit_key = input("Introduce la palabra salir para cerrar el programa: ")


def main():
    capital_cities_machine = CapitalCitiesMachine()
    capital_cities_machine.interface()


if __name__ == "__main__":
    main()
