import Util                                                       #importing  Class Utilities
import unittest                                                   # importing Unittest module
from unittest import TestCase

class AnagramTest(unittest.TestCase):

    def testanagram_True(self):                                  #function to test anagram
        result = Util.Utilities.is_anagram("earth", "heart")     #Callin the Utiliies class module and storing the result
        expected = True
        self.assertTrue(expected, result)                        #Checking result and expected With True Function


    def testanagram_False(self):                                 # function to test anagram
        result = Util.Utilities.is_anagram("test", "sets")       # Calling the Utilities  calss and storing the result
        expected = False
        self.assertFalse(expected, result)                       # Checking result and expected With False Function

if __name__ == '__main__':
    unittest.main()