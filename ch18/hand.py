from cards import Card, Deck


class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == "__main__":
    print(Hand("A hand"))
