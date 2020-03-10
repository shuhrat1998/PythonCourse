"""
INTL 550 - HW2 (Data collection)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import numpy as np
import pandas as pd
from pandas_datareader import wb # World Bank API from pandas_datareader

matches1 = wb.search('life expectancy') # choosing SP.DYN.LE00.IN
 
matches2 = wb.search('gdp per capita') # choosing NY.GDP.PCAP.CD 

matches3 = wb.search('school enrollment') # choosing SE.PRE.ENRR

matches4 = wb.search('birth rate') # choosing SP.DYN.CBRT.IN

df = wb.download(indicator=['SP.DYN.LE00.IN', 'NY.GDP.PCAP.CD', 'SE.PRE.ENRR', 'SP.DYN.CBRT.IN'], country='TJ', start=1990, end=2020)

# formatting the table
df.columns = ['lifexp', 'gdp', 'school', 'birth']
df = df[::-1] # reverting the data
df = df.dropna()
print(df)

# deleting unneeded column before exporting to csv
df = df.reset_index('country')
df = df.drop('country', axis=1)

df.to_csv('tjdata.csv')

# The end.