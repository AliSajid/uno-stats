"""
This file tests the cards.
"""

from uno_game import cards
from nose import tools

class TestCard:

    @classmethod
    def setup_class(cls):
        """
        Per Instance Set Up
        :return:
        """
        pass

    @classmethod
    def teardown_class(cls):
        """
        Per Class Tear Down
        :return:
        """
        pass

    def setup(self):
        """
        Per Instance Set Up
        :return:
        """
        pass

    def teardown(self):
        """
        Per Instance Tear Down
        :return:
        """
        pass

    def test_new_card_color(self):
        """
        Test if the new card returns the correct color.
        :return:
        """
        card = cards.Card("Red", "1")
        tools.assert_equal(card.color, "Red")

    def test_new_card_value(self):
        """
        Test if new card returns correct value
        :return:
        """
        card = cards.Card("Red", "0")
        tools.assert_equal(card.value, "0")

    def test_card_equality(self):
        """
        Test if two equal cards are equal
        :return:
        """
        card_1 = cards.Card("Red", "1")
        card_2 = cards.Card("Red", "1")
        tools.assert_equal(card_1, card_2)

    def test_card_inequality(self):
        """
        Test if two unequal cards are unequal
        :return:
        """
        card_1 = cards.Card("Red", "1")
        card_2 = cards.Card("Red", "0")
        tools.assert_not_equal(card_1, card_2)

    def test_card_representation(self):
        card = cards.Card("Red", "1")
        tools.assert_equal(repr(card), "<Card Red 1>")

class TestUnoCard:
    pass