"""
INTL 550 - HW2 (Regression function - test)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import unittest
import numpy as np
import pandas as pd
import Rfunction as fn

class RegTest(unittest.TestCase):
    """ Four different exemplary tests are done for Rfunction.py """

    def test_case(self):
        a, b, c = fn.reg(pd.DataFrame([1,0]), pd.DataFrame([0,1]))
        
        self.assertEqual(np.array([0.0]), np.array(a))
        self.assertEqual(np.array([1.0]), np.array(b))

    def type_error(self):
        with self.assertRaises(TypeError):
            fn.reg(pd.DataFrame(['5']), pd.DataFrame(['1', '34', '23']))
            
    def val_error(self):
        with self.assertRaises(ValueError):
            fn.reg(pd.Series(['5']), pd.Series(['1', '34', '23']))
            
    def attr_error(self):
        with self.assertRaises(AttributeError):
            fn.reg([5], [1, 34, 23])
      

if __name__ == '__main__':
  unittest.main()

# The end.