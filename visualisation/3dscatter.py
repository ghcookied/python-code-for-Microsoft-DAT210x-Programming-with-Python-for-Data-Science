# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:30:44 2016

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

# **** 3D scatter plot

df2=pd.read_csv("Datasets\Concrete_Data.csv")

fig = plt.figure()
plt.suptitle('Cement x H2O x Strength')
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('Cement content')
ax.set_ylabel('Water content')
ax.set_zlabel('Strength')
ax.scatter(df2.Cement, df2.Water,df2.Strength,c = 'r', marker='o')

plt.show()


