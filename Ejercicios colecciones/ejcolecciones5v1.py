"""
Goal of the program: A program that generates 5 different Spanish cards and adds their values (Brisca points system)
By Fran Ogallas
Project start date: 15th of March 2024. Last update: 18th of March 2024.
"""
from pootanda3ej14v4 import SpanishDeck
from pootanda3ej14v4 import Card
from random import randint


def main():
    random_cards = set()
    deck = SpanishDeck()

    while len(random_cards) < 5:
        card1 = deck.cards[randint(0, (len(deck.cards) - 1))]
        random_cards.add(card1)
    random_cards = list(random_cards)
    cards_points = {"1": 11, "3": 10, "rey": 4, "caballo": 3, "sota": 2}
    total_points = 0

    for n in range(len(random_cards)):
        if random_cards[n].number in cards_points:
            total_points += cards_points[random_cards[n].number]

    print(f"Cartas elegidas: {random_cards}")
    print(f"Puntos totales: {total_points}")


if __name__ == "__main__":
    main()
