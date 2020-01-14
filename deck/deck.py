import random


class Deck:
    Colors = ["yellow", "red", "green", "blue"]
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # fills the deck and shuffles it
    def __init__(self):
        self.deck = []
        for color in self.Colors:
            for number in self.Numbers:
                self.deck.append([color, number])  # each card has a color and a number
        self.shuffle()

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    #
    def deal(self):
        return next(self)

    def iteration(self):
        for card in self.deck[::-1]:
            print(next(self))

    def __iter__(self):
        return iter(self.deck)

    def __next__(self):
        if len(self.deck):  # if the deck contains cards
            card = self.deck[-1]
            del self.deck[-1]
            return card
        else:
            raise StopIteration("Deck is empty!")

    def __bool__(self):
        if self.deck:
            return True
        else:
            return False

def deal_if_not_empty(mydeck):
    if mydeck:
        print(mydeck.deal())
    else:
        print( "the deck is empty" )

if __name__ == "__main__":
    deck = Deck()
    deal_if_not_empty(deck)
    deal_if_not_empty(deck)
    deal_if_not_empty(deck)
    deck.iteration()
    deal_if_not_empty(deck)


    # print(deck.iteration())
