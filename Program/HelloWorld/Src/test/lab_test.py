import unittest
from src.main.lab import Lab

class HelloWorldTest(unittest.TestCase):
    def setUp(self):
        try:
            self.hw = Lab()
        except Exception as e:
            self.fail(f"Failed to initialize Lab: {e}")

    def test_hello(self):
        """
        Method sayHello() must return "Hello, World!". This test ignores whitespace differences.
        """
        expected = "Hello, World!"
        actual = self.hw.sayHello()
        self.assertEqual(expected, actual, "Strings are not equal")

if __name__ == '__main__':
    unittest.main()