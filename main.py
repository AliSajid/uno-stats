# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:28:44 2017

@author: ASIma
"""
import random
from collections import deque




class Deck:
    def __init__(self):
        self.deck = deque()
        self.suits = ["Red", "Green", "Blue", "Yellow"]
        self.vals = [str(n + 1) for n in range(9)] + ["R", "S", "D"]
        self.wilds = ["Black"]
        self.wild_vals = ["Wild", "Wild Draw Four"]
        self.populate_deck()
        self.shuffle()

    def __repr__(self):
        print("Total Cards: 108")
        print("Remaining Cards: {}".format(self.remaining_cards()))
        print("Order of Cards:")
        return str(self.deck)

    def populate_deck(self):
        regulars = [Card(s, v) for s in self.suits for v in self.vals for _ in range(2)]
        wilds = [Card(s, v) for s in self.wilds for v in self.wild_vals for _ in range(4)]
        zeros = [Card(s, '0') for s in self.suits]
        total = regulars + wilds + zeros
        for c in total:
            self.deck.append(c)

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_n(self, num):
        return [self.deck.popleft() for _ in range(num)]

    def initial_deal(self):
        return self.draw_n(7)

    def draw_one_card(self):
        return self.draw_n(1)

    def draw_two(self):
        return self.draw_n(2)

    def draw_four(self):
        return self.draw_n(4)

    def remaining_cards(self):
        return len(self.deck)


class Hand:
    def __init__(self, player_id, Deck):
        self.hand = Deck.initial_deal()
        self.player_id = player_id

    def __repr__(self):
        return "<Hand {}>".format(str(self.hand))

    def set_opening_hand(self, opening_hand):
        self.hand = opening_hand

    def draw_cards(self, cards):
        self.hand.extend(cards)

    def cards_of_color(self, color):
        return [c for c in self.hand if c.color == color]

    def cards_of_value(self, value):
        return [c for c in self.hand if c.value == value]

    def red_cards(self):
        return self.cards_of_color("Red")

    def yellow_cards(self):
        return self.cards_of_color("Yellow")

    def green_cards(self):
        return self.cards_of_color("Green")

    def blue_cards(self):
        return self.cards_of_color("Blue")

    def black_cards(self):
        return self.cards_of_color("Black")

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)


class Game:
    def __init__(self, number_players):
        self.deck = Deck()
        self.players = [Hand(i, self.deck) for i in range(number_players)]
        self.rotation = 'ascending'
        self.player_turn = 0

    def __repr__(self):
        return "<Ono Game: Players: {}, Turn Order: {}, Current Turn: {}>".format(len(self.players),
                                                                                  self.rotation.capitalize(),
                                                                                  self.player_turn)

    def take_turn(self, player_turn):
        pass
