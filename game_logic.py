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
            # sort cards
            cards = sortCards(cards)
            # define cards property
            ascending = True
            sameSuit = True
            # check straightFlush first : 
            for i in range(4):
                if(cards[i].value + 1 != cards[i+1].value):
                    ascending = False
                if(cards[i].suit != cards[i+1].suit):
                    sameSuit = False
            if(sameSuit and ascending):
                return straightFlush
            # check fourPlusOne ie KKKKA: 
            if(cards[1].value == cards[2].value == cards[3].value and (cards[1].value == cards[0].value or cards[1].value == cards[4].value)):
                return fourPlusOne
            # check gourd ie KKKAA: 
            if((cards[0].value == cards[1].value == cards[2].value and cards[3].value == cards[4].value)or  (cards[2].value == cards[3].value == cards[4].value and cards[0].value == cards[1].value)):
                return gourd
            # check flush(same suit):
            if(sameSuit):
                return flush
            if(ascending):
                return snake
    return -1 # no combination

def sortCards(cards):
    """
    A function to sort cards in 5.
    """
    for i in range (4):
        smallest = cards[i].value
        smallestIndex = i
        for k in range (i+1, 5):
            if(cards[k].value < smallest):
                smallest = cards[k].value
                smallestIndex = k
        temp = cards[smallestIndex]
        cards[i] = cards[smallestIndex]
        cards[smallestIndex] = temp
    return cards

        

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


def gameLoop(players): # players is an array with player object
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
    index = goFirst(players) # which player is playing the card now


    #loop start here
    while winner == False:
        