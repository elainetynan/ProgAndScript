# questions1To4.py
#
# Makes a list, called salaries, that has 10 random numbers (20000 – 80000).
#
# Author: Andrew Beatty

import numpy as np

min = 20000
max = 80001 # I put in 80001 in because the numpy randint does not include the max value

np.random.seed(1)
salaries = np.random.randint(min, max, 10)

salariesPlus = salaries + 5000

print(salaries)
print(salariesPlus)

salariesMult = salaries * 1.05
newSalaries = salariesMult.astype(int)
print(newSalaries)
'''
salariesMult = salariesMult.astype(int)
print(salariesMult)
'''