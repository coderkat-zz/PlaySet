"""Unit tests for set.py."""
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
        self.default_dimension_count = constants.DIMENSION_COUNT
        self.default_dimension_size = constants.DIMENSION_SIZE

    def test_n_cards_are_returned(self):
        """Test that we get the expected number of cards back in deck."""
        player_deck = get_cards(
            self.default_card_count,
            self.default_dimension_count,
            self.default_dimension_size)
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
            self.default_dimension_count + 2,
            self.default_dimension_size,
        )
        self.assertEqual(len(player_deck[0]), 6)

    def test_get_cards_with_var_dimension_size_works(self):
        """Test passing dimension_size beyond default works as expected."""
        player_deck = get_cards(
            self.default_card_count,
            self.default_dimension_count,
            self.default_dimension_size + 2
        )
        self.assertEqual(len(player_deck), self.default_card_count)
        self.assertEqual(len(player_deck[0]), constants.DIMENSION_COUNT)


class TestIsValidSet(unittest.TestCase):
    """Tests for is_valid_set function."""

    def setUp(self):
        """Some setup for constants."""
        self.dimension_count = constants.DIMENSION_COUNT

    def test_is_valid_false_when_only_two_shared_dimensions(self):
        """Test set validity function returns False when not a set.

        In the default configuration (where we have 3 dimensions), if
        two cards (but not three) share any one dimension, the set
        is invalid.
        """
        invalid_set = [
            ('red', 'oval', 'solid', '1'),
            ('red', 'diamond', 'solid', '2'),
            ('green', 'diamon', 'solid', '3')
        ]
        self.assertEqual(
            is_valid_set(invalid_set, self.dimension_count),
            False
        )

    def test_is_valid_when_set_rules_followed(self):
        """Test set validity function returns True when is a set."""
        valid_set = [
            ('red', 'oval', 'solid', '1'),
            ('red', 'oval', 'striped', '2'),
            ('red', 'oval', 'outlined', '3')
        ]
        self.assertEqual(
            is_valid_set(valid_set, self.dimension_count),
            True
        )

    def test_is_valid_longer_dimension_count(self):
        """Test set validity on a set with more than 4 card dimensions.

        i.e. this method should work as expected even if we add a new
        dimension to our cards, like a background color.
        """
        new_set = [
            ('red', 'oval', 'solid', '1', 'grey'),
            ('red', 'oval', 'striped', '2', 'white'),
            ('red', 'oval', 'outlined', '3', 'tan')
        ]
        self.assertEqual(
            is_valid_set(new_set, self.dimension_count + 1),
            True
        )

    def test_is_valid_larger_dimension_size(self):
        """Test set validity on a set with a dimension size of 4."""
        # Create a set where the dimension size is 4
        new_valid_set = [
            (3, 0, 0, 3),
            (3, 1, 3, 2),
            (3, 2, 1, 0),
        ]
        self.assertEqual(
            is_valid_set(new_valid_set, self.dimension_count),
            True
        )

    def test_is_not_valid_larger_dimensions_size(self):
        """Test set validity on an invalid set with dimension size of 4."""
        new_invalid_set = [
            (3, 0, 0, 3),
            (3, 1, 3, 2),
            (3, 0, 1, 2),
        ]
        self.assertEqual(
            is_valid_set(new_invalid_set, self.dimension_count),
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
            is_valid_set(big_valid_set, self.dimension_count),
            True
        )

    def test_not_is_valid_on_larger_set_size(self):
        """Test an invalid set larger than 3 is not valid."""
        big_invalid_set = [
            (3, 3, 2, 1),
            (1, 3, 0, 3),
            (1, 3, 2, 2),
            (0, 3, 2, 0),
        ]
        self.assertEqual(
            is_valid_set(big_invalid_set, self.dimension_count),
            False
        )


if __name__ == '__main__':
    unittest.main()
