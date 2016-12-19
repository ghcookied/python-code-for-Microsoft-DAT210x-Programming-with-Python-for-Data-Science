import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pca_kidney_disease_helper as helper
import os
import math

os.getcwd()
os.chdir('C:/Users/David/Documents/Technology/Python/edX/DAT210x-master/Module4')

# Look pretty...
matplotlib.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
scaleFeatures = True

# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
# .. your code here ..

df  = pd.read_csv('Datasets/kidney_disease.csv')

df.head()

df = df.dropna(axis = 0)

df_new = df.drop(labels = ['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'],axis = 1)

df_new.dtypes

# Create some color coded labels; the actual label feature
# will be removed prior to executing PCA, since it's unsupervised.
# You're only labeling by color so you can see the effects of PCA
labels = ['red' if i=='ckd' else 'green' for i in df.classification]

# TODO: Use an indexer to select only the following columns:
#       ['bgr','wc','rc']
#
# .. your code here ..


df_new.wc = pd.to_numeric(df_new.wc,errors='coerce')
df_new.rc = pd.to_numeric(df_new.rc,errors='coerce')
df_new.pcv = pd.to_numeric(df_new.pcv,errors='coerce')

df_new.describe()

# TODO: Print out and check your dataframe's dtypes. You'll probably
# want to call 'exit()' after you print it out so you can stop the
# program's execution.
#
# You can either take a look at the dataset webpage in the attribute info
# section: https://archive.ics.uci.edu/ml/datasets/Chronic_Kidney_Disease
# or you can actually peek through the dataframe by printing a few rows.
# What kind of data type should these three columns be? If Pandas didn't
# properly detect and convert them to that data type for you, then use
# an appropriate command to coerce these features into the right type.
#
# .. your code here ..



# TODO: PCA Operates based on variance. The variable with the greatest
# variance will dominate. Go ahead and peek into your data using a
# command that will check the variance of every feature in your dataset.
# Print out the results. Also print out the results of running .describe
# on your dataset.
#
# Hint: If you don't see all three variables: 'bgr','wc' and 'rc', then
# you probably didn't complete the previous step properly.
#
# .. your code here ..



# TODO: This method assumes your dataframe is called df. If it isn't,
# make the appropriate changes. Don't alter the code in scaleFeatures()
# just yet though!
#
# .. your code adjustment here ..
if scaleFeatures: df_new = helper.scaleFeatures(df_new)

# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
# .. your code here ..

from sklearn import decomposition
from sklearn import datasets

pca = decomposition.PCA(n_components=len(df_new.columns))
pca.fit(df_new)
T = pca.transform(df_new)
 
# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:

X = pd.DataFrame(T)

Y = X.iloc[:,[0,1]]


Y.columns = ['component1', 'component2']

Y.columns.values

pca.components_[0]

ax = helper.drawVectors(Y, pca.components_, Y.columns.values, plt, scaleFeatures)



Y.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()


