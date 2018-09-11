import random


class Card:

    names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(Card.ranks[self.rank],
                                 Card.names[self.suit])

    def __lt__(self, o):
        if self. suit < o.suit:
            return True
        if self.suit > o.suit:
            return False
        return self.rank < o.rank


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))

        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, c):
        self.cards.append(c)

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self):
        self.cards().sort()


if __name__ == "__main__":
    c1 = Card(1, 13)
    print(c1)

    print('***')

    d1 = Deck()
    print(d1)
