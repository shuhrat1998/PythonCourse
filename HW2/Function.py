"""
INTL 550 - HW2 (Regression function)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import numpy as np
import pandas as pd
from scipy.stats import t

def reg(y, x):
    n = x.shape[0]
    k = x.shape[1] # with constant term
    
    x2inv = np.linalg.inv(x.T @ x)
    
    B = x2inv @ (x.T @ y)
    e =  y - (x @ B)
    sigma2 = (e.T @ e) / (n - k) # constant term is included in k
    
    varB =np.diag( np.multiply(sigma2, x2inv) )
    seB = np.sqrt(varB)
    
    margin = seB * t.ppf(0.975, n-k)
    CI = [B-margin, B+margin]
    
    return B, seB, CI

# The end.