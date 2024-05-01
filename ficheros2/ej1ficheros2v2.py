"""
Goal of the program: Returning a .txt with the sorted words of another one input by cmd.
By Fran Ogallas
Starting date: 8th of April 2024. Current version: 9th of April 2024.
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


def order_words(text_list):
    words_dict = {}
    for n in range(len(text_list)):
        words_dict[text_list[n].upper()] = text_list[n]
    words_dict = list((dict(sorted(words_dict.items()))).values())
    return words_dict


def remove_txt(text):
    return text[:(len(text) - 4)]


def main():
    try:
        input_document = sys.argv[1]
        document_content = []
        source_document = open(input_document, "rt", encoding="utf8")
        print(f"contenido del documento {input_document}: ")
        document_content = order_words(separate_words(source_document.read()))
        source_document.close()
        sorted_document = open(f"{remove_txt(input_document)}-sort.txt", "wt")
        for n in range(len(document_content)):
            print(document_content[n], file=sorted_document)
        sorted_document.close()
    except IndexError:
        print("ERROR: No se han introducido bien los comandos.")


if __name__ == "__main__":
    main()
