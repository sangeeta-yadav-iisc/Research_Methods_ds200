import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
#create dataframe
df=pd.read_csv('data_scatter.csv', header=None, names=['col1', 'col2','col3','col4','col5','col6'])
df=df.dropna(axis=0, how='any')
df=df.drop(0)

#plot scatter with first column as x values and second column as y values
plt.scatter(np.array(df['col2']).astype(np.float),np.array(df['col3']).astype(np.float),color='#dd12dd')

#specifying labels
plt.xlabel("export")
plt.ylabel("import")
plt.xticks(rotation='vertical')
#enable legend
plt.legend()
plt.show()
