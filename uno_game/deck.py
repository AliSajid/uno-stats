"""

"""
from collections import deque
from uno_game.cards import UnoCard
import random


class Deck:
    def __init__(self):
        self.deck = deque()
        self.suits = ["Red", "Green", "Blue", "Yellow"]
        self.vals = [str(n) for n in range(1, 10)] + ["R", "S", "D"]
        self.wilds = ["Black"]
        self.wild_vals = ["Wild", "Wild Draw Four"]
        self.total_cards = 108
        self.populate_deck()
        self.shuffle()

    def __repr__(self):
        print("Total Cards: {}".format(self.total_cards))
        print("Remaining Cards: {}".format(self.remaining_cards()))
        print("Order of Cards:")
        return str(self.deck)

    def __len__(self):
        return self.remaining_cards()

    def __eq__(self, other):
        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.deck == other.deck
            else:
                return False

    def populate_deck(self):
        regulars = [UnoCard(suit, value) for suit in self.suits for value in self.vals for _ in range(2)]
        wilds = [UnoCard(suit, value) for suit in self.wilds for value in self.wild_vals for _ in range(4)]
        zeros = [UnoCard(suit, '0') for suit in self.suits]
        total = regulars + wilds + zeros
        for c in total:
            self.deck.append(c)

    def shuffle(self):
        random.shuffle(self.deck)

    def __draw_n(self, num):
        return deque([self.deck.popleft() for _ in range(num)])

    def initial_deal(self):
        return self.__draw_n(7)

    def draw_one_card(self):
        return self.__draw_n(1)

    def draw_two_cards(self):
        return self.__draw_n(2)

    def draw_four_cards(self):
        return self.__draw_n(4)

    def remaining_cards(self):
        return len(self.deck)
