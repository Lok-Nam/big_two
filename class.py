import pygame

class player:

    def __init__(self, name):
        self.name = name
        self.hand = []


class card:
    
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

