"""

"""

from uno_game import deck
from nose import tools
import random
from collections import deque


class TestDeck:
    """
    This class tests the Deck
    """

    def __init__(self):
        self.one_card_draw = [deck.UnoCard("Black", "Wild")]
        self.two_card_draw = self.one_card_draw + [deck.UnoCard("Yellow", "5")]
        self.four_card_draw = self.two_card_draw + [deck.UnoCard("Green", "0"), deck.UnoCard("Yellow", "2")]
        self.initial_deal = self.four_card_draw + [deck.UnoCard("Yellow", "S"), deck.UnoCard("Blue", "D"),
                                                   deck.UnoCard("Yellow", "7")]

    @classmethod
    def setup_class(cls):
        """
        Per Class Set Up
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
        random.seed(1989)

    def teardown(self):
        """
        Per Instance Tear Down
        :return:
        """
        pass

    def test_init(self):
        """
        Testing the Initialization
        :return:
        """
        d = deck.Deck()
        tools.assert_is_instance(d, deck.Deck)

    def test_length(self):
        """
        Testing if the reported length is correct.
        :return:
        """
        d = deck.Deck()
        tools.assert_equal(len(d), 108)

    def test_draw_one_card(self):
        """
        Testing if a correct number of cards is drawn
        :return:
        """
        d = deck.Deck()
        d.draw_one_card()
        tools.assert_equal(len(d), 107)
        tools.assert_equal(d.remaining_cards(), 107)

    def test_draw_one_card_result(self):
        d = deck.Deck()
        ret = d.draw_one_card()
        tools.assert_list_equal(list(ret), self.one_card_draw)
        tools.assert_is_instance(ret, deque)

    def test_draw_two(self):
        """
        Testing if a correct number of cards is drawn
        :return:
        """
        d = deck.Deck()
        d.draw_two_cards()
        tools.assert_equal(len(d), 106)
        tools.assert_equal(d.remaining_cards(), 106)

    def test_draw_two_cards_result(self):
        d = deck.Deck()
        ret = d.draw_two_cards()
        tools.assert_list_equal(list(ret), self.two_card_draw)
        tools.assert_is_instance(ret, deque)

    def test_initial_deal(self):
        """
        Testing if a correct number of cards is drawn
        :return:
        """
        d = deck.Deck()
        d.initial_deal()
        tools.assert_equal(len(d), 101)
        tools.assert_equal(d.remaining_cards(), 101)

    def test_initial_deal_result(self):
        d = deck.Deck()
        ret = d.initial_deal()
        tools.assert_list_equal(list(ret), self.initial_deal)
        tools.assert_is_instance(ret, deque)

    def test_draw_four(self):
        """
        Testing if a correct number of cards is drawn
        :return:
        """
        d = deck.Deck()
        d.draw_four_cards()
        tools.assert_equal(len(d), 104)
        tools.assert_equal(d.remaining_cards(), 104)

    def test_draw_four_cards_result(self):
        d = deck.Deck()
        ret = d.draw_four_cards()
        tools.assert_list_equal(list(ret), self.four_card_draw)
        tools.assert_is_instance(ret, deque)

    def test_remaining_cards(self):
        """
        Testing if a correct number of remaining cards is reported
        :return:
        """
        d = deck.Deck()
        d.draw_four_cards()
        tools.assert_equal(d.remaining_cards(), 104)
