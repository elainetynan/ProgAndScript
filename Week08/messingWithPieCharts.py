# messingWithPieCharts.py
#
# Messing with histograms
#
# Author: Andrew Beatty


import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(['Apples', 'Oranges', 'Bananas', 'Strawberries'])
numbers = np.array([23,77,500,100])

plt.pie(numbers, labels =fruit)
plt.title("Pie Chart")
plt.legend(fruit)
plt.show()
plt.savefig("MyFirstPieChart.png")