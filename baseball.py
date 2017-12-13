from __future__ import division
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

path = 'baseballdatabank-2017.1/core/'
master = pd.read_csv(path+'Master.csv')
batting = pd.read_csv(path+'Batting.csv')
pitching = pd.read_csv(path+'Pitching.csv')
fielding = pd.read_csv(path+'Fielding.csv')

births = pd.Series(data=master.loc[:,'birthYear'].values, index=master.loc[:,'playerID'].values)

runs = batting.loc[:, ['playerID','yearID','R','G']]

def per(row):
    return row['R']/row['G']

def age(row):
    year = row['yearID']
    birth = births[row['playerID']]
    return year - birth


runs['R/G'] = runs.apply(per,axis=1)
runs['age'] = runs.apply(age,axis=1)

runs = runs.dropna()
print runs

f = plt.figure(1)
runs.groupby('age')['R/G'].sum().plot()
#seems for sure like the best players are a bit under 30
#but wait...this result seems too perfect... I used the sum
#It could just be that the majority of players are at that age

#So let's count the number of players at each age over the years
h = plt.figure(2)
runs.groupby('age')['R/G'].count().plot()
#Indeed, the majority of players are just under 30. 

#So let's look at the mean of the R/G ratio at each age
g = plt.figure(3)
runs.groupby('age')['R/G'].mean().plot()
#Wow! much different

i = plt.figure(4)
max = runs.groupby('playerID')['age'].max()
max.hist(bins=int(max.max()-max.min()+1),align='left')
print max.max(), max.min()

j = plt.figure(5)
min = runs.groupby('playerID')['age'].min()
min.hist(bins=int(min.max()-min.min()+1),align='left')
print min.max(), min.min()



f.show()
g.show()
h.show()
i.show()
j.show()
raw_input()
