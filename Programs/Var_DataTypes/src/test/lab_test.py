import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.main.lab import (
    demonstrate_integer,
    demonstrate_float,
    demonstrate_boolean,
    demonstrate_tuple,
    demonstrate_string,
    demonstrate_set,
    demonstrate_dictionary,
    demonstrate_variable_scope,
    demonstrate_create_areas_list
)

class TestLab(unittest.TestCase):
    def test_demonstrate_integer(self):
    # Test if demonstrate_integer function returns an integer value
        with StringIO() as buffer, redirect_stdout(buffer):
            output = demonstrate_integer()
            self.assertIsInstance(output, int, "Output should be an integer")


    def test_demonstrate_float(self):
        # Test if demonstrate_float function prints a float value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_float()
            output = buffer.getvalue().strip()  # Get output as string
            if output:  # Check if output is not empty
                try:
                    float_output = float(output)
                    self.assertIsInstance(float_output, float, "Output should be a float")
                except ValueError:
                    self.fail("Output should be a float")

    def test_demonstrate_boolean(self):
        # Test if demonstrate_boolean function prints a boolean value
        with StringIO() as buffer, redirect_stdout(buffer):
            demonstrate_boolean()
            output = buffer.getvalue().strip()  # Get output as string
            if output:  # Check if output is not empty
                self.assertIsInstance(output, bool, "Output should be a boolean")


    def test_demonstrate_string(self):
        # Test if demonstrate_string function returns a string
        result = demonstrate_string()
        self.assertIsInstance(result, str, "Output should be a string")

    def test_demonstrate_tuple(self):
        # Test if demonstrate_tuple function returns a tuple
        result = demonstrate_tuple()
        self.assertIsInstance(result, tuple, "Output should be a tuple")


    def test_demonstrate_set(self):
    # Test if demonstrate_set function returns a set value
        with StringIO() as buffer, redirect_stdout(buffer):
            output = demonstrate_set()
            self.assertIsInstance(output, set, "Output should be a set")

    def test_demonstrate_dictionary(self):
    # Test if demonstrate_dictionary function returns a dictionary value
        with StringIO() as buffer, redirect_stdout(buffer):
            output = demonstrate_dictionary()
            self.assertIsInstance(output, dict, "Output should be a dictionary")



    def test_demonstrate_create_areas_list(self):
        # Get the list of areas
        areas = demonstrate_create_areas_list()

        # Define the expected list of areas
        expected_areas = [10, 20, 30, 40, 15]  # Assuming these are the predefined values

        # Check if the generated list matches the expected list
        self.assertEqual(areas, expected_areas, "List of areas does not match the expected list")
        # Check if the generated list is of type list
        self.assertIsInstance(areas, list, "Output should be a list")
        # Check if all elements in the list are integers
        for area in areas:
            self.assertIsInstance(area, int, "All elements in the list should be integers")

    def test_demonstrate_variable_scope(self):
        # Test if demonstrate_variable_scope function returns None
        result = demonstrate_variable_scope()
        self.assertIsNone(result, "Output should be None")

if __name__ == '__main__':
    unittest.main()
