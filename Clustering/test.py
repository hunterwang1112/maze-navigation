import numpy as np
import pandas as pd
import os
import glob
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans


fileName = '/Users/wangyan/Desktop/Research/Maze_Research/Parsed_Data/ANAV.csv'
df = pd.read_csv(fileName)
print(df)
feature = list(df['posX'].values[0:30000:10])
feature2 = list(df['posZ'].values[0:30000:10])
feature.extend(feature2)