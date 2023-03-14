import pygame


def checkWinner(player):
    """
    Check of a player has won.
    Return boolean value.
    """
    if player.hand == []:
        return True
    return False