from Util import Utilities                                        #importing  Class Utilities
import unittest                                                   # importing Unittest module
from unittest import TestCase                                     #importing TestCase from unittest

class DayofWeek(TestCase):

    def test_dayofWeekTrue(self):                                 #function to test daysofWeek
        result = Utilities.dayofWeek(14,6,2019)                   #storing the result
        expected = "Friday"
        self.assertTrue(expected, result)                         #Checking result and expected With True Function

    def test_dayofWeekFalse(self):                                 #function to test daysofWeek
        result =Utilities.dayofWeek(14,6,2019)                     #storing the result
        expected = False
        self.assertFalse(expected, result)                         #Checking result and expected With False Function

if __name__ == '__main__':
    unittest.main()
