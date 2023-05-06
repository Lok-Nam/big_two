import pygame
import game_class as gc
import game_control as gcon
import game_logic as gl
import display_functions as df

running = True
pygame.init()

players = []
for i in range (4):
    players.append(gc.player(i))
winner = gl.gameLoop(players)

if(winner == -1): # exiting game
    pygame.quit()
else:
    print("player", winner+1, "won") # print win message
    pygame.quit()