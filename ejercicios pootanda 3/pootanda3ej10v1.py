"""
Goal of the program: Several different vehicles class inheriting from an abstract class vehicle.
by Fran Ogallas
Starting date: 26th of February 2024. Last version: 26th of February 2024.
"""

from abc import ABC
from random import randint
from typeguard import typechecked


@typechecked
class Vehicle(ABC):

    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0.0
        Vehicle.__vehicles_created += 1

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

    def travel(self, distance: float):
        if distance < 0:
            raise ValueError("Distance cannot be a negative number.")
        Vehicle.__total_kilometers += distance
        self.__kilometers_traveled += distance

    def __repr__(self):
        return f"{self.__class__.__name__} [kilometers_traveled={self.__kilometers_traveled}]"


class Bike(Vehicle):

    def __init__(self):
        super().__init__()

    def do_wheelie(self):
        return f"[Y la bicicleta en cuestión efectuó un caballito.]"

    def travel(self):
        advanced_kilometers = randint(0, 500)
        super().travel(advanced_kilometers)
        return f"La bicicleta ha recorrido {advanced_kilometers} kilómetros."


class Car(Vehicle):

    def __init__(self):
        super().__init__()
        self.__gasoline = 0

    @property
    def gasoline(self):
        return self.__gasoline

    def burnout(self):
        if self.__gasoline < 1:
            return "No hay gasolina suficiente para quemar rueda"
        else:
            self.__gasoline -= 1
            return "Algunos lo llaman horterada. Yo lo llamo cultivar microplásticos."

    def fuel_up(self):
        self.__gasoline = 50

    def travel(self):
        if self.__gasoline <= 0:
            return "No se puede viajar. El depósito está vacío."
        else:
            advanced_kilometers = randint(0, (self.__gasoline * 10))
            self.__gasoline -= (advanced_kilometers // 10)
            super().travel(advanced_kilometers)
            return f"El coche ha recorrido {advanced_kilometers} kilómetros."


class Menu:

    def __init__(self, *options, title="Menú principal"):
        self.__options = list(options)
        self.__title = title

    @property
    def last_option(self):
        return len(self.__options)

    def choose(self):
        self.__print_menu()
        return self.__chosen_option()

    def __print_menu(self):
        print(self.__title)
        print("-" * len(self.__title))
        for n in range(len(self.__options)):
            print(f"{n + 1}. {self.__options[n]}")

    def __chosen_option(self):
        while True:
            picked_option = int(input("\nIntroduzca una opción: "))
            if 1 <= picked_option <= len(self.__options):
                return picked_option
            print("Ha introducido una opción incorrecta.")


def main():
    bike1 = Bike()
    car1 = Car()
    menu = Menu("Anda con la bicicleta", "Haz el caballito con la bicicleta", "Anda con el coche",
                "Quema rueda con el coche", "Llena el depósito del coche", "Ver kilometraje de la bicicleta",
                "Ver kilometraje del coche", "Ver el combustible que queda en el depósito del coche",
                "Ver kilometraje total", "Salir")
    while True:
        option = menu.choose()
        if option == 1:
            print(bike1.travel())
        elif option == 2:
            print(bike1.do_wheelie())
        elif option == 3:
            print(car1.travel())
        elif option == 4:
            print(car1.burnout())
        elif option == 5:
            car1.fuel_up()
            print(f"El coche tiene ahora el depósito lleno.")
        elif option == 6:
            print(f"Bicicleta: {bike1.kilometers_traveled}km")
        elif option == 7:
            print(f"Coche: {car1.kilometers_traveled}km")
        elif option == 8:
            print(f"{car1.gasoline} litros")
        elif option == 9:
            print(f"{Vehicle.total_kilometers()}km recorridos en total.")
        elif option == 10:
            break
        else:
            print("ERROR. Opción no aceptada. Volviendo al menú principal...")
    input()


if __name__ == "__main__":
    main()
