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
#-----------------------------------------
class Card:
    pass

#--------------------------------------------
class Deck:
        
    def shuffle(self):
        pass
    
    def deal(self):
        pass
    
#-----------------------------------------
class Hand:
        
    def add_card(self,card):
        pass
        
    def adjust_for_ace(self):
        pass

#----------------------------------------    
def hit(deck,hand):
    pass
    
#------------------------------------------
def hit_or_stand(deck,hand):
    pass

#------------------------------------------
def show_some(player,dealer):
    pass
        
#-----------------------------------------      
def show_all(player,dealer):
    pass
#----------------------------------------
# run.py file --------------------------

# Create and shuffle the deck

while True:
    
    # Create Player and Dealer hands

    # Deal two cards to each player
       
    # Show cards but keep one dealer card hidden

    playing = True
    while playing: # recall from hit_or_stand function
        
        # Prompt for player to hit or stand
        # Show cards but keep one dealer card hidden
        # If player's hand exceeds 21, player busts   
        # If player hasn't busted, 
        # play Dealer's hand until Dealer reach 17
        
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            pass
        
        # Show all cards
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            print('PLAYER WINS! because DEALER BUSTED!')
        elif dealer_hand.value > player_hand.value:
            print('DEALER WINS!')
        elif dealer_hand.value < player_hand.value:
            print('PLAYER WINS!')
        else:
            print('Dealer and Player tie! PUSH')
            
    
    # Ask to play again
        