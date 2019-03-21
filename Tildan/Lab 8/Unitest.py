import unittest

from L8 import *


class SyntaxTest(unittest.TestCase):

    def testnumber(self):
        """ Testar siffra """
        self.assertEqual(number("3"), "Följer syntaxen!")

    def testfelnumber(self):
        """ testtar felaktig siffta """
        self.assertEqual(number("b"), "Följer ej syntaxen!")
        


if __name__ == '__main__':
    unittest.main()


