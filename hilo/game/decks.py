import random
from game.cards import Cards

class Deck:
    def __init__(self):
        self.cards =[]
        # self.open_deck()
        # self.shuffle()
    
    def open_deck(self):
        for j in range(1,5):
            for i in range(1,14):
                self.cards.append(Cards(i))

    def display_next_card(self, position):
        return self.cards[position].value


    def shuffle(self, times_to_shuffle):
        for i in range(times_to_shuffle):
            random.shuffle(self.cards)