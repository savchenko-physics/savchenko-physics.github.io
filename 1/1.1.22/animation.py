import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
R = 10  # Radius of the cylinder
h = 2   # Minimum distance from the axis
dt = 0.1  # Time step

# Ball's initial position and velocity
x, y = R - h, 0
vx, vy = 1, 2  # Velocity components

# Ball's radius
ball_radius = 0.5

def update_position(x, y, vx, vy):
    x_new = x + vx * dt
    y_new = y + vy * dt
    
    # Check for collision with the cylinder wall
    if np.sqrt(x_new**2 + y_new**2) >= (R - ball_radius):
        # Reflect the velocity vector
        normal = np.array([x_new, y_new])
        normal /= np.linalg.norm(normal)
        v = np.array([vx, vy])
        v = v - 2 * np.dot(v, normal) * normal
        vx, vy = v[0], v[1]
        
        # Update position with reflected velocity
        x_new = x + vx * dt
        y_new = y + vy * dt
        
    return x_new, y_new, vx, vy

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_aspect('equal')

# Draw the cylinder
cylinder = plt.Circle((0, 0), R, edgecolor='blue', facecolor='none')
ax.add_patch(cylinder)

# Draw the ball
ball, = ax.plot([], [], 'ro', ms=10)

def init():
    ball.set_data([], [])
    return ball,

def animate(i):
    global x, y, vx, vy
    x, y, vx, vy = update_position(x, y, vx, vy)
    ball.set_data([x], [y])  # Provide x and y as sequences
    return ball,

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=30, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

plt.show()
