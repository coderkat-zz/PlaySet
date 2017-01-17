"""Unit tests for set.py.

Need to test:

"""
import unittest

import constants
from set_solver import (
    get_cards,
    is_valid_set,
)


class TestGetCards(unittest.TestCase):
    """Tests for building out the set deck."""

    def setUp(self):
        """Some setup for constants."""
        self.default_card_count = constants.HAND_SIZE
        self.default_attr_count = constants.DIMENSION_COUNT
        self.default_attr_size = constants.DIMENSION_SIZE

    def test_n_cards_are_returned(self):
        """Test that we get the expected number of cards back in deck."""
        player_deck = get_cards(
            self.default_card_count,
            self.default_attr_count,
            self.default_attr_size)
        self.assertEqual(
            len(player_deck),
            self.default_card_count
        )

    def test_get_cards_handles_variable_dimensions(self):
        """Test that get_cards creates cards with the proper n dimensions.

        i.e. a card with 6 dimensions should have a length of 6.
        """
        player_deck = get_cards(
            self.default_card_count,
            self.default_attr_count + 2,
            self.default_attr_size,
        )
        self.assertEqual(len(player_deck[0]), 6)


class TestIsValidSet(unittest.TestCase):
    """Tests for is_valid_set function."""

    def setUp(self):
        """Set up for tests.

        Create some dummy sets for testing, using
        4-attribute, 3-card sets.
        """
        self.invalid_set = [
            ('red', 'oval', 'solid', '1'),
            ('red', 'diamond', 'solid', '2'),
            ('green', 'diamon', 'solid', '3')
        ]
        self.valid_set = [
            ('red', 'oval', 'solid', '1'),
            ('red', 'oval', 'striped', '2'),
            ('red', 'oval', 'outlined', '3')
        ]
        self.attr_count = constants.DIMENSION_COUNT
        self.attr_size = constants.DIMENSION_SIZE

    def test_is_valid_false_when_only_two_shared_attrs(self):
        """Test set validity function returns False when not a set.

        If two cards (but not three) share any one attribute, the set
        is invalid.
        """
        self.assertEqual(
            is_valid_set(self.invalid_set, self.attr_count, self.attr_size),
            False
        )

    def test_is_valid_when_set_rules_followed(self):
        """Test set validity function returns True when set."""
        self.assertEqual(
            is_valid_set(self.valid_set, self.attr_count, self.attr_size),
            True
        )

    def test_is_valid_longer_var_count(self):
        """Test set validity on a set with more than 4 card attributes.

        i.e. this method should work as expected even if we add a new
        attribute to our cards, like a background color.
        """
        new_set = [
            ('red', 'oval', 'solid', '1', 'grey'),
            ('red', 'oval', 'striped', '2', 'white'),
            ('red', 'oval', 'outlined', '3', 'tan')
        ]
        self.assertEqual(
            is_valid_set(new_set, self.attr_count + 1, self.attr_size),
            True
        )

if __name__ == '__main__':
    unittest.main()
