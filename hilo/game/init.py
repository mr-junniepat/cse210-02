"""
The game package contains the classes for playing Hilo.
"""

import random
from game.decks import Deck
from game.player import Player

class CardSharer:

    def __init__(self):
        self.play_continues = True
        self.player = Player()
        self.deck = Deck()
        self.current_card_index = 0
        self.hilo = ''



    def start_game(self):
        print()
        print('Welcome to the HiLo Games, Hope we excite you!')
        self.deck.open_deck()
        self.deck.shuffle(random.randint(2,5))
        while self.play_continues:
            print()
            self.show_card(1)
            self.ask_hilo()
            self.show_card(2)
            self.determine_results()
            self.show_player_score()
            self.determine_if_play_continues()
            self.shuffle_if_needed()
        print('Thanks for playing this HiLo Game!')
        print()

    def show_card(self, position):
        if position == 1:
            print(f'The first card is a {self.deck.display_next_card(self.current_card_index)}')
            self.current_card_index += 1
        if position == 2:
            print(f'The second card is a {self.deck.display_next_card(self.current_card_index)}')

    def ask_hilo(self):
        valid_input = False
        while not valid_input:
            self.hilo = input(f'Do you think the next card is higher or lower than the first card? [h/l] ').lower()
            if self.hilo == 'h' or self.hilo == 'l':
                valid_input = True
            else:
                print('I didn\'t get that.')
                print('Try typing a \'l\' for lower and \'h\' for higher.')
    
    def determine_results(self):
        if self.hilo == 'h' and \
                    self.deck.display_next_card(self.current_card_index) > self.deck.display_next_card(self.current_card_index - 1)\
                or self.hilo == 'l' and \
                    self.deck.display_next_card(self.current_card_index) < self.deck.display_next_card(self.current_card_index - 1):
            self.player.scoretaken += 100
            print('That\'s 100 extra points in your pocket!')
        else:
            self.player.scoretaken -= 75
            print('Oh, so sorry. That\'ll subtract 75 points from your score')

    def show_player_score(self):
        print(f'You currently have {self.player.scoretaken} points.')
    
    def determine_if_play_continues(self):
        if self.player.scoretaken >= 0:
            valid_response = False
            while not valid_response:
                response = input('Would you like to continue? [y/n]! ').lower()
                if response == 'y' or response == 'n':
                    valid_response = True
                    if response == 'n':
                        self.play_continues = False
        else:
            self.play_continues = False
            print('I\'m sorry. You now have a negative balance and cannot continue')

    def shuffle_if_needed(self):
        if self.current_card_index == 51:
            print()
            print('You are amazing! You\'ve played through an entire deck of cards')
            print('Let\'s shuffle this deck.')
            print()
            self.deck.shuffle(random.randint(2,5))
            self.current_card_index = 0