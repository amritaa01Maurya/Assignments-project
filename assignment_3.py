import numpy as np
import pandas as pd

# task 1
# data = [25, 30, 35, 40, 45] 

# pds = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])

# print(pds[:3])
# print(pds.mean())
# print(pds.median())
# print(pds.std())


# task 2
data = {
    "Name":['Alice','Bob','Carol','David','Eve'],
    "Age":[20,22,19,21,20],
    "Gender":['Female','Male','Female','Male','Female'],
    "Marks":[85,78,92,74,88]
}

df = pd.DataFrame(data,columns=['Name','Age','Gender','Marks'])

# # print(df.head(2))
# # print(df.columns,df.dtypes)
# print(df.describe(include='all'))
# df['Passed'] = df['Marks'] >= 80
# print(df)


# task 3

# print(df[['Name','Marks']])
# print(df[df['Marks']>80])

# max = df['Marks'].max()
# print(df[df['Marks'] == max])

# task 4

df.loc[1, 'Marks'] = None 
df.loc[4, 'Age'] = None 

# print(df)
# print(df.isna())

df.fillna({'Marks':df['Marks'].mean()},inplace=True)
# print(df)

df.dropna(subset=['Age'],inplace=True)
# print(df)

# task 5
# ndf = df.groupby('Gender')

# print(ndf[['Age','Marks']].mean())
# print(ndf['Gender'].value_counts())

# task 6
# df.to_csv("students_data.csv")

ndf = pd.read_csv("students_data.csv")

print(ndf)
print(ndf.head)