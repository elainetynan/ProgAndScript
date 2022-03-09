# question7.py
#
# Makes a list called ages that has, the same number random values
# as salaries, (range:21 to 65) . Make scatter plot of this data.
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

min = 20000
max = 80001 # I put in 80001 in because the numpy randint does not include the max value
numEntries = 100
minAge = 21
maxAge = 66

np.random.seed(1)
salaries = np.random.randint(min, max, numEntries)
ages = np.random.randint(minAge, maxAge, numEntries)

plt.scatter(ages, salaries) # Very random scatterchart
plt.show()