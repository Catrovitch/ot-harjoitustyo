from card import Card
import random

class MasterDeck:

    def __init__(self):

        self.deck = []

    def create_deck(self):
        
        suits = ["hearts", "diamonds", "clubs", "spades"]
        numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14]

        for suit in suits:
            for number in numbers:
                next_card = Card(suit, number)
                self.deck.append(next_card)

        self.deck.append(Card("black-joker", 0))
        self.deck.append(Card("red-joker", 0))

    def scramble(self):

        random.shuffle(self.deck)

    def lay_out_deck(self):

        for card in self.deck:
            print(card.name)

    def draw(self, number_of_cards: int, destination: list):

        if number_of_cards >= len(self.deck):
            number_of_cards = len(self.deck)


        for i in range(0, number_of_cards):
            destination.append(self.deck.pop())


d = MasterDeck()
d.create_deck()
d.lay_out_deck()
print(len(d.deck))