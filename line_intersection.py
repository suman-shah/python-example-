import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString

x1 = []
x2 = []
y1 = []
y2 = []

N = 1000
x1 = np.arange(0, 1, (1-0)/N).reshape((N,1))
x2 = np.arange(0, 1, (1-0)/N).reshape((N,1))
y1 = np.arange(0, 1, (1-0)/N).reshape((N,1))
y2 = np.arange(1, 0, (0-1)/N).reshape((N,1))

line_1 = LineString(np.column_stack((x1, y1)))
line_2 = LineString(np.column_stack((x2, y2)))
intersect = line_1.intersection(line_2)
p = np.array(intersect)
print(p)

plt.plot(x1,y1)
plt.plot(x2,y2)
