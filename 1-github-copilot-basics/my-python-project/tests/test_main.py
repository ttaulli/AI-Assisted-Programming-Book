import unittest
from src.main import *

class TestMain(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

    def test_multiply_numbers(self):
        result = multiply_numbers(4, 5)
        self.assertEqual(result, 20)

if __name__ == '__main__':
    unittest.main()