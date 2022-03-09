# question13.py
#
# Creating plots from real data
#
# Author: Elaine Tynan

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

filename = 'beverageSales.txt'

count = 1
legends = []
temperatureList = []
salesList = []
with open(filename, "rt") as f:
    for line in f:
        line = line.replace("\n", "") # https://stackoverflow.com/questions/17658055/how-can-i-remove-carriage-return-from-a-text-file-with-python
        allFields = line.split(",") # https://www.w3schools.com/python/ref_string_split.asp
        if count == 1:
            legends.append(allFields[0])
            legends.append(allFields[1])
        else:
            temperatureList.append(int(allFields[0]))
            salesList.append(int(allFields[1]))
        count += 1

print(legends)

temperatures = np.array(temperatureList)
sales = np.array(salesList)

plt.plot(salesList, temperatureList)

plt.title("Beverage Sales")
plt.xlabel("Sales")
plt.ylabel("Temperature")
plt.xticks(rotation=90) # https://www.adamsmith.haus/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python
plt.legend(legends)

plt.show()