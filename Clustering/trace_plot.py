import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import pandas as pd


file_name = '/Users/wangyan/Desktop/Research/Maze_Research/Maze-Navigation/Parsed_Data/ACGN.csv'
df = pd.read_csv(file_name)
# read in the data on X and Z position plus the rotation
x = list(df['posX'].values[::10])
y = list(df['posZ'].values[::10])
print(x)
print(y)

fig = plt.figure()
ax = plt.axes(projection="3d")

time = list(range(3000, 0, -1))
t_size = len(x)
# colorGrad customized
colorGrad = []
for i in range(0, t_size):
    colorGrad.append([i/t_size, 0, 1 - i/t_size])

z_points = time
x_points = x
y_points = y
ax.scatter3D(x_points, y_points, z_points, c=colorGrad, cmap='hsv')

plt.show()