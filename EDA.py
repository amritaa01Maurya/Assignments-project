
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

# load the data into pandas dataframe 
df = pd.read_csv('Car Sell Dataset.csv')

# display top 5 and bootom 5 values
print(df.head())
print(df.tail())

# know the datatypes of df
print(df.dtypes)

# delete the columns which are of no use in eda
df = df.drop(['Model Name','Model Variant'],axis=1)

# print(df.info())
# print(df.describe(include='all'))

# print(df.isna())

print(df)