# question6.py
#
# Plots a histogram of the salaries (from Question 1)
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

min = 20000
max = 80001 # I put in 80001 in because the numpy randint does not include the max value
numEntries = 100

np.random.seed(1)
salaries = np.random.randint(min, max, numEntries)

plt.hist(salaries)
plt.show()