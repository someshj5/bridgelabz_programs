from Util import Utilities                              #importing  Class Utilities
import unittest                                         # importing Unittest module
from unittest import TestCase                           # importing TestCase from unittest

class Insertionsort(TestCase):
    try:
        def testinsertionsort_with_possitive_num(self):  # function to test insertion sort with array of +ve numbers
            result = (Utilities.insertionSort([12, 5, 45, 78, 1, 0]))  # Pass Array To Insertion Sort Function
            expected = [0, 1, 5, 12, 45, 78]  # Initialize Expected as Sorted Array
            self.assertEqual(expected, result)  # Checking result and expected With Equal Function
    except:
        print("Failed..")

    try:
        def testinsertion_sort_with_negative_num(self):  # function to test insertion sort with array of -ve numbers
            result = (Utilities.insertionSort([-1, 2, -2, 0, -1, -6]))
            expected = [-6, 0, -1, -1, 0, 2]
            self.assertNotEqual(expected, result)  # Checking result and expected With NotEqual Function
    except:
        print("Failed..")

    try:
        def testinsertion_sort_with_negative(self):
            result = (Utilities.insertionSort([-1, 6, 5, 0, -1, -6]))
            expected = [-6, -1, -1, 0, 5, 6]
            self.assertEqual(expected, result)  # Checking result and expected With Equal Function
    except:
        print("Failed..")


if __name__ == '__main__':
    unittest.main()
