import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Set the limits of the x-axis (walls)
ax.set_ylim(-1, 1)  # Set the limits of the y-axis (so the disk stays in view)

# Initial position of the disk
x = 5
velocity = 0.2

# Create a disk (circle)
disk, = ax.plot([], [], 'bo', ms=40, color='#964B00')
rect1 = plt.Rectangle((1.0, -0.3), 0.3, 0.5, fc='#000000')
rect2 = plt.Rectangle((8.7, -0.3), 0.3, 0.5, fc='#000000')
ax.add_patch(rect1)
ax.add_patch(rect2)

def init():
    """Initialize the background of the animation."""
    disk.set_data([], [])
    return disk,
w = 5
def animate(i):
    """Perform animation step."""
    global x, velocity,w

    # Update the position with constant velocity and modulo operation
    print (f"{i} {np.sin(np.radians(i*w))}")
    
    x = 4.99 + 3.12 *np.sin(np.radians(i*w))
    # x += velocity

    # if x >= 8 or x <= 2:
    #     velocity *= -1

    x = x % 10  # Wrap around using modulo operation

    # Update the disk position
    disk.set_data([x], [0])  # Wrap x and y in a list
    return disk,

# Create animation object
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=30, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

# Display the animation
plt.show()
