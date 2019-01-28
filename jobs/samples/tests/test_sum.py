#unit test script to test sum module under my_sum

import sys

sys.path.append('/home/user/workarea/projects/learn-pyspark/jobs/samples/')

import unittest

from calc import basic

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data=[1,2,3]
        result=basic.sum(data)
        self.assertEqual(result,6)
    def test_list_str(self):
        """
        Test that it can sum a list of strings
        """
        data=['ina','mina','dica']
        result=basic.sum(data)
        self.assertEqual(result,'inaminadica')

class TestSubstract(unittest.TestCase):
    def test_sub_int(self):
        """
        Test substraction of two integers
        """
        result=basic.substract(5,2)
        self.assertEqual(result,3)

if __name__=='__main__':
    unittest.main()
