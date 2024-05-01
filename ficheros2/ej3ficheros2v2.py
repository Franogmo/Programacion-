"""
Goal of the program: Counting the words of a text file through cmd.
By Fran Ogallas
Starting date: 9th of April 2024. Current version: 9th of April 2024.
"""
import sys


def separate_words(text):
    words_list = []
    word = ""
    for n in range(len(text)):
        if not (text[n].isalpha() or text[n] == "ñ" or text[n] == "Ñ") and word != "":
            words_list.append(word)
            word = ""
        elif text[n].isalpha() or text[n] == "ñ" or text[n] == "Ñ":
            word += text[n]
    return words_list


def word_counter(text_list, given_word):
    appearances = 0
    for n in range(len(text_list)):
        if text_list[n].upper() == given_word.upper():
            appearances += 1
    return appearances


def main():
    try:
        document_name = sys.argv[1]
        word_to_search = sys.argv[2]
        with open(document_name, "rt", encoding="utf8") as document:
            document_content = document.read()
            word_count = word_counter(separate_words(document_content), word_to_search)
            print(f"La palabra -{word_to_search}- se repite {word_count} veces en el documento {document_name}")
    except IndexError:
        print("ERROR: No se han introducido bien los comandos.")


if __name__ == "__main__":
    main()
