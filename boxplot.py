import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
#create dataframe from csv
df=pd.read_csv('data_scatter.csv', header=None, names=['col1', 'col2','col3','col4','col5','col6'])
df = df.dropna(axis=0,how='any').drop(0)
plotMap=[]

#create a list of lists where each list will have a corresponding box plot
plotMap.append(np.array(df['col2']).astype(np.float).tolist())
plotMap.append(np.array(df['col3']).astype(np.float).tolist())

#plotting
plt.boxplot(plotMap)

#specifying labels
plt.xticks([1,2],["Exports","Imports"])
plt.ylabel("in Crores")


plt.legend()
plt.show()
