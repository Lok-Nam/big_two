"""
This file is just for me to test random things.
"""
import pygame
import game_class as gc
import game_control as gcon
import game_logic as gl
import display_functions as df

while True:

    pygame.init()
    players = []
    for i in range (4):
        players.append(gc.player(i))
    testDeck = gc.deck()
    decks = testDeck.distribute()
    gl.iniHand(players, decks)
    df.display_hand(players[0])
    pygame.display.flip()
    pygame.time.delay(10000)