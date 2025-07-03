
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris



# Load the dataset into dataframe
titanic_df = pd.read_csv('Titanic.csv',index_col='PassengerId')


# get the statistic summary of the dataframe
print(titanic_df.describe(include='all'))
print(titanic_df.info())

# get the shape of dataframe
print(titanic_df.shape)

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

# to show distribution of ages by gender
# sns.histplot(df, x='Age',hue='Sex')

# to show distribution of ages by survival status
# sns.histplot(df, x='Age',hue='Survived')

#to show the survival chances across gender
# sns.countplot(df, x='Sex',hue='Survived')

# to show the survival chances across classes
# sns.countplot(df, x='Pclass',hue='Survived',stat='percent')

# to show distribution of fare by gender
# sns.histplot(df, x='Fare',hue='Sex')

# to show fare distribution across class
# sns.histplot(df, x='Fare',hue='Pclass')
# print(df.groupby('Pclass')['Fare'].mean())

# fare distribution by embarkation port
sns.histplot(df, x='Fare',hue='Embarked')
print(df.groupby('Embarked')['Fare'].mean())

# to show the survival chances with embarked
# sns.countplot(df, x='Embarked',hue='Survived',stat='probability')
print(df.groupby('Embarked')['Survived'].mean())

# to show the frequency on the basis of gender 
# sns.countplot(df, x='Embarked',hue='Sex')

# sns.jointplot(df, y='Fare',x='Age',hue='Survived')

# sns.scatterplot(df,y = 'Fare',x = 'Age',style='Survived',hue='Sex')


plt.show()