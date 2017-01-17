# A simple python 'Set' solver!

## The Game
In case you're unfamiliar with Set, you can [read about it](https://en.wikipedia.org/wiki/Set_(game)) or [try this tutorial](http://www.setgame.com/sites/default/files/tutorials/tutorial/SetTutorial.swf).

## The Program
Given a number of cards in a player's hand, this Set solver takes an arbitrary (user-provided) number of dimensions per card (i.e. a card has a background color in addition to color, shape, shading, and number, giving the card 5 dimensions) and an arbitrary size (i.e. each card may now have 4 of every dimension instead of the standard 3).

The game will default to a hand of 12 cards with 4 diemsions and 3 options for each dimension ('dimension size'), as well as a standard set size of 3 cards. The user may chose to alter any of these settings, but must have at minimum a set size of 3 cards. To solve set with these default value, the user can just hit 'enter' at each prompt.

The solver will print out the player's hand as well as every possible set that can be made from that hand.

## Run the game
Please use Python3 to run this program. There are no other dependencies.
$ python set_solver.py

## Run unit tests
$ python -m unittest tests.py
