
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris



# Load the dataset into dataframe
titanic_df = pd.read_csv('Titanic.csv')


# get the statistic summary of the dataframe
print(titanic_df.describe(include='all'))
print(titanic_df.info())

# get the shape of dataframe
# print(titanic_df.shape)

# drop the less useful columns such as 'Ticket' and 'Cabin'
df = titanic_df.drop(columns=['Ticket','Cabin'],axis=0) 

# print(df.shape)

# check if any duplicate entry is present
# print(df[df.duplicated()].shape)

# there is no duplicates entry

# check the count of non-null entries in each column
# print(df.count())

# check the count of naN values in each columns
# print(df.isna().sum())

# we got 177 naN count in Age columns

# remove rows containing missing of null values
df = df.dropna()
# print(df.count())
# now no null values

# print(df)

# Survival rate by gender
print(df.groupby('Sex')['Survived'].mean())
# we find that women had high survival rate on titanic

# Histogram to show distribution of ages by gender
# sns.histplot(df, x='Age',hue='Sex')

# Histogram to show distribution of ages by survival status
# sns.histplot(df, x='Age',hue='Survived')

# Histogram to show the survival chances across gender
# sns.histplot(df, x='Sex',hue='Survived')

# Histogram to show distribution of fare by gender
# sns.histplot(df, x='Fare',hue='Sex')

# Histogram to show fare distribution across class
# sns.histplot(df, x='Fare',hue='Pclass')

# 
# sns.barplot(df, x='Sex',y='Age',hue='Survived')
# sns.scatterplot(df,x = 'Fare',y = 'Age',hue='Survived',style='Sex',palette='viridis')


# plt.show()