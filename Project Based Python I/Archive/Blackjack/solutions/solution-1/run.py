from utils import *

os.system('clear')
print('WELCOME TO BLACKJACK')

# Create and shuffle the deck
deck = Deck()
deck.shuffle()

while True:
    
    # Create Player and Dealer hands
    player_hand = Hand()
    dealer_hand = Hand()

    # Deal two cards to each player
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Show cards but keep one dealer card hidden
    show_some(player_hand,dealer_hand)
    
    
    playing = True
    while playing: # recall from hit_or_stand function
        
        #Prompt for player to hit or stand
        show_some_again, playing = hit_or_stand(deck,player_hand)
        
        # Show cards but keep one dealer card hidden
        if show_some_again:
            show_some(player_hand,dealer_hand)
        
        # If player's hand exceeds 21, run player busts()
        if player_hand.value > 21:
            print('DEALER WINS! because PLAYER BUSTED!')
            
            break
            
    # If player hasn't busted, 
    # play Dealer's hand until Dealer reach 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        
        # Show all cards
        show_all(player_hand,dealer_hand)
        
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
    new_game = input('Would you like to play another hand? y/n?')
    
    if new_game[0].lower() == 'y':
        continue
    else:
        print('Thank you for playing')
        break
        