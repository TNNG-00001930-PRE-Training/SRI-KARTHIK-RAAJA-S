import unittest
from src.main.lab import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    modulus_numbers
)

class TestArithmeticOperations(unittest.TestCase):
    def test_add_numbers(self):
        # Test addition of two numbers
        result = add_numbers(5, 3)
        self.assertEqual(result, 8)

    def test_subtract_numbers(self):
        # Test subtraction of two numbers
        result = subtract_numbers(10, 4)
        self.assertEqual(result, 6)

    def test_multiply_numbers(self):
        # Test multiplication of two numbers
        result = multiply_numbers(6, 7)
        self.assertEqual(result, 42)

    def test_divide_numbers(self):
        # Test division of two numbers
        result = divide_numbers(20, 5)
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        # Test division by zero should raise ValueError
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

    def test_modulus_numbers(self):
        # Test modulus of two numbers
        result = modulus_numbers(10, 3)
        self.assertEqual(result, 1)

    def test_modulus_by_zero(self):
        # Test modulus by zero should raise ValueError
        with self.assertRaises(ValueError):
            modulus_numbers(8, 0)

if __name__ == '__main__':
    unittest.main()
