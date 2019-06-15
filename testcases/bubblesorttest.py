from Util import Utilities                                  #importing  Class Utilities
import unittest                                             # importing Unittest module
from unittest import TestCase                               # importing TestCase from unittest

class Test_Bubblesort_Program(TestCase):

    def test_bubblesort_with_possitive_array(self):         # function to test bubble sort with positive numbers
        result = Utilities.bubble_sort([12, 1, 0, 5, 4, 2])  # call the utilities class and storing the result
        expected = [0, 1, 2, 4, 5, 12]
        self.assertEqual(expected, result)                   # Checking result and expected With Equal Function

    def test_bubblesort_with_array(self):                     #function to test bubble_sort with array
        result = Utilities.bubble_sort([12, 1, 0, 5, 4, 2])
        expected = [0, 1, 2, 4, 5, 2]                        #
        self.assertNotEqual(expected, result)                   # Checking result and expected With NotEqual Function

    def test_bubblesort_with_True(self):                       # function to test bubble sort with True
        result = Utilities.bubble_sort([12, 1, 0, 5, 4, 2]), [0, 1, 2, 4, 5, 12] # call the utilities class and storing the result
        expected = True
        self.assertTrue(expected, result)                       # Checking result and expected With True Function



if __name__ == '__main__':
    unittest.main()