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
            temperatureList.append(allFields[0])
            salesList.append(allFields[1])
        count += 1

print(legends)

temperatures = np.array(temperatureList)
sales = np.array(salesList)

# Try to set axes before plotting
# https://subscription.packtpub.com/book/big_data_/9781849513265/3/ch03lvl1sec48/controlling-tick-spacing
#ax  = plt.axes()
#ax.xaxis.set_major_locator(ticker.MultipleLocator(500))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(250))

plt.plot(salesList, temperatureList)

#specify x-axis labels
# https://www.statology.org/set-x-axis-values-matplotlib/
#xTicks = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500] 
#add x-axis values to plot
#plt.xticks(ticks=xTicks)


plt.title("Beverage Sales")
plt.xlabel("Sales")
plt.ylabel("Temperature")
plt.xticks(rotation=90) # https://www.adamsmith.haus/python/answers/how-to-rotate-axis-labels-in-matplotlib-in-python
plt.legend(legends)

plt.show()