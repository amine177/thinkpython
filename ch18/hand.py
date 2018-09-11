from cards import Card, Deck


class Hand(Deck):

    def __init__(self, label=''):
        self.cards = []
        self.label = label


if __name__ == "__main__":
    d = Deck()
    d.shuffle()
    h = Hand("Jack playing")
    h.add_card(d.pop_card())
    print(h)
