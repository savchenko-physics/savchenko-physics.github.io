import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
from matplotlib.transforms import Affine2D

import matplotlib.animation as animation

g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0   # Length of the pendulum (m)
theta0 = np.radians(30)  # Initial angle (30 degrees)
omega0 = 0.0  # Initial angular velocity (rad/s)
dt = 1/40  # Time step (s)
total_time = 10  # Total time of simulation (s)

t = np.arange(0, total_time, dt)

theta = np.zeros(len(t))
omega = np.zeros(len(t))

theta[0] = theta0
omega[0] = omega0

for i in range(1, len(t)):
    omega[i] = omega[i-1] - (g / L) * np.sin(theta[i-1]) * dt
    theta[i] = theta[i-1] + omega[i] * dt

x = L * np.sin(theta)
y = -L * np.cos(theta)

fig, ax = plt.subplots()
ax.set_xlim(-L, L)
ax.set_ylim(-L-L/2, L-L/2)
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-', lw=2, markersize=3)
line1, = ax.plot([], [], '--', lw=2)
time_template = 'Time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

img = mpimg.imread('bulb.png')
imagebox = ax.imshow(img, extent=(0, 0, 0, 0), aspect='auto')

val1=1
def init():
    line.set_data([], [])
    imagebox.set_extent((0, 0, 0, 0))  # Hide the image initially
    return line, imagebox


# Update function for animation
def update(frame):
    # Update the line data
    line.set_data([0, x[frame * val1]], [0, y[frame * val1]])

    size_factor = 0.4
    imagebox.set_extent((
        x[frame * val1] - 0.5 * size_factor,
        x[frame * val1] + 0.5 * size_factor,
        y[frame * val1] - 0.5 * size_factor,
        y[frame * val1] + 0.5 * size_factor
    ))

    # print(rotation_angle, frame)
    # transform = Affine2D().rotate_deg(rotation_angle) + ax.transData
    # imagebox.set_transform(transform)

    print(frame)
    return line, imagebox


ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*100)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

plt.show()