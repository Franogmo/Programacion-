"""
Goal of the program: a bank account class
by Fran Ogallas
Starting date: 5th of March 2024. Last version: 11th of March 2024.
"""
from __future__ import annotations
from random import shuffle
from typing import List

from typeguard import typechecked


@typechecked()
class Card:

    def __init__(self, number: str, suit: str):
        self.__number = number
        self.__suit = suit

    @property
    def number(self):
        return self.__number

    @property
    def suit(self):
        return self.__suit

    def __str__(self):
        return f"{self.__number} de {self.__suit}"

    def __repr__(self):
        return f"{self.__number} de {self.__suit}"

    def __eq__(self, other: Card):
        return (self.__number, self.__suit) == (other.__number, other.__suit)

    def __hash__(self):
        return hash(self.__number + self.__suit)


@typechecked
class Deck:

    def __init__(self, cards: List[Card]):
        self.__cards = cards

    @property
    def cards(self):
        return self.__cards.copy()

    def draw(self):
        return self.__cards.pop(0)

    def deal(self, player: CardPlayer, card_amount: int):
        if card_amount < 1:
            raise ValueError("0 or less cards cannot be dealt.")
        if card_amount > len(self.__cards):
            raise ValueError("Drawing from an empty deck is not allowed.")
        for n in range(card_amount):
            player.receive(self.draw())

    def shuffle(self):
        shuffle(self.__cards)

    def __len__(self):
        return len(self.__cards)

    def __str__(self):
        return f"{self.__cards}"


@typechecked()
class CardPlayer:

    def __init__(self, name: str, *cards: Card):
        self.__name = name
        self.__cards = list(cards)

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards

    def draw(self, deck: Deck):
        self.__cards.append(deck.draw())

    def discard(self, card: Card):
        if card not in self.__cards:
            raise ValueError("The card player does not have that card.")
        self.__cards.remove(card)
        return card

    def receive(self, card: Card):
        self.__cards.append(card)


class SpanishDeck(Deck):
    __SPANISH_DECK_NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "sota", "caballo", "rey"]
    __SPANISH_DECK_SUITS = ["bastos", "copas", "espadas", "oros"]

    @classmethod
    def __generate_deck(cls, numbers: List[str], suits: List[str]):
        generated_deck = []
        for n in range(len(suits)):
            for m in range(len(numbers)):
                generated_deck.append(Card(numbers[m], suits[n]))
        shuffle(generated_deck)
        return generated_deck

    def __init__(self):
        super().__init__(SpanishDeck.__generate_deck(SpanishDeck.__SPANISH_DECK_NUMBERS,
                                                     SpanishDeck.__SPANISH_DECK_SUITS))

    @classmethod
    def numbers(cls):
        return cls.__SPANISH_DECK_NUMBERS.copy()

    @classmethod
    def suits(cls):
        return cls.__SPANISH_DECK_SUITS.copy()

    @property
    def cards(self):
        return super().cards


class EnglishDeck(Deck):
    __ENGLISH_DECK_NUMBERS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    __ENGLISH_DECK_SUITS = ["corazones", "picas", "diamantes", "tréboles"]

    @classmethod
    def __generate_deck(cls, numbers: List[str], suits: List[str]):
        generated_deck = []
        for n in range(len(suits)):
            for m in range(len(numbers)):
                generated_deck.append(Card(numbers[m], suits[n]))
        shuffle(generated_deck)
        return generated_deck

    def __init__(self):
        super().__init__(EnglishDeck.__generate_deck(EnglishDeck.__ENGLISH_DECK_NUMBERS,
                                                     EnglishDeck.__ENGLISH_DECK_SUITS))

    @classmethod
    def numbers(cls):
        return cls.__ENGLISH_DECK_NUMBERS.copy()

    @classmethod
    def suits(cls):
        return cls.__ENGLISH_DECK_SUITS.copy()

    @property
    def cards(self):
        return super().cards
