import unittest

from L8 import *


class SyntaxTest(unittest.TestCase):

    def test_syntax_correct(self):

        self.assertEqual(syntax_control("Ha3"), "Formeln följer korrekt syntax!")
    
    def test_no_uppercase(self):

        self.assertEqual(syntax_control("ha3"), "En stor bokstav saknas!")

    def test_digit(self):

        self.assertEqual(syntax_control("Ha1"), "Siffran måste vara större än 1!")

    def test(self):

        self.assertEqual(syntax_control("HH3"), "SyntaxFel")

    def test_3(self):

        self.assertEqual(syntax_control("Ha1a"), "SyntaxFel")

if __name__ == '__main__':
    unittest.main()


