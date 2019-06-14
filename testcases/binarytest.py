from Util import Utilities                                        #importing  Class Utilities
import unittest                                                    # importing Unittest module

class TestBinarysearch(unittest.TestCase):

    def testbinary_search_possitive(self):                         # function to test binarysearch of posotive number
        result = Utilities.binary_search(1,4,3,[1,2,3,4,5,6])      # call the uitlites class and storing the result
        expected = 1
        self.assertEqual(expected, result)                         # Checking result and expected With Equal Function


if __name__ == '__main__':
    unittest.main()