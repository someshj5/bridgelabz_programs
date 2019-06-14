from Util import Utilities                 #importing  Class Utilities
import unittest                            # importing Unittest module
from unittest import TestCase              # importing TestCase from unittest

class TempConversion(TestCase):

    def test_tempconverTrue(self):          #function to test temperature conversion in Celcius
        result = Utilities.Temp_conversion(2100,0)  #storing the result
        expected =  1148.888888888889
        self.assertTrue(expected, result)   # Checking result and expected With True Function

    def test_tempconverFalse(self):            #function to test temperature conversion in Farheiniet
        result = Utilities.Temp_conversion(1148.888888888889,1)   #storing the result
        expected = 2100
        self.assertTrue(expected,result)        # Checking result and expected With True Function

if __name__ == '__main__':
    unittest.main()