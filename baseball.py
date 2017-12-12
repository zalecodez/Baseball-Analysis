import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

path = 'baseballdatabank-2017.1/core/'
teams = pd.read_csv(path+'Teams.csv')

wins = teams.groupby('yearID').get_group(2016)
print wins

plt.hist(wins['W'])
plt.show()
