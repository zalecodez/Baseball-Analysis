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

#group by age and extract R/G column
age_rg = runs.groupby('age')['R/G']

plots = []
#R/G sum against age
plots.append(plt.figure(len(plots)+1))
age_rg.sum().plot()

#count against age
plots.append(plt.figure(len(plots)+1))
age_rg.count().plot()

#R/G mean against age
plots.append(plt.figure(len(plots)+1))
age_rg.mean().plot()

#Age players stop playing
plots.append(plt.figure(len(plots)+1))
max = runs.groupby('playerID')['age'].max()
max.hist(bins=int(max.max()-max.min()+1),align='left')
print max.max(), max.min()

#Age players start playing
plots.append(plt.figure(len(plots)+1))
min = runs.groupby('playerID')['age'].min()
min.hist(bins=int(min.max()-min.min()+1),align='left')
print min.max(), min.min()

#players over 50
print runs[runs['age']>50]

#players with over 50 games
runs_g_over_50 = runs[runs['G']>50]

plots.append(plt.figure(len(plots)+1))
runs_g_over_50.groupby('age')['R/G'].count().plot()

plots.append(plt.figure(len(plots)+1))
runs_g_over_50.groupby('age')['R/G'].mean().plot()

def plot_player(name,games=0):   
    plots.append(plt.figure(len(plots)+1))
    table = runs[runs['G']>games]
    p = table[table['playerID']==name]
    r = p.loc[:,['R/G']].values
    a = p.loc[:,['age']].values
    plt.plot(a,r)

plot_player('orourji01',1)
plot_player('minosmi01',1)

for i in range(3):
    name = np.random.choice(runs_g_over_50.loc[:,'playerID'].values)
    plot_player(name,50)

for p in plots:
    p.show()
raw_input()
