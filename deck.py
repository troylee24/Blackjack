from card import Card
import random

class Deck:
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self) -> None:
        self.cards = []

        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(suit, rank))

        self.i = 0

    def shuffle(self) -> None:
        self.i = 0
        random.shuffle(self.cards)
    
    def draw(self) -> None:
        card = self.cards[self.i]
        self.i += 1
        return card

    def __str__(self) -> str:
        return " ".join(str(card) for card in self.cards)