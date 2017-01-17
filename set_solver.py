"""Solve a game of set."""
import itertools
import random

import constants


def get_all_possible_cards(attributes):
    """Get every possible set card in the deck.

    This method takes a list of tuples, where each tuple
    is the set of attributes available for the card.
    """
    # Using python's itertools, create set (cartesian product)
    # of all possible cards: think of this as the full Set deck.
    full_deck = set(itertools.product(*attributes))

    return(full_deck)


def get_cards(n, dimension_count, dimension_size):
    """Get n number of set cards. Each card must be unique."""
    # Build list of card attributes, where each dimension
    # is a tuple of dimension_size options. This sets the
    # rules for each card in full_deck.
    attribute_list = []
    for i in range(dimension_count):
        attribute_list.append(tuple(i for i in range(dimension_size)))

    full_deck = get_all_possible_cards(attribute_list)

    # Select random n cards from full_deck to build player's deck.
    player_deck = random.sample(full_deck, n)

    # This returns a list of tuples where each inner list is,
    # in order, the card attributes passed to get_all_possible_cards.
    return(player_deck)


def is_valid_set(cards, dimension_count):
        """Check if the set is valid.

        This check uses set() on each group of card attributes
        to quickly eliminate duplicates. A group of matching
        attributes will have length 0, and a group of unique attributes
        will have length equal to whatever the size of our desired set is.
        """
        for i in range(dimension_count):
            # Since python's set() will remove duplicates and
            # is quick to construct/lookup, we use that to check if
            # either all attributes match across cards, or if none do.
            if 1 < len(set(card[i] for card in cards)) < len(cards):
                return(False)
        return(True)


def play_set(player_deck, dimension_count, set_size):
    """Given a set of cards, find all possible set combinations."""
    set_count = 0

    for cards in itertools.combinations(player_deck, set_size):
        if not is_valid_set(cards, dimension_count):
            continue
        set_count += 1
        print(("Set #{}:").format(set_count))
        for card in cards:
            print(card)

    # Explicit messaging if no sets are found
    if set_count == 0:
        print("No sets are possible with this hand.")


if __name__ == '__main__':
    # Prompt user for cards, dimension count, dimension size, and set size
    size_of_hand = int(input(
        constants.HAND_SIZE_PROMPT
    ) or constants.HAND_SIZE)

    if not constants.MIN_HAND_SIZE < size_of_hand < constants.MAX_HAND_SIZE:
        size_of_hand = constants.HAND_SIZE
        print(constants.HAND_SIZE_OUT_OF_RANGE_PROMPT)

    dimension_count = int(input(
        constants.DIMENSION_COUNT_PROMPT
    ) or constants.DIMENSION_COUNT)
    if dimension_count < constants.MIN_DIMENSION_COUNT:
        dimension_count = constants.DIMENSION_COUNT
        print(constants.DIMENSION_COUNT_TOO_SMALL_PROMPT)

    dimension_size = int(input(
        constants.DIMENSION_SIZE_PROMPT
    ) or constants.DIMENSION_SIZE)
    if dimension_size < constants.MIN_DIMENSION_SIZE:
        dimension_size = constants.DIMENSION_SIZE
        print(constants.DIMENSION_SIZE_TOO_SMALL_PROMPT)

    set_size = int(input(
        constants.SET_SIZE_PROMPT
    ) or constants.SET_SIZE)
    if set_size < constants.SET_SIZE:
        set_size = constants.SET_SIZE
        print(constants.SET_TOO_SMALL_PROMPT)

    # Display all cards in hand to user
    player_deck = get_cards(size_of_hand, dimension_count, dimension_size)
    print("Great! Here is your hand:")
    for card in player_deck:
        print(card)
    print('\n')

    # Find and print all viable sets from cards in hand.
    input("Press enter to see all possible sets made with this hand.\n")
    play_set(player_deck, dimension_count, set_size)
    print("\nThanks for playing!\n")
