import pygame
import game_class as gc
import game_logic as gl
import display_functions as df



def handle_mouse_click(player, cardPlayed, isPlayable, isSkippable):
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # clicking cards
            num = len(player.hand)
            offset = (df.screen_width -( df.card_width*num ))/2
            if ((pos[0] > offset and pos[0] < df.screen_width - offset )and pos[1] > df.screen_height - df.card_height):

                # within range of picking cards
                card_num = (pos[0] - offset) // df.card_width
                cardPlayed = gl.pickCard(int(card_num), player, cardPlayed)
                
                return (player, cardPlayed, False, False, False)
            
            # clicking play button
            if(isPlayable):
                if((pos[0] > df.play_button_X and pos[0] < df.play_button_X + df.button_width) and (pos[1] > df.play_button_Y and pos[1] < df.play_button_Y + df.button_height)):
                    player = gl.playCard(player, cardPlayed)
                    return (player, cardPlayed, False, True, False)
            
            # clicking skip button
            if(isSkippable):
                if((pos[0] > df.skip_button_X and pos[0] < df.skip_button_X + df.button_width) and (pos[1] > df.play_button_Y and pos[1] < df.play_button_Y + df.button_height)):
                    return (player, cardPlayed, True, False, False)
        elif event.type == pygame.QUIT:
            return (player, cardPlayed, False, False, True)
        else:
            return (player, cardPlayed, False, False, False)
    return (player, cardPlayed, False, False, False)