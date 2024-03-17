"""
Goal of the program: Menu for dates management.
by Fran Ogallas
Development start date: 5th of February 2024. Last modification date: 12th of February 2024.
"""

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


