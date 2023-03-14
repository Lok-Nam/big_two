import random
import pygame
from enum import Enum
import numpy as np

class player:

    def __init__(self, name):
        self.name = name
        self.hand = []

class suits(Enum):
    CLUB = 1
    SPADE = 2
    HEART = 3
    DIAMOND = 4

def deck():
    
    def __init__(self):
        self.cards = []
        for suit in suits:
            for i in range (1,14):
                self.cards.append(card(suit, i))
    
    def shuffle(self):
        """
        shuffle the deck
        """
        random.shuffle(self.cards)

    def distribute(self):
        """
        return a list of 4 decks
        """
        array = np.array(self.cards)
        decks = np.array_split(array)
        return decks



class card:
    
    def __init__(self, suit, value, image):
        self.value = value
        self.suit = suit
        self.image = pygame.image.load('images/' + self.suit.name + '-' + self.value + '.png')

