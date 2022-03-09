# questions8To10.py
#
# Makes a list called ages that has, the same number random values
# as salaries, (range:21 to 65) . Make scatter plot of this data.
#
# Add a line to the plot that shows y= x2 in a different colour and 
# add a legend, title and axis labels to this plot. Finally save 
# this to a file called “prettier-plot.py”
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

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

#plt.plot(xpoints, ypoints, color = 'g')
plt.plot(xpoints, ypoints, color = 'g', label = "x-squared")
plt.title("Random Plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()

#plt.show()
plt.savefig("prettier-plot.png")