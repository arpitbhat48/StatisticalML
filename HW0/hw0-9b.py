import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


x = np.arange(0,10,0.5)
y = np.arange(0,10,0.5)
X, Y = np.meshgrid(x,y)
Z = X + Y

ax = plt.axes(projection="3d")
ax.plot_surface(X,Y,Z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
# plt.xlabel("x")
# plt.ylabel("y")

plt.title("3D Hyper Plane")
plt.show()