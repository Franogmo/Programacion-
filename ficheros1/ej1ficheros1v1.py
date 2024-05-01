"""
Goal of the program: Saving a prime number list in a text file.
By Fran Ogallas
Start date: 4th of April 2024. Last version: 4th of April 2024.
"""


def is_prime(number):
    if number - int(number) != 0:
        raise ValueError("is_prime function cannot receive floating numbers.")
    if number < 2:
        return False
    elif number == 2:
        return True
    else:
        half = round(number / 2)
        prime_detection = True
        counter = 2
        while prime_detection and counter <= half:
            tested_number = number / counter
            if tested_number - int(tested_number) == 0:
                prime_detection = False
            counter += 1
        return prime_detection


def main():
    prime_document = open("primedocument.txt", "wt")
    for n in range(501):
        if is_prime(n):
            print(n, file=prime_document)
    prime_document.close()


if __name__ == "__main__":
    main()
