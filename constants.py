"""Constant values for set_solver.py."""

# Default properties for a game of set.
HAND_SIZE = 12
DIMENSION_COUNT = 4
DIMENSION_SIZE = 3
SET_SIZE = 3

# Text for gameplay.
HAND_SIZE_PROMPT = """
    Enter the nuber of cards you wish to play with, between 3 and 81.
    If you wish to use the game default of 12, just press enter:
"""
DIMENSION_COUNT_PROMPT = """
    Enter the number of unique dimensions each card has.
    For example, if your cards have color, shading, shape,
    background, and count, enter 5.
    If you wish to use the game default of 4, just press enter:
"""
DIMENSION_SIZE_PROMPT = """
    Enter the number of possible items in each dimension.
    For example, if there are 5 possible colors, enter 5.
    If you wish to use the game default of 3, just press enter:
"""
SET_SIZE_PROMPT = """
    Enter the number of cards required to make a set, greater than 3.
    If you wish to use the game default of 3, just press enter:
"""
SET_TOO_SMALL_PROMPT = """
    Sorry, Set cannot be played with fewer than {size} cards to a set!
    We've set your set size to the default of {size}.
""".format(size=SET_SIZE)
