# question5.py
#
# Plots the function y = x2.
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()