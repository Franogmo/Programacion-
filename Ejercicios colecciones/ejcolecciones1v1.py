"""
Goal of the program: Password control device made with a dictionary
By Fran Ogallas
Project start date: 15th of March 2024. Last update: 15th of March 2024.
"""


class PasswordControl:

    def __init__(self):
        self.__passwords = {"Puma": "12345", "Jellyfish": "67890", "Bear": "01020", "Amoeba": "42069"}

    def access(self):
        username = input("Introduce tu nombre de usuario: ")
        if username not in self.__passwords:
            raise ValueError("This user is not registered.")
        mistakes = 0
        while True:
            input_password = input("Introduce tu contraseña: ")
            if self.__passwords[username] == input_password:
                print("Ha accedido al área restringida")
                break
            elif mistakes >= 3:
                print("Lo siento, no tiene acceso al área restringida")
                break
            else:
                print("Contraseña incorrecta.")


def main():
    password_control = PasswordControl()
    password_control.access()


if __name__ == "__main__":
    main()
