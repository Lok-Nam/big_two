import pygame
import game_class as gc
import game_logic as gl


def get_key_click():
    ev = pygame.event.get()

    for event in ev:
        return

def get_mouse_click():
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            