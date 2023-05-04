import game_class as gc
import pygame

global screen

# defining variables.
size_o = screen_width, screen_height = 1400, 720

card_width = 100
card_height = 140
card_rect = pygame.Rect(0, 0, card_width, card_height)
bounds = (screen_width, screen_height)
screen = pygame.display.set_mode(bounds)
screen.fill((0, 0, 0))
pygame.display.set_caption("big_two")


def display_hand(player):
    cards = player.hand
    num = len(cards)
    offset = (screen_width -( card_width*num ))/2
    for i in range (num):
        image = cards[i].image.convert()
        image = pygame.transform.scale(image, (card_width, card_height))
        x = offset + (i*card_width)
        pos = pygame.Rect(x, screen_height - card_height, card_width, card_height)
        screen.blit(image, pos)


def display_last_played(played):
    cards = played[0]

def display_play_buttons(isPlayable):
    if(isPlayable):
        return
    else:
        return

def display_current_player(player):
    return

def display_left_cards(players):
    return
