"""
Goal of the program: Mixing two .txts input through cmd.
By Fran Ogallas
Starting date: 9th of April 2024. Current version: 9th of April 2024.
"""
import sys
from typeguard import typechecked


@typechecked()
def mix_test_lists(text1: list, text2: list):
    final_text = []
    for n in range(max(len(text1), len(text2))):
        if n < len(text1):
            final_text.append(text1[n])
        if n < len(text2):
            final_text.append(text2[n])
    return final_text


def main():
    try:
        text1_name = sys.argv[1]
        text2_name = sys.argv[2]
        with open(text1_name, "rt", encoding="utf8") as text1:
            text1_lines = text1.readlines()
        with open(text2_name, "rt", encoding="utf8") as text2:
            text2_lines = text2.readlines()
        mixed_text = mix_test_lists(text1_lines, text2_lines)
        existing_copies = 1
        try:
            with open("mixedtext.txt", "xt", encoding="utf8") as final_text:
                for n in range(len(mixed_text)):
                    print(mixed_text[n], file=final_text)
        except FileExistsError:
            while True:
                existing_copies += 1
                try:
                    with open(f"mixedtext{existing_copies}.txt", "xt", encoding="utf8") as final_text:
                        for n in range(len(mixed_text)):
                            print(mixed_text[n], file=final_text)
                    existing_copies = 1
                    break
                except FileExistsError:
                    pass
    except IndexError:
        print("ERROR: No se han introducido bien los comandos.")


if __name__ == "__main__":
    main()
