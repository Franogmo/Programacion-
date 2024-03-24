"""
Goal of the program: Program to generate 10 different spanish deck cards
By Fran Ogallas
Project start date: 15th of March 2024. Last update: 15th of March 2024.
"""
from pootanda3ej14v4 import SpanishDeck
from random import randint


class ImmutableSpanishDeck(SpanishDeck):

    def __init__(self):
        super().__init__()

    def duplicate_random_existing_card(self):
        return super().cards[randint(0, (len(super().cards) - 1))]


ten_random_cards = set()
deck = ImmutableSpanishDeck()

while len(ten_random_cards) < 10:
    card = deck.duplicate_random_existing_card()
    ten_random_cards.add(card)

ten_random_cards = list(ten_random_cards)
cards_ordered_by_suit = [[], [], [], []]  # In this order: clubs - cups - swords - coins.


for n in range(len(ten_random_cards)):
    if ten_random_cards[n].suit == "bastos":
        cards_ordered_by_suit[0].append(ten_random_cards[n])
    elif ten_random_cards[n].suit == "copas":
        cards_ordered_by_suit[1].append(ten_random_cards[n])
    elif ten_random_cards[n].suit == "espadas":
        cards_ordered_by_suit[2].append(ten_random_cards[n])
    elif ten_random_cards[n].suit == "oros":
        cards_ordered_by_suit[3].append(ten_random_cards[n])

aux_dict = {}

for n in range(len(cards_ordered_by_suit)):
    aux_dict[n] = {}
    counter = -1
    while len(cards_ordered_by_suit[n]) > 0:
        counter += 1
        if SpanishDeck.numbers()[counter] == cards_ordered_by_suit[n][-1].number:
            x = cards_ordered_by_suit[n].pop(-1)
            aux_dict[n][counter] = x
            counter = -1

    aux_dict[n] = dict(sorted(aux_dict[n].items()))
    aux_dict[n] = list(aux_dict[n].values())

cards_ordered_by_suit = list(aux_dict.values())
output_cards = []

for n in range(len(cards_ordered_by_suit)):
    output_cards.extend(cards_ordered_by_suit[n])

print(output_cards)
