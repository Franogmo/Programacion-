"""
Goal of the program: 20 words long Spanish-English dictionary for tourism-related terms
By Fran Ogallas
Project start date: 15th of March 2024. Last update: 15th of March 2024.
"""


class TouristMiniDictionary:

    def __init__(self):
        self.__words = {"Museo": "Museum", "Avión": "Plane", "Barco": "Boat", "Propina": "Tip", "Ducha": "Shower",
                        "Habitación": "Room", "Queja": "Complaint", "Devolución": "Refund", "Iglesia": "Church",
                        "Plaza": "Square", "Fiesta": "Party", "Bebida": "Drink", "Comida": "Food", "Dinero": "Money",
                        "Equipaje": "Luggage", "Playa": "Beach", "Montaña": "Mountain", "Cama": "Bed",
                        "País": "Country", "Clima": "Weather"}

    @property
    def words(self):
        return self.__words.copy()

    def translate(self, word):
        if word not in self.__words:
            raise ValueError("Palabra no registrada.")
        else:
            return str(self.__words[word])

    def menu(self):
        print("Traductor turístico de bolsillo Español-Inglés:\n")
        while True:
            word = input("Introduce una palabra en español para ver su traducción al "
                         "inglés (Primera letra en mayúscula): ")
            if word not in self.__words:
                exit_key = input("Esta palabra no está en el diccionario. Introduce X si quieres intentarlo con otra: ")
                if exit_key != "x" and exit_key != "X":
                    break
            else:
                print(f"{word} = {self.translate(word)}")
                break


def main():
    dictionary = TouristMiniDictionary()
    dictionary.menu()
    print("Test del método translate de la clase TouristMiniDictionary. Devolución = " +
          dictionary.translate("Devolución"))
    try:
        print(dictionary.translate("Baldosa"))
        raise SyntaxError
    except ValueError:
        print("El programa funciona bien.")


if __name__ == "__main__":
    main()
