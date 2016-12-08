# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:58:00 2016

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import os

os.getcwd()

# **** Histogram ****

matplotlib.style.use('ggplot') # Look pretty

df = pd.read_csv("Module3\Datasets\wheat.data")

df.head()
df.describe()
df.wheat_type.unique()

df.asymmetry.plot.hist(title='Asymmetry', bins = 6)

plt.show()

# **** Multiple histograms ****

plt.figure()
df[df.wheat_type=='kama'].asymmetry.plot.hist(alpha=0.3)
df[df.wheat_type=='canadian'].asymmetry.plot.hist(alpha=0.6)
df[df.wheat_type=='rosa'].asymmetry.plot.hist(alpha=0.6)
plt.show()

# **** 2D scatter plot

df2=pd.read_csv("Module3\Datasets\Concrete_Data.csv")

df2.head()
df2.plot.scatter(x='Cement', y='Strength')
plt.suptitle('Cement content vs strength')
plt.xlabel('Cement')
plt.ylabel('Strength')

# **** 3D scatter plot

fig = plt.figure()
plt.suptitle('Cement x H2O x Strength')
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Cement content')
ax.set_ylabel('Water content')
ax.set_zlabel('Strength')
ax.scatter(df2.Cement, df2.Water,df2.Strength,c = 'r', marker='o')

plt.show()


