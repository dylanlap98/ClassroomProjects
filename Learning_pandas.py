import pandas as pd
import numpy as np

#s = pd.Series(np.random.randint(1, 100, 10))
#print(s)

df1 = pd.DataFrame(np.reshape(range(0,12), [3,4]))
# this shows counts across x and y.
print(df1)

df1[0][0] = 20

print(df1)

# save dictionary to a pandas DataFrame
data = {'Year' : [2020, 2021], 'Life_Span':[78,77], 'Density': [67.2, 35.9]}
df2 = pd.DataFrame(data)
print(df2)
# df2.iloc[0][0]  # need to use iloc to search in this DataFrame since its from a dict (view of wrap dictionary)

df2 = df2.copy(deep=True)  # make a deep copy
df2.iloc[0][0]

print('\n', 'New lines', '\n')


print(df1)
# sum across columns
print(df1.sum())
# sum across rows
print(df1.sum(axis=1))
# sum of all in df
print(df1.sum().sum())
# sum specific column in this case
print(df1.iloc[:,3].sum())

print(df1)

print('\n', 'New lines', '\n')
# new Section

import string
abt = list(string.ascii_lowercase)
df1 = pd.DataFrame(np.reshape(range(20),[4,5]), columns=abt[0:5])
df3=df1.reindex(columns=abt[0:6])
df2 = df1.reindex([3,2,'a',0])

print(df2)

# drop default is drop row.  dropna() if any row has na it drops whole row...
df2_1 = df2.dropna()  # not in place
print(df2_1)

# new df2
df2 = pd.DataFrame(np.reshape(range(0,20),[4,5]), columns=abt[0:5])
print(df2)
# this makes our 0 a NaN, we can use this to drop a row on the following code below this statement
print(df2[df2>0])
print(df2[df2>0].dropna())


print(df2.drop([0]))  # to just drop first row
print(df2.drop([0,2]))  # to drop first and third row

df3 = df2[df2 != 0]  # used to target a specific value..
print(df3)

print('\n', 'New lines', '\n')
# new Section

s8 = pd.Series(np.random.randint(0,100,8),index=[list('aabbccdd'), [0,1,0,1,0,1,0,1]])
print(s8)
