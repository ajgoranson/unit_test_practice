import unittest
from unittest import TestCase

import camel_case

# Adding a test class
class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camel_case.camel_case('Hello World'))

    def test_empty_string_value_error(self):
        with self.assertRaises(ValueError):
             camel_case.camel_case('') 

    def test_string_with_numbers(self):
        with self.assertRaises(ValueError):
             camel_case.camel_case('1532') 




if __name__ == '__main__':
    unittest.main()
