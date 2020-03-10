"""
INTL 550 - HW2 (Regression function - test)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import unittest
import pandas as pd
import Rfunction as fn

class RegTest(unittest.TestCase):
    """ Five different exemplary tests are done for FinModel.py """

#    def test_cash0(self):
#        self.assertEqual(0,f.Portfolio().cash)
        
    def type_error(self):
        with self.assertRaises(TypeError):
            fn.reg(pd.DataFrame(['5']), pd.DataFrame(['1', '34', '23']))
            
    def val_error(self):
        with self.assertRaises(ValueError):
            fn.reg(pd.Series(['5']), pd.Series(['1', '34', '23']))
            
    def attr_error(self):
        with self.assertRaises(AttributeError):
            fn.reg([5], [1, 34, 23])

#    def test_withdraw(self):
#        portfolio = f.Portfolio() 
#        portfolio.addCash(500)
#        portfolio.withdrawCash(495.5)
#        
#        self.assertEqual(4.5, portfolio.cash)
#
#    def test_bond(self):
#        portfolio = f.Portfolio() 
#        portfolio.addCash(200)
#        u = f.Bond(10, "QWE")
#        
#        self.assertEqual(10, u.price)
#        self.assertEqual("QWE", u.symbol)
#        self.assertEqual("bond", u.type)
#
#    def test_hw(self):
#        portfolio = f.Portfolio() 
#        portfolio.addCash(300.50) 
#        s = f.Stock(20, "HFH") 
#        portfolio.buyStock(5, s) 
#        mf1 = f.MutualFund("BRT") 
#        mf2 = f.MutualFund("GHT") 
#        portfolio.buyMutualFund(10.3, mf1) 
#        portfolio.buyMutualFund(2, mf2)
#        
#        self.assertNotEqual(10.33, mf1.quantity)
#        self.assertEqual(10.3, mf1.quantity)
#        
#        self.assertNotEqual(140.5, portfolio.cash)
#        self.assertEqual(188.2, portfolio.cash)
        

if __name__ == '__main__':
  unittest.main()

# The end.