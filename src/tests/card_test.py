import unittest
from services.card import Card


class TestCard(unittest.TestCase):

    def setUp(self):

        pass

    def test_constructor_suit(self):

        test_card = Card("hearts", 2)

        test_card_suit = test_card.suit

        self.assertEqual(test_card_suit, "hearts")

    def test_constructor_number(self):

        test_card = Card("hearts", 2)

        test_card_number = test_card.number

        self.assertEqual(test_card_number, 2)

    def test_constructor_name(self):

        test_card = Card("hearts", 2)

        test_card_name = test_card.name

        self.assertEqual(test_card_name, "2_of_hearts")
