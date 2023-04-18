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
    The arguement taken are a 2 size array, where 0 is the cards and 1 is the combination type
    """
    if currCard[1] == None: # When there are no previous card
        return True
    # checking combination type 1-4:
    if((currCard[1] == cardPlayed[1] and currCard[1] < 5) and currCard[0][0].value == cardPlayed[0][0].value):
        return True
    # checking combination type 5-9
    if(currCard[1] > 4 and cardPlayed[1] > 4):
        if(currCard[1] == cardPlayed[1]): # same combination case i.e. snake vs snake
            size = len(currCard[0])
            match size:
                case 5:
                    if(cardPlayed[0][4].value > currCard[0][4].value):
                        return True
                    elif(cardPlayed[0][4].value == currCard[0][4].value and cardPlayed[0][4].value.suit > currCard[0][4].value.suit):
                        return True
                case 6:
                    if(cardPlayed[0][4].value > currCard[0][4].value):
                        return True
                case 7|8:
                    if(cardPlayed[0][2].value > currCard[0][2].value):
                        return True
                case 9:
                    if(cardsPlayed[0][4].value > currCard[0][4].value):
                        return True
                    elif(cardPlayed[0][4].value.suit > currCard[0][4].value.suit):
                        return True
        elif(cardPlayed[1] > currCard[1]):
            return True
        else:
            return False
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

def checkContainThree(cards):
    """
    check if the player's played card contains diamond 3.
    this function is for first round only.
    """
    for x in cards:
        if x.value == 3 and x.suit.value == 1:
            return False
    return True

def playCard(player):
    """
    this function play the card.
    """

def nextPlayer(index):
    if(index == 3):
        return 0
    else:
        return index + 1


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
    passNum = 0 # when 3 players pass, the 4th player is able to play any card
    isSkip = False
    isPlayed = False

    #loop start here
    while winner == False:
        # initialising variables for each turn at the beginning.


        # methods to display player's desk first.


        # a while loop for player to pick card. If the combination is correct, "play" button will appear.
        # if the "play" button is pressed or the skip button is pressed, while loop ends. Then next player's turn. 
        while(not isSkip and not isPlayed):

              
        
        # initialising variables for each turn at last.
        index = nextPlayer(index)
        isSkip = False
        isPlayed = False