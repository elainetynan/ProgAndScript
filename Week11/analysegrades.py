# in this program I do some basic analysis of the grades.csv
# author: Andrew Beatty

import pandas as pd
import matplotlib.pyplot as plt

# I made this var to make it easier to change the location of the files
path = '../data/'
filenameForGrades = path + 'grades.csv'

# there is an index col in this csv
df = pd.read_csv(filenameForGrades, index_col=0)
#print(df)

# get rid of nulls and duplicates
# we could have chained these calls
# df = df.dropna().drop_duplicates()
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
#print(df)

# select the highest grade for each subject for a student
df = df.pivot_table(values='grade',index=['name','subject'],aggfunc='max').reset_index()
#print(df)

# group by a value in a column
meanValues = df.groupby('name').mean()
#print(meanValues)

# values would default to any columns that are left so setting the
# values is unnecessary but here for information/learning
df = df.pivot(index='name',columns='subject',values='grade')
#print(df)

# print a corralation table 
print(df.corr())

# plot a bar graph
#df.plot.bar()

# I meant to say in the lecture if you want to plot a sub-set of the dataframe
# then just select the parts you want to plot
# eg

df[['math', 'SIEM']].plot.bar()

plt.show()