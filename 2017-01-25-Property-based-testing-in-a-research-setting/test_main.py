import unittest
import main

class TestDivisible(unittest.TestCase):
    def test_divisible_by_11(self):
        for k in range(10):
            self.assertTrue(main.divisible_by_11(11 * k))
            self.assertFalse(main.divisible_by_11(11 * k + 1))

        # Some more examples
        self.assertTrue(main.divisible_by_11(121))
        self.assertFalse(main.divisible_by_11(123))
