

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
