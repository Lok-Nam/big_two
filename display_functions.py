import game_class as gc
import pygame

global screen
pygame.init()

# defining variables.

# screen
size_o = screen_width, screen_height = 1400, 720
bounds = (screen_width, screen_height)
screen = pygame.display.set_mode(bounds)
screen.fill((0, 0, 0))
pygame.display.set_caption("big_two")

# colours
blue = (0, 0, 255)
dark_blue = (0,0,139)
orange = (255,165,0)
dark_orange = (220,88,42)
green = (124,252,0)
white=(255,255,255)
black = (0,0,0)

# cards
card_width = 100
card_height = 140

# buttons
button_width = 120
button_height = 70
play_button_X = screen_width /2 -250
play_button_Y = screen_height/2 + card_height
skip_button_X = screen_width - play_button_X - button_width
skip_button_Y = play_button_Y
play_button_rect = pygame.Rect(play_button_X, play_button_Y, button_width, button_height)
skip_button_rect = pygame.Rect(skip_button_X, skip_button_Y, button_width, button_height)

# fonts
smallfont = pygame.font.SysFont('Corbel',35)

# top bar
bar_height = 50
bar_rect = pygame.Rect(0, 0, screen_width, bar_height)

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
    num = len(cards)
    offsetX = (screen_width -( card_width*num ))/2
    offsetY = (screen_height - card_height)/2
    for i in range (num):
        image = cards[i].image.convert()
        image = pygame.transform.scale(image, (card_width, card_height))
        x = offsetX + (i*card_width)
        pos = pygame.Rect(x, offsetY, card_width, card_height)
        screen.blit(image, pos)

def display_buttons(isPlayable):
    text_play = smallfont.render('play' , True , white)
    text_skip = smallfont.render('skip', True, white)
    mouse = pygame.mouse.get_pos()
    if((mouse[0] > play_button_X and mouse[0] < play_button_X + button_width)and(mouse[1] > play_button_Y and mouse[1] < play_button_Y + button_height) and isPlayable):
        pygame.draw.rect(screen, dark_blue, play_button_rect)
        screen.blit(text_play, (play_button_X+20, play_button_Y+20))
    elif(isPlayable):
        pygame.draw.rect(screen, blue, play_button_rect)
        screen.blit(text_play, (play_button_X+20, play_button_Y+20))
    
    if((mouse[0] > skip_button_X and mouse[0] < skip_button_X + button_width)and(mouse[1] > skip_button_Y and mouse[1] < skip_button_Y + button_height)):
        pygame.draw.rect(screen, dark_orange, skip_button_rect)
        screen.blit(text_skip, (skip_button_X+20, skip_button_Y+20))
    else:
        pygame.draw.rect(screen, orange, skip_button_rect)
        screen.blit(text_skip, (skip_button_X+20, skip_button_Y+20))

    

def display_top_bar(players, index):
    message = ('Current player is Player' + str(index+1) + ', Cards left for each player : ')
    pygame.draw.rect(screen, green, bar_rect)
    for i in range(len(players)):
        if(i != index):
            message += (' | Player' + str(i+1) + ': ' + str(len(players[i].hand)))
    bar_message = smallfont.render(message, True, black)
    screen.blit(bar_message, (0,0))
