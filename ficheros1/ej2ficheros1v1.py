"""
Goal of the program: Displaying a prime number list from a text file.
By Fran Ogallas
Start date: 4th of April 2024. Last version: 4th of April 2024.
"""


def main():
    """
    Reads txt.
    """
    prime_list = open("primedocument.txt", "rt")
    current_line = prime_list.readline()
    while current_line != "":
        print(current_line, end="")
        current_line = prime_list.readline()
    prime_list.close()


if __name__ == "__main__":
    main()
