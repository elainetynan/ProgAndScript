# messingWithPlots.py
#
# Messing with plots
#
# Author: Andrew Beatty

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.plot(xpoints, xpoints, label="straight", color="red")

#plt.show()
plt.legend("Legend")
plt.title("This is the title")

randompoints = np.random.randint(1,1000, 100)
plt.scatter(xpoints, randompoints, label="random")
plt.savefig("MyFirstPlot.png")