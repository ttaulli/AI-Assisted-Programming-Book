import unittest
from tests import calculate


class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate('add', 2, 3), 5)
        self.assertEqual(calculate('add', -1, 1), 0)
        self.assertEqual(calculate('add', 0, 0), 0)
        self.assertEqual(calculate('add', 2.5, 3.5), 6.0)

    def test_subtract(self):
        self.assertEqual(calculate('subtract', 5, 3), 2)
        self.assertEqual(calculate('subtract', 1, 1), 0)
        self.assertEqual(calculate('subtract', -1, -1), 0)
        self.assertEqual(calculate('subtract', 5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(calculate('multiply', 2, 3), 6)
        self.assertEqual(calculate('multiply', -2, 3), -6)
        self.assertEqual(calculate('multiply', 0, 5), 0)
        self.assertEqual(calculate('multiply', 2.5, 2), 5.0)

    def test_divide(self):
        self.assertEqual(calculate('divide', 6, 3), 2)
        self.assertEqual(calculate('divide', -6, 3), -2)
        self.assertEqual(calculate('divide', 0, 5), 0)
        self.assertEqual(calculate('divide', 5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate('divide', 6, 0)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate('modulus', 6, 3)
        with self.assertRaises(ValueError):
            calculate('', 1, 2)
        with self.assertRaises(ValueError):
            calculate(None, 1, 2)

    def test_invalid_input_types(self):
        with self.assertRaises(TypeError):
            calculate('add', 'string', 3)
        with self.assertRaises(TypeError):
            calculate('add', 2, 'string')
        with self.assertRaises(TypeError):
            calculate('add', None, 3)
        with self.assertRaises(TypeError):
            calculate('add', 2, None)

if __name__ == '__main__':
    unittest.main()