"""
Goal of the program: A Spanish to English short translation game
By Fran Ogallas
Project start date: 15th of March 2024. Last update: 18th of March 2024.
"""
from ejcolecciones3v1 import TouristMiniDictionary
from random import randint
from random import choice


def main():
    dictionary = TouristMiniDictionary()
    terms = list(dictionary.words.keys())
    chosen_terms = set()
    while len(chosen_terms) < 5:
        chosen_terms.add(choice(terms))
    chosen_terms = list(chosen_terms)
    print("Juego de traducir términos al inglés\n")
    right_answers = 0
    wrong_answers = 0
    for n in range(len(chosen_terms)):
        answer = input(f"¿Cómo se dice {chosen_terms[n]} en inglés?: ")
        if answer == dictionary.words[chosen_terms[n]]:
            print("¡Correcto!\n")
            right_answers += 1
        else:
            print(f"Incorrecto. La respuesta correcta era {dictionary.words[chosen_terms[n]]}\n")
            wrong_answers += 1
    print(f"Fin del juego.\n Respuestas correctas: {right_answers}\n Respuestas incorrectas: {wrong_answers}\n")


if __name__ == "__main__":
    main()
