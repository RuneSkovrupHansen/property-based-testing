#!/bin/python3

import unittest

import awesome_math
import awesome_sort
import awesome_logger

class TestAwesomeMath(unittest.TestCase):

    def test_add_positive_numbers(self):
        a = 10
        b = 20
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_negative_numbers(self):
        a = -5
        b = -30
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_mix_numbers(self):
        a = 90
        b = -30
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_large_numbers(self):
        a = 600
        b = 123456789
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_negative_large_numbers(self):
        a = -750
        b = -978654321
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_zero_and_positive(self):
        a = 0
        b = 10
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_zero_and_negative(self):
        a = 0
        b = -10
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_zeros(self):
        a = 0
        b = 0
        self.assertEqual((a+b), awesome_math.add(a,b))

    def test_add_to_equal_zero(self):
        a = 10
        b = -10
        self.assertEqual((a+b), awesome_math.add(a,b))

class TestAwesomeSort(unittest.TestCase):

    def test_bubble_sort(self):
        array = [3, 2, 1, 4, 5]
        awesome_sort.bubble_sort(array)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def test_bubble_sort_no_elements(self):
        array = []
        awesome_sort.bubble_sort(array)
        self.assertEqual(array, [])

    def test_bubble_sort_one_element(self):
        array = [0]
        awesome_sort.bubble_sort(array)
        self.assertEqual(array, [0])

    def test_bubble_sort_multiple_same(self):
        array = [1, 2, 3, 1, 2, 3]
        awesome_sort.bubble_sort(array)
        self.assertEqual(array, [1, 1, 2, 2, 3, 3])

    def test_bubble_sort_large_numbers(self):
        array = [1, 5000, 60, 5, 7000]
        awesome_sort.bubble_sort(array)
        self.assertEqual(array, [1, 5, 60, 5000, 7000])

    def test_bubble_sort_length(self):
        array = [1, 50, 60, 5, 70]
        awesome_sort.bubble_sort(array)
        self.assertEqual(len(array), 5)

    def test_bubble_sort_length_no_elements(self):
        array = []
        awesome_sort.bubble_sort(array)
        self.assertEqual(len(array), 0)

class TestAwesomeLogger(unittest.TestCase):

    def get_error_code_message_is_valid_string(self):
        error_message = awesome_logger.get_error_code_message(1)
        self.assertIsInstance(error_message, str)
        self.assertEqual(len(error_message), 0)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
