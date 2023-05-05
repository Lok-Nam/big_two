import pygame
import game_class as gc
import game_control as gcon
import display_functions as df

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
                    return -1 # -1 means invalid combination
            return size
        case 5:
            # sort cards
            cards = sortCardsVisualValue(cards)
            # define cards property
            ascending = True
            sameSuit = True
            specialAsc = True
            specialSnake = [1,10,11,12,13]
            # check straightFlush first : 
            for i in range(4):
                if(cards[i].value + 1 != cards[i+1].value):
                    ascending = False
                if(cards[i].suit != cards[i+1].suit):
                    sameSuit = False
            for i in range(5):
                if(cards[i].value != specialSnake[i]):
                    specialAsc = False
            if(sameSuit and (ascending or specialAsc)):
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
            if(ascending or specialAsc):
                return snake
    return -1 # no combination

def sortCardsActualValue(cards):
    """
    A function to sort cards. By actual value i.e. 2 is largest
    """
    for i in range (len(cards)):
        smallest = cards[i]
        smallestIndex = i
        for k in range (i+1, len(cards)):
            if(checkLargerCard(smallest, cards[k]) == True):
                smallest = cards[k]
                smallestIndex = k
        (cards[i], cards[smallestIndex]) = (cards[smallestIndex], cards[i])
    return cards

def sortCardsVisualValue(cards):
    """
    A function to sort cards. By visual value i.e. 1 is smallest
    """
    for i in range (len(cards)):
        smallestIndex = i
        for k in range (i+1, len(cards)):
            if(cards[smallestIndex].value > cards[k].value):
                smallestIndex = k
        (cards[i], cards[smallestIndex]) = (cards[smallestIndex], cards[i])
    return cards


def checkLargerCard(cardA,cardB):
    """
    check if first card is larger than second card.
    return True if so.
    """
    valueA = cardA.value
    valueB = cardB.value
    if(valueA == 1 or valueA == 2): # in big_2, ace and 2 are the largest.
        valueA = valueA + 13
    if(valueB == 1 or valueB == 2):
        valueB = valueB + 13

    if(valueA > valueB):
        return True
    elif(valueA == valueB and cardA.suit.value > cardB.suit.value):
        return True
    else:
        return False

def findLargestCard(cards):
    """
    take in a valid combination of cards and return the card that indicate the combination value.
    cards[0] is the card list, cards[1] is the type of comb
    """
    sortCardsActualValue(cards[0])
    size = len(cards[0])
    if(size > 0 and size < 5):
        return cards[0][size-1]
    if(size == 5):
        match cards[1]:
            case 5|6|9:
                return cards[0][4]
            case 7|8:
                return cards[0][2]
    return -1
        

def checkLargerComb(currCard, cardPlayed):
    """
    check if the played card is larger than the currCard(previous player's card)
    return True if the card is playable (cards are sorted)
    The arguement taken are a 2 size array, where 0 is the cards and 1 is the combination type
    """
    if currCard[1] == -1 and cardPlayed[1] != -1: # When there are no previous card
        return True
    if cardPlayed[1] == -1:
        return False
    # get the value of the largest card in combination first
    currLargest = findLargestCard(currCard)
    playedLargest = findLargestCard(cardPlayed)
    isLarger = checkLargerCard(playedLargest, currLargest)
    # checking combination type 1-4:
    if((currCard[1] == cardPlayed[1] and currCard[1] < 5)and isLarger): # same combination
        return True
    # checking combination type 5-9
    if(currCard[1] > 4 and cardPlayed[1] > 4):
        if(currCard[1] < cardPlayed[1]):
            return True
        if(currCard[1] == cardPlayed[1] and isLarger):
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


def checkContainThree(cards, isFirst):
    """
    check if the player's played card contains diamond 3.
    this function is for first round only.
    """
    if(isFirst == False):
        return True
    for x in cards:
        if x.value == 3 and x.suit.value == 1:
            return True
    return False

def playCard(player, cardPlayed):
    """
    this function play the card.
    """
    for x in cardPlayed[0]:
        for i in range(len(player.hand)):
            if (player.hand[i].value == x.value) and (player.hand[i].suit.value == x.suit.value):
                player.hand.remove(player.hand[i])
                break
    return player


def nextPlayer(index):
    if(index == 3):
        return 0
    else:
        return index + 1

def isSkipping(cards):
    if(cards == []):
        return False
    return True

def pickCard(cardIndex, player, cardPlayed):
    cardPicked = player.hand[cardIndex]
    if cardPicked in cardPlayed[0]:
        cardPlayed[0].remove(cardPicked)
    else:
        cardPlayed[0].append(cardPicked)
    sortCardsActualValue(cardPlayed[0])
    return cardPlayed

def gameLoop(players): # players is an array with player object
    """
    looping the game until a player win
    """
    # initialising variables
    deck = gc.deck()
    decks = deck.distribute()
    iniHand(players, decks)
    winner = False # True if there is a winner
    currCard = [[], -1] # value and type of combination of card played by previous player
    cardPicked = [[], -1]
    index = goFirst(players) # which player is playing the card now
    passNum = 0 # when 3 players pass, the 4th player is able to play any card
    isSkip = False
    isPlayed = False
    isExit = False
    isFirst = True

    #loop start here
    while winner == False:
        # initialising variables for each turn at the beginning.
        if(passNum == 3): # this line is to allow 4th player to play any card if the previous 3 players all skipped
            currCard = [[], -1]
            passNum = 0
        isSkip = False
        isPlayed = False
        sortCardsActualValue(players[index].hand)

        # a while loop for player to pick card. If the combination is correct, "play" button will appear.
        # if the "play" button is pressed or the skip button is pressed, while loop ends. Then next player's turn. 
        while((not isSkip) and (not isPlayed) and (not isExit)):
            # debugging
            # handling events
            (players[index], cardPicked, isSkip, isPlayed, isExit) = gcon.handle_mouse_click(players[index], cardPicked, checkLargerComb(currCard, cardPicked) and checkContainThree(cardPicked[0], isFirst), isSkipping(currCard[0]))

            # updating card info
            cardPicked[1] = -1
            comType = checkCombination(cardPicked[0])
            if(comType != -1):
                cardPicked[1] = comType
            

            # update screen
            df.ini_screen()
            df.display_hand(players[index], cardPicked[0])
            df.display_last_played(currCard)
            df.display_buttons(checkLargerComb(currCard, cardPicked)and checkContainThree(cardPicked[0], isFirst), isSkipping(currCard[0]))
            df.display_top_bar(players, index)
            pygame.display.flip()


        # initialising variables for each turn at last.
        isFirst = False
        index = nextPlayer(index)
        if(isSkip == True):
            passNum += 1
        else:
            currCard = cardPicked.copy()
            passNum = 0
        cardPicked = [[], -1]
        if checkWinner(players[index]):
            return index
        if isExit:
            pygame.quit()