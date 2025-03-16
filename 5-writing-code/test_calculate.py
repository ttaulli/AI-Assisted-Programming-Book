import unittest
from test import *


class TestCalculate(unittest.TestCase):
    def test_add(self):
        # Intentionally incorrect expected value to make the test fail
        self.assertEqual(calculate('add', 2, 3), 6)

    def test_subtract(self):
        self.assertEqual(calculate('subtract', 5, 3), 2)

    def test_multiply(self):
        self.assertEqual(calculate('multiply', 2, 3), 6)

    def test_divide(self):
        self.assertEqual(calculate('divide', 6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate('divide', 6, 0)

    def test_unsupported_operation(self):
        with self.assertRaises(ValueError):
            calculate('modulus', 6, 3)

if __name__ == '__main__':
    unittest.main()

