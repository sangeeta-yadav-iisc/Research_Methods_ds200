import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys


#reading data frame from a csv file

df=pd.read_csv('data_scatter.csv', header=None, names=['col1', 'col2','col3','col4','col5','col6'])
for index in range(0,50):
      df = df.drop(index)


#plot bar plot with xticks which is position of bars as first argument and height of bars as second argument
plt.bar(range(1,16),np.array(df['col2']).astype(np.float),color='#ddbbaa',label="export")

#specify labels on xticks
plt.xticks(range(1,16),df['col1'],rotation='vertical')
plt.xlabel("year")
plt.ylabel("export")

#enabling legend
plt.legend()
plt.show()
