import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import andrews_curves

# Look pretty...
matplotlib.style.use('ggplot')


#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..

os.getcwd()
os.chdir('C:/Users/David/Documents/Technology/Python/edX/DAT210x-master/Module3')

wheat_df  = pd.read_csv('Datasets/wheat.data')

wheat_df.describe()

#
# TODO: Drop the 'id'
# 
# .. your code here ..

wheat_df = wheat_df.drop(labels = ['id'], axis = 1)
wheat_df.head()

#
# TODO: Plot a parallel coordinates chart grouped by
# the 'wheat_type' feature. Be sure to set the optional
# display parameter alpha to 0.4
# 
# .. your code here ..

plt.figure()
andrews_curves(wheat_df, 'wheat_type')
plt.show()


