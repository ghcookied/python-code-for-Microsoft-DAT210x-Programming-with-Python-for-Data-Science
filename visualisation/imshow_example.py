import pandas as pd
import matplotlib.pyplot as plt
import os


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
# TODO: Drop the 'id' feature
# 
# .. your code here ..

wheat_df = wheat_df.drop(labels = ['id'], axis = 1)
wheat_df.head()

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..

wheat_df.corr()

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..

plt.imshow(wheat_df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()
tick_marks = [i for i in range(len(wheat_df.columns))]
plt.xticks(tick_marks, wheat_df.columns, rotation='vertical')
plt.yticks(tick_marks, wheat_df.columns)
plt.show()


