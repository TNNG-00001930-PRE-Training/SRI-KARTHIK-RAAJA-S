import unittest
from src.main.lab import even_or_odd

class TestEvenOrOdd(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(even_or_odd(2), "Even")
        self.assertEqual(even_or_odd(0), "Even")
        self.assertEqual(even_or_odd(-4), "Even")

    def test_odd_numbers(self):
        self.assertEqual(even_or_odd(1), "Odd")
        self.assertEqual(even_or_odd(-3), "Odd")
        self.assertEqual(even_or_odd(7), "Odd")

if __name__ == '__main__':
    unittest.main()
