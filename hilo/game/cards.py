from random import Random, random


class Cards:
    """ one of 52 playing card with one side displaying the numbers 2 through 10, Jack, Queen, King, Ace  and it's suite, Spades, Clubs, Diamonds
            and hearts and the other side a generic design.
    The responsibility of Card is to display its value 1-13
   
    Attributes:
        value (int): The number on the card.
    """

    def __init__(self, value):
        """Constructs a new instance of Die with a value and points attribute.
        Args:
            self (Card): An instance of Card.
        """
        self.value = value

        """Generates a new random value.
        
        Args:
            self (Card): An instance of Card
        """
    def reveal(self):
        self.value = self.value

"""
There are 52 cards in a deck, four suits of 13 valued cards
"""