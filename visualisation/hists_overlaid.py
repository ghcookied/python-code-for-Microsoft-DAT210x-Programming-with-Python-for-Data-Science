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
wheat_df = pd.read_csv('Datasets/wheat.data')

wheat_df.describe()

#
# TODO: Create a slice of your dataframe (call it s1)
# that only includes the 'area' and 'perimeter' features
# 
# .. your code here ..

s1 = wheat_df[['area','perimeter']]
s1.describe()

#
# TODO: Create another slice of your dataframe (call it s2)
# that only includes the 'groove' and 'asymmetry' features
# 
# .. your code here ..

s2 = wheat_df[['groove','asymmetry']]
s2.describe()

#
# TODO: Create a histogram plot using the first slice,
# and another histogram plot using the second slice.
# Be sure to set alpha=0.75
# 
# .. your code here ..

plt.figure()
s1.plot.hist(alpha=0.75)
plt.show()

plt.figure()
s2.plot.hist(alpha=0.75)
plt.show()
