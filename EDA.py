
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
# print(titanic_df.describe(include='all'))
# print(titanic_df.info())

# get the shape of dataframe
# print(titanic_df.shape)

# drop the less useful columns such as 'Ticket' and 'Cabin'
df = titanic_df.drop(columns=['Ticket','Cabin'],axis=1) 


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


df.loc[:, 'Embarked'] = df['Embarked'].map({'C': 'Cherbourg', 'Q': 'Queenstown', 'S': 'Southampton'})
df.loc[:, 'Embarked'] = pd.Categorical(df['Embarked'], categories=['Cherbourg', 'Queenstown', 'Southampton'])
df.loc[:, 'Pclass'] = df['Pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})
df.loc[:, 'Pclass'] = pd.Categorical(df['Pclass'], categories=['First', 'Second', 'Third'], ordered=True)
df.loc[:, 'Sex'] = df['Sex'].astype('category')

print(df.info())


#               sibling or spouse   parents or children
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

print(df.to_string)

# Survival rate by gender
print(df.groupby('Sex')['Survived'].mean())
# we find that women had high survival rate on titanic

# to show distribution of ages by gender
sns.histplot(df, x='Age',hue='Sex')

# to show distribution of ages by survival status
sns.histplot(df, x='Age',hue='Survived')

#to show the survival chances across gender
sns.countplot(df, x='Sex',hue='Survived')

# to show the survival chances across classes
sns.countplot(df, x='Pclass',hue='Survived',stat='percent')

# to show distribution of fare by gender
sns.histplot(df, x='Fare',hue='Sex')

# to show fare distribution across class
sns.histplot(df, x='Fare',hue='Pclass')
print(df.groupby('Pclass')['Fare'].mean())

# fare distribution by embarkation port
sns.histplot(df, x='Fare',hue='Embarked')
print(df.groupby('Embarked')['Fare'].mean())

# to show the survival chances with embarked
sns.countplot(df, x='Embarked',hue='Survived',stat='probability')
print(df.groupby('Embarked')['Survived'].mean())

# to show the frequency on the basis of gender 
sns.countplot(df, x='Embarked',hue='Sex')

# to show the whether is passenger was alone or with family
sns.countplot(df,x='FamilySize')
# higher number of passengers were traveling alone

# sns.countplot(df,x='FamilySize',hue='Survived')
family_survival = df.groupby('FamilySize')['Survived'].mean().reset_index()
sns.lineplot(data=family_survival, x='FamilySize', y='Survived')
plt.title("Survival Rate by Family Size")


print(df.groupby('FamilySize')['Survived'].mean())

sns.jointplot(df, y='Fare',x='Age',hue='Survived')

sns.scatterplot(df,y = 'Fare',x = 'Age',style='Survived',size='Sex',hue='FamilySize',palette='viridis')

sns.swarmplot(df,x = 'Sex',y = 'Age')

sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age Distribution by Survival Status")
plt.xticks([0, 1], ['Did Not Survive', 'Survived'])

pivot = df.pivot_table(index='Pclass', columns='Sex', values='Survived', aggfunc='mean')
print(pivot)
sns.heatmap(pivot, annot=True, cmap='YlGnBu')
plt.title("Survival Rate by Class and Gender")


fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(df['Age'], df['Fare'], df['Survived'], c=df['Survived'], cmap='coolwarm', alpha=0.7)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
ax.set_zlabel('Survived')
plt.title("3D Plot: Age vs Fare vs Survival")
plt.colorbar(sc, label='Survival')


# plt.grid()

sns.pairplot(df[['Age','Fare','Survived']], hue ='Survived', diag_kind='kde')

plt.show()