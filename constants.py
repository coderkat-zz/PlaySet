"""Constant values for set_solver.py."""

# Default properties for a game of set.
MIN_HAND_SIZE = 3
MAX_HAND_SIZE = 81
HAND_SIZE = 12

MIN_DIMENSION_COUNT = 3
DIMENSION_COUNT = 4

MIN_DIMENSION_SIZE = 2
DIMENSION_SIZE = 3

SET_SIZE = 3

# Text for gameplay.
HAND_SIZE_PROMPT = """
    Enter the nuber of cards you wish to play with, between 3 and 81.
    If you wish to use the game default of 12, just press enter:
"""
HAND_SIZE_OUT_OF_RANGE_PROMPT = """
    Sorry, you must have a hand size of at least 3 cards
    and no more than 81 cards.
    We've set your hand size to the default of {size}.
""".format(size=HAND_SIZE)

DIMENSION_COUNT_PROMPT = """
    Enter the number of unique dimensions each card has (no less than 3).
    For example, if your cards have color, shading, shape,
    background, and count, enter 5.
    If you wish to use the game default of 4, just press enter:
"""
DIMENSION_COUNT_TOO_SMALL_PROMPT = """
    Sorry, each card needs to have at least 3 distinct dimensions
    in order to play Set.
    We've set your dimension count to the default of {count}.
""".format(count=DIMENSION_COUNT)

DIMENSION_SIZE_PROMPT = """
    Enter the number of possible items in each dimension (no less than 2).
    For example, if there are 5 possible colors, enter 5.
    If you wish to use the game default of 3, just press enter:
"""
DIMENSION_SIZE_TOO_SMALL_PROMPT = """
    Sorry, dimension must have at least 2 options.
    We've set your dimension size to the default of {size}.
""".format(size=DIMENSION_SIZE)

SET_SIZE_PROMPT = """
    Enter the number of cards required to make a set, no less than 3.
    If you wish to use the game default of 3, just press enter:
"""
SET_TOO_SMALL_PROMPT = """
    Sorry, Set cannot be played with fewer than {size} cards to a set!
    We've set your set size to the default of {size}.
""".format(size=SET_SIZE)
