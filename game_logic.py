import pygame
import game_class as gc

def checkWinner(player):
    """
    Check if a player has won.
    Return boolean value.
    """
    if player.hand == []:
        return True
    return False

def playCard(player):
    """
    function to play the card
    """
    return

def checkCombination(cards):
    """
    check which type of combination is this
    """
    size = len(cards)
    snake = 5
    flush = 6
    gourd = 7
    fourPlusOne = 8
    straightFlush = 9
    match size:
        case 1:
            return 1
        case 2|3|4:
            for i in range (size - 1):
                if(cards[i].value != cards[i+1].value):
                    return 0 # 0 means invalid combination
            return size
        case 5:


    return 

def checkLarger(currCard, cardPlayed):
    """
    check if the played card is larger than the currCard(previous player's card)
    return True if the card is playable
    """
    
    if currCard[1] == None: # When there are no previous card
        return True
    if (currCard[1] == cardPlayed[1]) and (max(currCard[0]) < ):
        return True
    return False

def goFirst(players):
    """
    check which player go first, player with diamond 3 will go first
    
    return the number of the player
    """
    for i in range(4):
        for x in players[i].hand:
            if(x.value == 3 and x.suit.value == 1):
                return i
    return -1 # this line should not be runned because diamond 3 is always there unless it has bug

def iniHand(players, decks):
    """
    initialise players' hand i.e. distribute decks
    """
    for i in range(4):
        players[i].hand = decks[i]


def gameLoop(players):
    """
    looping the game until a player win
    """
    # initialising things
    turn = 0
    deck = gc.deck()
    decks = deck.distribute()
    iniHand(players, decks)
    winner = False
    currCard = [[None][None]] # value and type of combination

    #loop start here
    while winner == False:
        