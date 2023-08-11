import random

deck_symbols = {
    'HEARTS': '♥',
    'DIAMONDS': '♦',
    'CLUBS': '♣',
    'SPADES': '♠'
}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f' {self.rank} of {self.suit}'

    def card_shape(self):
        shape_text = f"""
                ┌─────────┐
                │{deck_symbols[self.suit]:<9}│
                │         │
                │         │
                │    {self.rank:<2}   │
                │         │
                │         │
                │{deck_symbols[self.suit]:>9}│
                └─────────┘
"""
        print(shape_text)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ('HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES'):
            for rank in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return None
        else:
            return self.cards.pop()

    def reset(self):
        self.__init__()

my_deck = Deck()

for i in range(5):
    my_card = my_deck.draw()

    print(my_card)
    my_card.card_shape()

a=input("sds")

