"""
INTL 550 - HW2 (Main run)
Name : Shukhrat Khuseynov
ID   : 0070495
"""

import numpy as np
import pandas as pd
import Rfunction as fn
import matplotlib.pyplot as plt

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
output = pd.DataFrame([beta, sterror, confidence[0], confidence[1]])
output.columns = ['Bi', 'SEi', 'CI1', 'CI2']
print("\n(Initial)\n", output)

# running the normalized version
beta_n, sterror_n, confidence_n = fn.reg(data_n['lifexp'], data_n[['const', 'gdp', 'school', 'birth']])
output_n = pd.DataFrame([beta_n, sterror_n, confidence_n[0], confidence_n[1]])
output_n.columns = ['Bi', 'SEi', 'CI1', 'CI2']
print("\n(Normalized)\n", output_n)

# plotting
i = np.array([0,1,2,3])

# plot for beta (initial version)
plt.plot(i, beta, 'o')
plt.vlines(ymin = confidence[0], ymax = confidence[1], x=i, linestyle = '-')
plt.title("Beta estimates and confidence interval (initial).", loc = 'center')
plt.xlabel("- i -")
plt.xticks(np.arange(0, 4, 1.0))
plt.ylabel("- Bi -")
plt.show()

# plot for beta (initial version - closer)
plt.plot(i[1:], beta[1:], 'o')
plt.vlines(ymin = confidence[0][1:], ymax = confidence[1][1:], x=i[1:], linestyle = '-')
plt.title("Beta estimates and confidence interval (initial) - closer.", loc = 'center')
plt.xlabel("- i -")
plt.xticks(np.arange(0, 4, 1.0))
plt.ylabel("- Bi -")
plt.show()

# plot for beta (using normalized version)
plt.plot(i, beta_n, 'o')
plt.vlines(ymin = confidence_n[0], ymax = confidence_n[1], x=i, linestyle = '-')
plt.title("Beta estimates and confidence interval (normalized).", loc = 'center')
plt.xlabel("- i -")
plt.xticks(np.arange(0, 4, 1.0))
plt.ylabel("- Bi -")
plt.show()

# The end.