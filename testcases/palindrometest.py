from Util import Utilities

import unittest
from unittest import TestCase

class Palindrometest(unittest.TestCase):

    def testpalindromeTrue(self):
        result = Utilities.Is_palindrome('mam')
        expected = True
        self.assertTrue(expected, result)

    def testpalindromeFalse(self):
        result = Utilities.Is_palindrome('am')
        expected = False
        self.assertTrue(expected, result)

if __name__ == '__main__':
    unittest.main()