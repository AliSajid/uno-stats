"""
This file tests the cards.
"""

from uno_game import cards
from nose import tools
import itertools

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
    """
    Test class for Uno Card
    """

    def __init__(self):
        self.ALLOWED_COLORS = ["Red", "Blue", "Green", "Yellow", "Black"]
        self.ALLOWED_VALUES = [str(n) for n in range(10)] + ["R", "S", "D"]
        self.CARD_PAIRS = itertools.product(self.ALLOWED_COLORS, self.ALLOWED_VALUES)

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


    def teardown(self):
        """
        Per Instance Tear Down
        :return:
        """
        pass

    def test_card_creation(self):
        """
        Test if the new card is created successfully.
        :return:
        """
        for color, value in self.CARD_PAIRS:
            yield self.check_creation, color, value

    def check_creation(self, col, val):
        """

        :param col:
        :param val:
        :return:
        """
        tools.assert_is_not_none(cards.UnoCard(col, val))

    @tools.raises(ValueError)
    def test_creation_fails_with_invalid_color(self):
        """
        Test creation fails with invalid color
        :return:
        """
        cards.UnoCard("blah", "0")

    @tools.raises(ValueError)
    def test_creation_fails_with_invalid_value(self):
        """
        Test creation fails with invalid value
        :return:
        """
        cards.UnoCard("Blue", "A")

    def test_new_card_color(self):
        """
        Test if the new card returns the correct color.
        :return:
        """
        for color, value in self.CARD_PAIRS:
            yield self.check_color, color, value

    def check_color(self, col, val):
        """
        check if each color and value pair creates correctly
        :param col:
        :param val:
        :return:
        """
        card = cards.UnoCard(col, val)
        tools.assert_equal(card.color, col)

    def test_new_card_value(self):
        """
        Test if new card returns correct value
        :return:
        """
        for color, value in self.CARD_PAIRS:
            yield self.check_value, color, value

    def check_value(self, col, val):
        """
        Check if new card has correct value per card/value pair
        :param col:
        :param val:
        :return:
        """
        card = cards.UnoCard(col, val)
        tools.assert_equal(card.value, val)

    def test_card_equality(self):
        """
        Test if two equal cards are equal
        :return:
        """
        for color, value in self.CARD_PAIRS:
            yield self.check_card_equality, color, value

    def check_card_equality(self, col, val):
        """

        :param col:
        :param val:
        :return:
        """
        card_one = cards.UnoCard(col, val)
        card_two = cards.UnoCard(col, val)
        tools.assert_equal(card_one, card_two)

    def test_card_inequality(self):
        """
        Test if two unequal cards are unequal
        :return:
        """
        for pair_one, pair_two in itertools.product(self.CARD_PAIRS, repeat=2):
            yield self.check_card_inequality, pair_one, pair_two

    def check_card_inequality(self, pair_one, pair_two):
        """

        :param pair_one:
        :param pair_two:
        :return:
        """
        if not(pair_one == pair_two):
            tools.assert_not_equal(cards.UnoCard(*pair_one), cards.UnoCard(*pair_two))

    def test_card_representation(self):
        """

        :return:
        """
        for color, value in self.CARD_PAIRS:
            yield self.check_card_representation, color, value

    def check_card_representation(self, col, val):
        """

        :param col:
        :param val:
        :return:
        """
        card = cards.UnoCard(col, val)
        tools.assert_equal(repr(card), "<Card {} {}>".format(col, val))
