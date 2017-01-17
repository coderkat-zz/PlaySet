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
            constants.HAND_SIZE
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

    def test_get_cards_with_var_dimension_size_works(self):
        """Test passing attr_size beyond default works as expected."""
        player_deck = get_cards(
            self.default_card_count,
            self.default_attr_count,
            self.default_attr_size + 2
        )
        self.assertEqual(len(player_deck), self.default_card_count)
        self.assertEqual(len(player_deck[0]), constants.DIMENSION_COUNT)


class TestIsValidSet(unittest.TestCase):
    """Tests for is_valid_set function."""

    def setUp(self):
        """Set up for tests.

        Create some dummy sets for testing, using
        4-attribute, 3-card sets. Values could be anything here,
        as the program is agnostic and should work on strings as
        well as integers.
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

        In the default configuration (where we have 3 attributes), if
        two cards (but not three) share any one attribute, the set
        is invalid.
        """
        self.assertEqual(
            is_valid_set(self.invalid_set, self.attr_count),
            False
        )

    def test_is_valid_when_set_rules_followed(self):
        """Test set validity function returns True when is a set."""
        self.assertEqual(
            is_valid_set(self.valid_set, self.attr_count),
            True
        )

    def test_is_valid_longer_attribute_count(self):
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
            is_valid_set(new_set, self.attr_count + 1),
            True
        )

    def test_is_valid_larger_attribute_size(self):
        """Test set validity on a set with a dimension size of 4."""
        # Create a set where the dimension size is 4
        new_valid_set = [
            (3, 0, 0, 3),
            (3, 1, 3, 2),
            (3, 2, 1, 0),
        ]
        self.assertEqual(
            is_valid_set(new_valid_set, self.attr_count),
            True
        )

    def test_is_not_valid_larger_attribute_size(self):
        """Test set validity on an invalid set with dimension size of 4."""
        new_invalid_set = [
            (3, 0, 0, 3),
            (3, 1, 3, 2),
            (3, 0, 1, 2),
        ]
        self.assertEqual(
            is_valid_set(new_invalid_set, self.attr_count),
            False
        )

    def test_is_valid_on_arbitrary_num_of_cards(self):
        """Test passing an arbitrary number of cards to is_valid."""
        big_valid_set = [
            (3, 3, 2, 1),
            (1, 3, 2, 3),
            (2, 3, 2, 2),
            (0, 3, 2, 0),
        ]
        self.assertEqual(
            is_valid_set(big_valid_set, self.attr_count),
            True
        )


if __name__ == '__main__':
    unittest.main()
