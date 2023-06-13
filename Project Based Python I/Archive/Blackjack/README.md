<img src="./images/blackjack.png" width="700"/>

# Blackjack
> DIFFICULTY: **INTERMEDIATE**

Blackjack is a super popular card game with relatively simple rules: the most important being you need 21 to win, or you need a higher score than the dealer without going bust!

It combines most of the skills we’ve already covered in previous projects, including creating classes, loops, conditional statements, importing modules, accepting user input, and string formatting.

## Deck

A standard deck of cards has four suits, Heart, Diamonds, Spades and Clubs. It also has 13 ranks, 2 through 10, then the face cards Jack, Queen, King and Ace. For a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting.

## TODO

1. Create a deck of 52 cards.
2. Shuffle the deck.
3. Deal two cards to the Dealer and two cards to the Player.
4. Show only one of the Dealer’s cards, the other remains hidden.
5. Show both of the Player’s cards.
6. Ask the Player if they wish to Hit, and take another card.
7. If the Player’s hand doesn’t Bust (go over 21) , ask if they’d like to Hit again.
8. If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17.
9. Determine the winner.
10. Ask the Player if they’d like to play again.

## Rules

- A card is dealt to the player facing upwards (visible to everyone).
- The dealer deals a card to himself visible to everyone.
- Another card is given to the player facing upwards.
- The dealer deals a card facing downwards for himself.
- The player has to decide whether to stand with the current set of cards or get another card.
- If the player decides to hit, another card is dealt.
- If the sum of the player's cards is more than 21. Player **BUSTED**
- If the player decides to stand, then the dealer reveals his hidden card.
- The dealer does not have the authority to decide whether to hit or stand. 
- The dealer needs to keep hitting more cards if the sum of dealer’s cards is less than 17.
- As soon as the sum of dealer’s cards is either 17 or more, the dealer is obliged to stand.
- If the sum of the dealer's cards is more than 21. Dealer **BUSTED**
- According to the final sum of the cards, the winner is decided.

