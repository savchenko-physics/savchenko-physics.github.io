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
alpha = np.radians(15)

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
    line1.set_data([0, -L * np.sin(alpha)*2], [0, -L*2 * np.cos(alpha)])
    time_text.set_text('')
    return line, line1, time_text

val1 = 0
def update(frame):
	global val1
	frame1 = (frame+val1)%400
	line.set_data([0, x[frame1]], [0, y[frame1]])	

	if (x[(frame1+2)%400]<-L * np.sin(alpha) and y[(frame1+2)%400]>-L * np.cos(alpha)):
		# line.set_color('red')
		print(frame)
		val1=val1+29
	# else:
		# line.set_color('blue')
	time_text.set_text(time_template % (frame * dt))
	return line, line1, time_text

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=dt*1000)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)
plt.show()
