'''String Operations:
Test cases for string concatenation
Test cases for string slicing
Test cases for string formatting
Test cases for string manipulation methods (e.g., upper(), lower(), strip(), replace())'''


import unittest

def concatenate_strings(str1, str2):
    return str1 + str2

def slice_string(string, start, end):
    return string[start:end]

def format_string(name, age):
    return f"My name is {name} and I am {age} years old."
    

def manipulate_string(string):
    return string.upper(), string.lower(), string.strip(), string.replace(' ', '_')

class TestStringOperations(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings('hello', 'world'), 'helloworld')
        self.assertEqual(concatenate_strings('Hi', 'Karthik'), 'HiKarthik')
        self.assertEqual(concatenate_strings('', 'test'), 'test')

    def test_slice_string(self):
        self.assertEqual(slice_string('hello world', 6, None), 'world')
        self.assertEqual(slice_string('python', None, 4), 'pyth')
        self.assertEqual(slice_string('goodbye', 2, 7), 'odbye')

    def test_format_string(self):
        self.assertEqual(format_string('Karthik', 24), 'My name is Karthik and I am 24 years old.')
        self.assertEqual(format_string('Raaja', 23), 'My name is Raaja and I am 23 years old.')

    def test_manipulate_string(self):
        self.assertEqual(manipulate_string('Hello World'), ('HELLO WORLD', 'hello world', 'Hello World', 'Hello_World'))
        self.assertEqual(manipulate_string('  Python is great  '), ('  PYTHON IS GREAT  ', '  python is great  ', 'Python is great', '__Python_is_great__'))

if __name__ == '__main__':
    unittest.main()
