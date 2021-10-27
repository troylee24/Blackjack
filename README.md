# Blackjack
This python project runs a Blackjack game using the terminal.

Please free to check out the [rules](https://bicyclecards.com/how-to-play/blackjack/) if you are unfamiliar with the game.

## Class Descriptions
* [Card](card.py) - creates a card from a standard 52-card deck
* [Deck](deck.py) - creates a deck that can be shuffled and drawn from
* [Hand](hand.py) - creates a hand and provides functions for checking its status (i.e. hand is a bust)
* [Player](player.py) - creates a player that can play and make bets

## Starting the game
```
$ python3 game.py
```

## Example Game
```
Number of Players: 4
Ready to Play? (Y/N): Y

...Shuffling Deck...
...Gathering Bets...

* Bets must be in multiples of $5 *

Player 0's chip stack: $100
How much would you like to bet?: $10

Player 1's chip stack: $100
How much would you like to bet?: $20

Player 2's chip stack: $100
How much would you like to bet?: $50

Player 3's chip stack: $100
How much would you like to bet?: $10

...Dealing Cards...

----- Player 0's turn -----

Dealer's Hand: Q♦ (10)

Hand: A♣ 6♣ (7 or 17)
Hit or Stand?: hit
Hand: A♣ 6♣ 5♥ (12)
Hit or Stand?: hit
Hand: A♣ 6♣ 5♥ 10♥ (22)

* BUST! *

----- Player 1's turn -----

Dealer's Hand: Q♦ (10)

Hand: 9♣ A♠ (10 or 20)
Hit or Stand?: stand

* STAND! *

----- Player 2's turn -----

Dealer's Hand: Q♦ (10)

Hand: 5♦ 4♦ (9)
Hit or Stand?: hit
Hand: 5♦ 4♦ A♥ (10 or 20)
Hit or Stand?: stand

* STAND! *

----- Player 3's turn -----

Dealer's Hand: Q♦ (10)

Hand: 7♦ J♠ (17)
Hit or Stand?: stand

* STAND! *

----- Dealer's turn -----

Dealer: Q♦ K♥ (20)

* DEALER STANDS WITH 20 *

----- RESULTS -----

Dealer   | 20
Player 0 | 22 (BUST!)
Player 1 | 20
Player 2 | 20
Player 3 | 17

Dealer ended with 20.
Player 0 busted with 22.
Player 1 tied with 20.
Player 2 tied with 20.
Player 3 lost with 17.

----- CHIP STACKS -----

Player 0 | $90 (-$10)
Player 1 | $100 (+$0)
Player 2 | $100 (+$0)
Player 3 | $90 (-$10)
```