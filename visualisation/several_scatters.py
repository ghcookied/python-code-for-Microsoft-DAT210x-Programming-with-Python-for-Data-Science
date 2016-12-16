import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import os

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
# TODO: Create a 2d scatter plot that graphs the
# area and perimeter features
# 
# .. your code here ..

wheat_df.plot.scatter(x='area', y='perimeter')
plt.suptitle('Wheat seed area vs perimeter')
plt.xlabel('area')
plt.ylabel('perimeter')

#
# TODO: Create a 2d scatter plot that graphs the
# groove and asymmetry features
# 
# .. your code here ..

wheat_df.plot.scatter(x='groove', y='asymmetry')
plt.suptitle('Wheat seed groove vs asymmetry')
plt.xlabel('groove')
plt.ylabel('asymmetry')


#
# TODO: Create a 2d scatter plot that graphs the
# compactness and width features
# 
# .. your code here ..

wheat_df.plot.scatter(x='compactness', y='width',marker = 'x')
plt.suptitle('Wheat seed compactness vs width')
plt.xlabel('compactness')
plt.ylabel('width')




# BONUS TODO:
# After completing the above, go ahead and run your program
# Check out the results, and see what happens when you add
# in the optional display parameter marker with values of
# either '^', '.', or 'o'.


plt.show()


