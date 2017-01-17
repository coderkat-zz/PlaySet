"""Solve a game of set."""
import sys

import itertools
import random


# TODO: later, this will need to accept *args
def get_all_possible_cards(colors, symbols, shading, symbol_count):
    """Get every possible set card in the deck.

    This method takes a list of tuples, where each tuple
    is the set of attributes available for the card, i.e.:
    [('red', 'green', 'purple'), ('heart', 'diamond', 'squiggle')...]
    """
    # using itertools, create set of all options
    # itertools is python's awesome builtin way to do cartesian product.
    # TODO: is there a more efficient way to do this in python?
    # May require implemending a generator like before...
    full_deck = set(itertools.product(colors, symbols, shading, symbol_count))

    return(full_deck)


def get_cards(n):
    """Get n number of set cards. Each card must be unique.

    Returns a list of lists representing the deck of cards.
    TODO: find a better/faster data structure that makes sense.
    Figure out how to use a set of tuples?!? works great b/c tuples are
    immutable...
    """
    # FOR NOW, hard code this. Later we'll make this something a user
    # can change.
    colors = ('red', 'green', 'purple')
    symbols = ('squiggle', 'diamond', 'oval')
    shading = ('solid', 'striped', 'outlined')
    symbol_count = ('1', '2', '3')

    # Full_deck is a set...
    full_deck = get_all_possible_cards(colors, symbols, shading, symbol_count)

    # Select random n cards from set_option to build player's deck

    # player deck will be list b/c of how random.sample works.
    # TODO: if this needs to be a set, can just cast list of tuples
    # to set()
    player_deck = random.sample(full_deck, n)

    # This returns a list of tuples where each inner list is, in order,
    # the card attributes passed to get_all_possible_cards.
    # TODO: find a nicer way to display this to user.
    print(("Player deck: \n {player_deck} \n").format(player_deck=player_deck))
    return(player_deck)


def is_valid_set(cards, attr_count):
        """Check if the set is valid.

        This check uses set() on each group of card attributes
        to quickly eliminate duplicates. A group of matching
        attributes will have length 0, and a group of unique attributes
        will have length 3 (or whatever attr_number is, to implement later)
        """
        for i in range(attr_count):
            # any time that ONLY 2 cards have different attributes, we don't
            # have a set. Since python's set() will remove duplicates and
            # is quick to construct/lookup, we use that.
            # i.e. if 3 attributes are shared, len will == 0,
            # if all three are different, len will == 3.
            # TODO: how does this need to change to allow for an
            # arbitrary number of attributes? == attr_number-1 I THINK.
            if len(set(card[i] for card in cards)) == 2:
                return(False)
        return(True)


def play_set(player_deck):
    """Given a set of cards, find all possible set combinations."""
    # iterate over every pair (use itertools, look into itertools.combination)
    # This is going to be a recursive solution (hopefully using conbination!)
    # itertools.combinations(p[, r]) returns r-length tuples, in sorted order,
    # with no repeated elements

    # TODO: pass in attr_count as a var if we want to allow a larger or var set
    attr_count = 4

    # TODO: return the number of sets, then show them.
    # TODO: think about the best way to return this information,
    # also remember that isn't very important in the grand scheme
    # of the problem. But move print statements out of functions and
    # into main() program runner.
    set_count = 0
    for cards in itertools.combinations(player_deck, 3):
        if not is_valid_set(cards, attr_count):
            continue
        set_count += 1
        print(("Set #{}:").format(set_count))
        for card in cards:
            print(card, end="\n")
        # print()


if __name__ == '__main__':
    # Handle missing args gracefully.
    if not len(sys.argv) == 2:
        print("""
            This program requires you to pass in the number of cards you
            wish to play with as an argument, i.e.:

            $ python3 set_solver.py 12

            Please try again!
        """)
    else:
        player_deck = get_cards(int(sys.argv[1]))
        play_set(player_deck)
