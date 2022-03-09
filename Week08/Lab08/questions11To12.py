# questions11To12.py
#
# Makes a list called ages that has, the same number random values
# as salaries, (range:21 to 65) . Make scatter plot of this data.
#
# Add a line to the plot that shows y= x2 in a different colour.
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

possibleCounties = ['Lierick', 'Wicklow', 'Westmeath', 'Galway','Mayo']
counties = np.random.choice(
    possibleCounties,
    p=[0.4, 0.15, 0.2, 0.07, 0.18],
    size = 100
)

# This returns a tuple of the unique values (counties) and how many times they appear
unique, counts = np.unique(counties, return_counts=True)

# Plot on pie chart
plt.figure(1) # found this on https://matplotlib.org/stable/gallery/subplots_axes_and_figures/multiple_figs_demo.html
plt.pie(counts, labels=unique)
plt.show()

plt.figure(2)
plt.bar(unique, counts)
plt.show()