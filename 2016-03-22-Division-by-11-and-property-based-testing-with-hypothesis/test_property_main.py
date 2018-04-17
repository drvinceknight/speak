import unittest
import main

from hypothesis import given
from hypothesis.strategies import integers

class TestDivisible(unittest.TestCase):

    @given(k=integers(min_value=1))
    def test_divisible_by_11(self, k):
        self.assertTrue(main.divisible_by_11(11 * k))
