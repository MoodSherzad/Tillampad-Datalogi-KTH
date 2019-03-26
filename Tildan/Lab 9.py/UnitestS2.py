import unittest
from L9v2 import *

class TestStringMethods(unittest.TestCase):

    def test_upper1(self):
        self.assertEqual(readFormel("C(Xx4)5"), 'Okänd atom vid radslutet 4)5')

    def test_upper2(self):
        self.assertEqual(readFormel("C(OH4)C"), 'Saknad siffra vid radslutet C')
    
    def test_upper3(self):
        self.assertEqual(readFormel("C(OH4C"), 'Saknad högerparentes vid radslutet ')
"""
    def test_upper4(self):
        self.assertEqual(readFormel("H2O)Fe"), 'Felaktig gruppstart vid radslutet )Fe') # FEL
"""
    def test_upper5(self):
        self.assertEqual(readFormel("H0"), 'För litet tal vid radslutet ')


    def test_upper6(self):
        self.assertEqual(readFormel("H1C"), 'För litet tal vid radslutet C')

    def test_upper7(self):
        self.assertEqual(readFormel("H02C"), 'För litet tal vid radslutet 2C')
    def test_upper8(self):
        self.assertEqual(readFormel("Nacl"), 'Saknad stor bokstav vid radslutet cl')
    def test_upper9(self):
        self.assertEqual(readFormel("a"), 'Saknad stor bokstav vid radslutet a')

"""
    def test_upper10(self):
        self.assertEqual(readFormel("(Cl)2)3"), 'Felaktig gruppstart vid radslutet )3') #FEL
"""
    def test_upper11(self):
        self.assertEqual(readFormel(")"), 'Felaktig gruppstart vid radslutet )')
    def test_upper12(self):
        self.assertEqual(readFormel("2"), 'Felaktig gruppstart vid radslutet 2')
    
if __name__ == '__main__':
    unittest.main()

