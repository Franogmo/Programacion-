"""
Goal of the program: Inputting a .java through cmd and returning a copy of it without comments.
By Fran Ogallas
Starting date: 8th of April 2024. Current version: 10th of April 2024.
"""
import sys
from typeguard import typechecked

"""
Comments in java:
Single line // . Multiline /*  */
"""


def basic_validator(full_text):
    if len(full_text) <= 2:
        raise ValueError("This is not a valid .java")
    return full_text


@typechecked
def tab_remover(line: str):
    line_copy = line
    clean_line = ""
    while len(line_copy) > 3 and line_copy[0:4] == "    ":
        clean_line = ""
        for n in range(len(line_copy)):
            if n > 3:
                clean_line += line_copy[n]
        line_copy = clean_line
    return clean_line


@typechecked
def remove_single_comment(line: str):
    for n in range(len(line)):
        if line[n] == "/" and n < (len(line) - 1) and line[n + 1] == "/":
            if tab_remover(line[:n]) == "":
                return ""
            return line[:n]
    return line


@typechecked
def purge_single_comments(text_list: list):
    final_text = ""
    for n in range(len(text_list)):
        current_line = remove_single_comment(text_list[n])
        if n == (len(text_list) - 1):
            final_text += current_line
        elif n != (len(text_list) - 1) and current_line != "":
            final_text += current_line + "\n"
    return final_text


@typechecked
def remove_multiline_comments(full_text: str):  # This should be cleaned up.
    modified_text = full_text
    pointer = 0
    open_key_place = None
    while True:  # This detects /* and */ and deletes anything inbetween.
        if modified_text[pointer] + modified_text[(pointer + 1)] == "/*":
            open_key_place = pointer
            pointer += 1
        if open_key_place is not None and (modified_text[pointer] + modified_text[(pointer + 1)] == "*/"):
            if (pointer + 1) == (len(modified_text) - 1):
                modified_text = modified_text[:open_key_place]
                open_key_place -= 1
            else:
                modified_text = modified_text[:open_key_place] + modified_text[(pointer + 2):]
            pointer = open_key_place - 1
            open_key_place = None
        pointer += 1
        if pointer == len(modified_text) - 1:
            break
    return modified_text


def is_java(filename):
    return ((len(filename) > 5) and (filename[(len(filename) - 5):] == ".java"))


def main():
    try:
        java_program_name = sys.argv[1]
        java_clean_program_name = sys.argv[2]
        if not is_java(java_program_name) or not is_java(java_clean_program_name):
            raise ValueError("ERROR: No se han introducido .java's")
        try:
            with open(java_program_name, "rt", encoding="utf8") as java_program:
                java_full_text = basic_validator(java_program.read())
                java_full_text = remove_multiline_comments(java_full_text)
                java_content = purge_single_comments(java_full_text.split("\n"))
        except FileNotFoundError:
            print(f"No se ha encontrado ningún fichero {java_program_name} en este archivo.")
            exit(0)
        with open(java_clean_program_name, "wt", encoding="utf8") as output_program:
            print(java_content, file=output_program)
    except IndexError:
        print("ERROR: No se han introducido bien los comandos.")


if __name__ == "__main__":
    main()

