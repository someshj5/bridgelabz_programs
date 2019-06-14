import Util

import unittest
from unittest import TestCase



class AnagramsTesting(TestCase):

    def anagram_True(self):
        result = Util.Utilities.is_anagram("earth", "heart")
        expected = True
        self.assertTrue (expected, result)


    def anagram_False(self):
        result = Util.Utilities.is_anagram("test", "sets")
        expected = False
        self.assertFalse(expected, result)

if __name__ == '__main__':
    unittest.main()