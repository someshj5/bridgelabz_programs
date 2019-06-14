from Util import Utilities                                   #importing  Class Utilities
import unittest                                              # importing Unittest module

class Monthlypayemnt(unittest.TestCase):

    def test_monthlypayment(self):                           #function to test monthly payment
        result = Utilities.calculatePayment(1200,1,13)       # storing the result
        expected = 107.18073085409955
        self.assertTrue(expected, result)                    # Checking result and expected With True Function

    def test_monthlypaymentNotequal(self):                   #function to test monthly payment
        result = Utilities.calculatePayment(1200,2,13)        # storing the result
        expected = 17.18073085409955
        self.assertNotEqual(expected,result)                 # Checking result and expected With NotEqual Function


if __name__ == '__main__':
    unittest.main()