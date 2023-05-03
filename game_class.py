import random
import pygame
from enum import Enum
import numpy as np

class player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def getDeck(self, deck):
        self.hand = deck

class suits(Enum):
    CLUB = 2
    SPADE = 4
    HEART = 3
    DIAMOND = 1

class deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for i in range (1,14):
                self.cards.append(card(suit, i))

    def distribute(self):
        """
        return a list of 4 shuffled decks
        """
        random.shuffle(self.cards)
        array = np.array(self.cards)
        decks = np.array_split(array, 4)
        return decks

class card:
    
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
        #self.image = pygame.image.load('images/' + self.suit.name + '-' + self.value + '.png')

