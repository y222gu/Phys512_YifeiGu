import numpy as np
import matplotlib.pyplot as plt
import random

# load data for a three-dimensional plot
data = np.loadtxt('rand_points.txt')
x = data[:,0]
y = data[:,1]
z = data[:,2]
fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
ax.scatter(x, y, z, marker='o',s=0.1)

for angle in range(0, 360):
    ax.view_init(angle,45)
    plt.draw()
    plt.pause(.001)
plt.savefig('rand_points_from_broken_lib_after_rotation.png')
plt.show()
# random points from python generator
X = []
Y = []
Z = []

for i in range(30253):    
    x = random.randrange(0,10**8)
    y = random.randrange(0,10**8)
    z = random.randrange(0,10**8)
    X.append(x)
    Y.append(y)
    Z.append(z)
fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, marker='o',s=0.1)
plt.savefig('python_rand_points_generator.png')
plt.show()