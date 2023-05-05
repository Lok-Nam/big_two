"""
This file is just for me to test random things.
"""
import pygame
import game_class as gc
import game_control as gcon
import game_logic as gl
import display_functions as df

while True:
    players = []
    for i in range (4):
        players.append(gc.player(i))
    testDeck = gc.deck()
    decks = testDeck.distribute()
    gl.iniHand(players, decks)
    gl.sortCardsActualValue(players[0].hand)
    df.display_hand(players[0])
    df.display_last_played([players[0].hand])
    df.display_buttons(True)
    df.display_top_bar(players, 0)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #pygame.time.delay(5000)