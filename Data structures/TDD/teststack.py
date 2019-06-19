import unittest
from program3 import balanced


class BalanceP(unittest.TestCase):

    def testBalanced(self):
        result = balanced('mydata')
        expected = None
        self.assertEqual(result, expected)

    def testNotBalanced(self):
        result = balanced('mydata')
        expected = 1
        self.assertNotEqual(result, expected)


if __name__ == '__main__':
    unittest.main()