"""
INTL 550 - HW2 (Main run)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import numpy as np
import pandas as pd
import Function as fn

data = pd.read_csv('tjdata.csv')

data = data.set_index('year')

# calculating normalized version
data_n = (data - np.mean(data, axis=0) ) / np.std(data, axis=0)

# adding constant term
n = data.shape[0]
data.insert(1, 'const', n * [1])
data_n.insert(1, 'const', n * [1])

# running without normalizing 
beta, sterror, confidence = fn.reg(data['lifexp'], data[['const', 'gdp', 'school', 'birth']])

# running the normalized version
beta_n, sterror_n, confidence_n = fn.reg(data_n['lifexp'], data_n[['const', 'gdp', 'school', 'birth']])

# The end.