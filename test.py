"""
This file is just for me to test random things.
"""

import game_class as gc
import game_logic as gl
testDeck = gc.deck()
#cards = testDeck.distribute()
counter = 0
for x in testDeck.cards:
    print(counter, x.value, x.suit.name)
    counter = counter + 1
print("==========")
testComb1 = []
for x in [0,13,26,39]:
    testComb1.append(testDeck.cards[x])
type1 = gl.checkCombination(testComb1)
print(type1)
curr = [testComb1, type1]
print("==========")
testComb2 = []
for x in [2,15,28,41]:
    testComb2.append(testDeck.cards[x])
type2 = gl.checkCombination(testComb2)
print(type2)
played = [testComb2, type2]
print("==========")
print(gl.checkLargerComb(curr, played))