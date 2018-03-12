import NewDeck
"""
DRAW CARD: Draw(x, deck):  -- Returns list of cards in class form
PRINT CARD TO USER: ReadCard(card):  -- Returns nothing, prints in format "King of Spades"
READ HAND: ReadHand(hand): calls read card function for all cards in hand
READ WHOLE DECK: ReadWholeDeck(Stack):
NEW DECK: NewDeck()
SHUFFLE ShuffleDeck(deck):
"""
#A = 1 for now
#No splitting

def GameStart(deck):
    dealer_hand = []
    hand1 = []
    hand1.extend(NewDeck.Draw(1,deck))          #Dealing one card at a time is probably not necessary
    dealer_hand = NewDeck.Draw(1,deck)
    print("***Dealer Shows:"),                   
    NewDeck.ReadHand(dealer_hand)               #Dealer shows one, first card face up according to Bicycle
    hand1.extend(NewDeck.Draw(1,deck))          #Second Cards
    dealer_hand.extend(NewDeck.Draw(1,deck))
    print("***Your Hand:")
    NewDeck.ReadHand(hand1)
    #ready for player 1 turn
    return(dealer_hand,hand1)

def PlayerTurn(hand,deck):
    double = 1.0        #multiply returned value by this variable
    double2 = 1.0
    split = ''
    hand2 = []
#Split Section
    if hand[0].value == hand[1].value:
        split = input ("(sp)lit?")
        if split == 'sp':                           #Split hand and draw new cards
            hand2 = hand[:1]                          
            hand = hand[1:]
            hand.extend(NewDeck.Draw(1,deck))
            hand2.extend(NewDeck.Draw(1,deck))
            print('*****Hand 1:')
            NewDeck.ReadHand(hand2)   
            (hand2, double2) = HandActions(hand2, deck)
            NewDeck.ReadHand(hand)  
            print('*****Hand 2:')                                                    #Plays split hand
    (hand,double) = HandActions(hand,deck)                      #Plays main hand
    return (hand, double, hand2, double2)
    
def HandActions(hand,deck):     #Decision making of player turn
    action = ''
    double = 1.0
    while SumHand(hand) < 21:
        if action == '':                        #First Action
            action = input("(h)it, (st)and, or (d)ouble?")
        else:                                   #subsequent actions
            action = input("(h)it or (st)and")  
        #Handling input    
        if action == 'h':
            hand.extend(NewDeck.Draw(1,deck))
            NewDeck.ReadHand(hand)            
        elif action == 'st':
            return(hand, double) #end while loop
        elif action == 'd':
            #double bet function here
            hand.extend(NewDeck.Draw(1,deck))
            NewDeck.ReadHand(hand)
            double = 2.0
            return(hand, double)
    return (hand,double)

def DealerTurn(hand,deck):
    while SumHand(hand) < 17:
        hand.extend(NewDeck.Draw(1,deck))
    print("Dealer Shows:")   
    NewDeck.ReadHand(hand)            
    return (hand)


def SumHand(hand):
    sum = 0
    ace = 0     #tracks if ace is in hand
    for items in hand:
        if items.value > 10:
            sum += 10
        else:
            sum += items.value
        if items.value == 1:
            ace = 1
    if (sum < 12 and ace > 0):  #Are you using ace as an 11?
        sum += 10
    return sum

def ScoreCheck(player_hand, dealer_hand):  # -1 = loss, 0 = push, 1 = win
    Player_Score = SumHand(player_hand)
    Dealer_Score = SumHand(dealer_hand)
    #For Bug Checking
    if (Player_Score > 0):          #Covers empty split hand scenario
        print('Player Score: ' + str(Player_Score))
        print('Dealer Score: ' + str(Dealer_Score))
    
    if Player_Score == 0:     #This is to cover for empty split hands
        return (0.0)
    elif Player_Score > 21:       #does player bust?
        print("BUST!")
        return (-1.0)
    elif Dealer_Score > 21:     #does dealer bust?
        print("Dealer Busts!")
        return (1.0)
    else:                       #actual head to head
        if Player_Score > Dealer_Score:       
            print("You Win!")
            return (1.0)
        elif Player_Score == Dealer_Score:
            print("Push")
            return (0.0)
        else:
            print("You Lose!")
            return (-1.0)

def BlackjackCheck(player_hand, dealer_hand):  #Only call before any action
    PBj = (SumHand(player_hand) == 21)
    DBj = (SumHand(dealer_hand) == 21)

    if PBj == True and DBj == True:
        print("Push")
        return (0.0)
    elif PBj == True and DBj == False:
        print("Blackjack!")
        return (1.5)
    elif PBj == False and DBj == True:
        print("Dealer Blackjack")
        NewDeck.ReadHand(dealer_hand)   
        return (-1.0)
    else:
        return  2.0   #2 will be written over, place holder to use for checking to score off blackjack check or not
       
    
def main():
    deck_count = 2
    min_cards = 20  #cards before a shuffle
    my_deck = NewDeck.NewDeck()*deck_count
    print('Deck Count: '+str(deck_count))
    NewDeck.ShuffleDeck(my_deck)
    #Could ask player count here
    done = ''
    score = 0.0
    double = 1.0
    double2 = 1.0
    while (done != 'y'):
        (dealer_hand,hand1) = GameStart(my_deck)            #Deals cards into hands, reads applicable cards
        round_score = BlackjackCheck(hand1, dealer_hand)    #checks for blackjacks
        if (round_score == 2):                              #i.e. no blackjacks
            (hand1, double, hand2, double2) = PlayerTurn(hand1,my_deck)                       #player 1 turn, returns finished hand
            if SumHand(hand1) < 22 or (0 < SumHand(hand2) < 22):                         #if player busts, dont bother with dealer. 
                DealerTurn(dealer_hand, my_deck)
        round_score = ScoreCheck(hand1, dealer_hand) * double + ScoreCheck(hand2, dealer_hand) * double2
        score += round_score
        print('Current Score: ' + str(score))
        done = input("Done? - (y)es or any key to continue")
        #print ('debugging: Cards left = '+str(len(my_deck)))
        if len(my_deck) < min_cards:                                #Shuffle
            my_deck = NewDeck.NewDeck()*deck_count
            NewDeck.ShuffleDeck(my_deck)
            print ('New Deck')
        
main()
