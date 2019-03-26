import unittest
from L9v2 import *

class TestStringMethods(unittest.TestCase):

    def test_upper1(self):
        self.assertEqual(readFormel("Na"), 'Formeln är syntaktiskt korrekt')

    def test_upper2(self):
        self.assertEqual(readFormel("H2O"), 'Formeln är syntaktiskt korrekt')
    
    def test_upper3(self):
        self.assertEqual(readFormel("Si(C3(COOH)2)4(H2O)7"), 'Formeln är syntaktiskt korrekt')

    def test_upper4(self):
        self.assertEqual(readFormel("Na332"), 'Formeln är syntaktiskt korrekt')

if __name__ == '__main__':
    unittest.main()

