'''
Created on Jun 13, 2017

Synopsis:
This is a testcase for factorial module using unittest module
    
@author: pneela
'''
import unittest
from src.root.pyconcpets.factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_negative(self):
        self.assertRaises(ValueError,factorial,-1)
    
    def test_secnnegative(self):                             
        with self.assertRaises(ValueError,msg="Negative number Expected"):
            factorial(-10)
        
    def test_value(self):
        self.assertEqual(factorial(5), 120, msg="Value didn't match")
    
    def test_zero(self):
        self.assertEqual(factorial(0), 1, msg="A non-zero value is passed")
        
    def test_maxrecurssion(self):
        with self.assertRaises(RecursionError,msg="A very large number is expected"):
            factorial(120000)
            
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity = 2 )