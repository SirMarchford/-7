import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def func(x):
    return np.cos(x), np.sin(x)

x = np.linspace(-5*np.pi, 5*np.pi, 100)

y, z = func(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Трехмерный график')
plt.show()
