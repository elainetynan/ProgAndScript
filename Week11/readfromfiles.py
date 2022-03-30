# readfrom sources.py
#
# Various ways to read in data to pandas

# Author: Andrew Beatty

import pandas as pd
import numpy as np
import re
import dataManipulation

filename = 'originalData.tsv'
workbookfilename = 'timetabledata.xlsx'
df = pd.read_table(filename)

df.to_excel(workbookfilename, sheet_name='activities', index=False)

ds_staff = dataManipulation.getSeriesOfUnique(df,'Staff (delimited)')

#print(ds_staff) # debug, I shuld use logging
# we have to use a different engine (openpyxl) to append the book
with pd.ExcelWriter(workbookfilename, engine='openpyxl', mode='a') as writer:
    ds_staff.to_excel(writer, sheet_name='staff', index=False)