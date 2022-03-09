# messingWithHist.py
#
# Messing with histograms
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1) # Seed it to get the same numbers every time it is run

# This won't look normalised if the size is too small, e.g., 100
normData = np.random.normal(size=100)

plt.hist(normData)
plt.title("Histogram")
plt.show()
plt.savefig("MyFirstHistogram.png")