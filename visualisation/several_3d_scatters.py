import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

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
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the area,
# perimeter and asymmetry features. Be sure to use the
# optional display parameter c='red', and also label your
# axes
# 
# .. your code here ..

fig = plt.figure()
plt.suptitle('area x perimeter x asymmetry')
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('area')
ax.set_ylabel('perimeter')
ax.set_zlabel('asymmetry')
ax.scatter(wheat_df.area, wheat_df.perimeter,wheat_df.asymmetry,c = 'r', marker='o')
plt.show()

#
# TODO: Create a new 3D subplot using fig. Then use the
# subplot to graph a 3D scatter plot using the width,
# groove and length features. Be sure to use the
# optional display parameter c='green', and also label your
# axes
# 
# .. your code here ..

fig = plt.figure()
plt.suptitle('width x groove x length')
ax = fig.add_subplot(111, projection = '3d')
ax.set_xlabel('width')
ax.set_ylabel('groove')
ax.set_zlabel('length')
ax.scatter(wheat_df.width, wheat_df.groove,wheat_df.length,c = 'green', marker='o')
plt.show()
