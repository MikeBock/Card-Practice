#Generating a deck
#suits  0: Spades
#       1: Hearts
#       2: Clubs   
#       3: Diamonds
import random

class card(object):
    def __init__(self, suit, value):
        self.suit = suit  
        self.value = value
  
def NewDeck():
    Deck = []
    loc = 0
    suit = 0
    value = 1
    while loc < 52:
        Deck.append(card(suit,value))
        loc += 1
        value += 1 
        if value > 13:              #if greater than king, move on to next suit
            value = 1
            suit += 1
    return Deck

def ReadCard(card):
    if card.suit == 0:
        psuit = "Spade"
    elif card.suit == 1:
        psuit = "Heart"
    elif card.suit == 2:
        psuit = "Club"
    else:
        psuit = "Diamond"
        
    if card.value == 1:
        pvalue = "Ace"
    elif card.value == 11:
        pvalue = "Jack"
    elif card.value == 12:
        pvalue = "Queen"
    elif card.value == 13:
        pvalue = "King"
    else:
        pvalue = str(card.value)
        
    print (pvalue+" of "+psuit+"s")
        
    return 

def ReadWholeDeck(Stack):
    for items in Stack:
        reading = ReadCard(items)
       # print (reading[0]+" of "+reading[1]+"s")
        #print (join(str(items.suit)+" of "+(str(items.value))+"s"))
    return()

def ShuffleDeck(deck):
    random.shuffle(deck)
    return (deck)

def Draw(x, deck): #draw x cards from deck
    cardsdrawn = []
    index = 0
    while index < x:
        drawn = deck.pop(0)
        cardsdrawn.append(drawn)
        index += 1
    return (cardsdrawn) #returns cards drawn in a list

def ReadHand(hand):
    for items in hand:
        ReadCard(items)
    return

###ReadWholeDeck(Stack) #Reads the whole deck of stack.
##ShuffledDeck = ShuffleDeck(NewDeck())
###ReadWholeDeck(ShuffledDeck)
###my_hand = ReadCard(Draw(1,ShuffledDeck))
##
##my_hand = []
##
##my_hand.extend(Draw(2, ShuffledDeck))
##
##ReadHand(my_hand)

