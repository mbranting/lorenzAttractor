import numpy as np
import matplotlib.pyplot as plt
# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import time

# Start the timer
start = time.time()


def lorenz(x, y, z, s=15, r=28, b=2.667):
    '''
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    '''
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


t0 = 0
ts = np.linspace(0, 100, 10001)
dt = 0.01
num_steps = 10000

# Need one more for the initial values
xs = np.empty(num_steps + 1)
ys = np.empty(num_steps + 1)
zs = np.empty(num_steps + 1)

# Set initial values
xs[0], ys[0], zs[0] = (0., 1., 1.05)

# Step through "time", calculating the partial derivatives at the current point
# and using them to estimate the next point
for i in range(num_steps):
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)

figure, axis = plt.subplots(2, 2)
# For x(t)
axis[0, 0].plot(ts, xs)
axis[0, 0].set_title("x(t): r = 28")

# For y(t)
axis[0, 1].plot(ts, ys)
axis[0, 1].set_title("y(t): r = 28")

# For z(t)
axis[1, 0].plot(ts, zs)
axis[1, 0].set_title("z(t): r = 28")

# For Green's function of equation 2
axis[1, 1].plot()
axis[1, 1].set_title("")

# # Plot

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs, lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()

# Computes the amount of time the program took to execute
end = time.time()
print("Computing Time: ")
print(end - start, "in seconds")

