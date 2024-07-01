import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
ax.set_xlim(-L-0.1, L+0.1)
ax.set_ylim(-L-0.1, L+0.1)
ax.set_aspect('equal')

line, = ax.plot([], [], 'o-', lw=2)
line1, = ax.plot([], [], 'o-', lw=2)
time_template = 'Time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    line.set_data([], [])
    line1.set_data([], [])
    time_text.set_text('')
    return line, line1, time_text

val1 = 1
def update(frame):
	print(frame)
	if x[frame*val1]/2 <=0:
		line1.set_data([0, 0], [0, -L/2])
		line1.set_color('#e84c17')
		line.set_data([0, x[frame*val1]/2], [-L/2, -L/2+y[frame*val1]/2])
	else:
		line1.set_data([0, x[frame*val1]/2], [0, y[frame*val1]/2])
		line1.set_color('#1e72b6')
		line.set_color('#1e72b6')
		line.set_data([x[frame*val1]/2, x[frame*val1]], [y[frame*val1]/2, y[frame*val1]])
	time_text.set_text(time_template % (frame * dt))
	return line, line1, time_text

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

plt.show()
