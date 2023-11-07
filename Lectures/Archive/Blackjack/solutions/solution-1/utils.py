import random
import os
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight',
    'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace',
)
values = {
    'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,
    'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
    'Jack':10, 'Queen':10, 'King':10, 'Ace':11,
}
#---------------------------------------------------
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
#--------------------------------------------------
class Deck:
    
    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit,rank)
                self.deck.append(created_card)
                         
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp
            
        
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
    
#----------------------------------------------
class Hand:
    def __init__(self):
        self.cards = [] # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0   # add an arribute to keep track of aces
        
    def add_card(self,card):
        # card passed in from Deck.deal()
        self.cards.append(card)
        self.value += card.value
        
        # trace aces
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        
        # if total value > 21 and i still have an ace
        # then change my ace to be 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
#-----------------------------------------------------
def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
#----------------------------------------------------
def hit_or_stand(deck,hand):
    playing = True
    
    while True:
        x = input('Hit or Stand? Enter h or s: ')
        
        if x[0].lower() == 'h':

            hit(deck,hand)
            show_some_again = True
        elif x[0].lower() == 's':

            print("Player Stands. Dealer's Turn.")
            show_some_again = False
            playing = False
        else:

            print('Sorry, please try again.')
            continue
        break
    return show_some_again, playing

#---------------------------------------------
def show_some(player,dealer):
    os.system('clear')
    # Show only second card of dealer's cards
    print('__'*25)
    print("\nDealer's Hand: ")
    print("\tFirst card (hidden)")
    print('\t',dealer.cards[1])
    print('__'*25)
    
    # Show all (2) cards of player's cards and value
    print("\nPlayer's Hand:")
    for card in player.cards:
        print('\t',card)
    print(f"Value of Player's hand is: {player.value}")
    print('__'*25)
        
        
def show_all(player,dealer):
    os.system('clear')
    # Show all (2) cards of dealer's cards and value
    print('__'*25)
    print("\nDealer's Hand:")
    for card in dealer.cards:
        print('\t',card)
    print(f"Value of Dealer's hand is: {dealer.value}")
    print('__'*25)
    print("\nPlayer's Hand:")
    for card in player.cards:
        print('\t',card)
    print(f"Value of Player's hand is: {player.value}")
    print('__'*25)
