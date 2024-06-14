import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Parameters
alpha = np.radians(30)  # Angle in radians (for 2*alpha = 60 degrees)
v = 1  # velocity
rod_length = 20  # Length of each rod
interval = 50  # Time interval between frames in milliseconds

# Calculate initial positions of the rods
x1_init, y1_init = np.array([-rod_length/2, rod_length/2]), np.array([-rod_length/2, rod_length/2]) * np.tan(alpha)
x2_init, y2_init = np.array([-rod_length/2, rod_length/2]), -np.array([-rod_length/2, rod_length/2]) * np.tan(alpha)

# Setup the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-rod_length, rod_length)
ax.set_ylim(-rod_length, rod_length)
line1, = ax.plot([], [], 'k-', lw=2)
line2, = ax.plot([], [], 'k-', lw=2)
intersection_point, = ax.plot([], [], 'ro')  # Marker for intersection point

def init():
    """Initialize the background of the animation."""
    line1.set_data([], [])
    line2.set_data([], [])
    intersection_point.set_data([], [])
    return line1, line2, intersection_point

def animate(i):
    """Perform animation step."""
    shift = v * i / 10.0  # Movement shift
    
    # Calculate current positions of rods
    x1_current = x1_init - shift * np.sin(alpha)
    y1_current = y1_init + shift * np.cos(alpha)
    x2_current = x2_init - shift * np.sin(alpha)
    y2_current = y2_init - shift * np.cos(alpha)
    
    # Update rods' positions
    line1.set_data(x1_current, y1_current)
    line2.set_data(x2_current, y2_current)
    
    # Calculate intersection point of the two rods
    x_intersect = -shift/np.sin(alpha)
    y_intersect = 0
    
    # Update intersection point marker
    intersection_point.set_data([x_intersect], [y_intersect])  # Ensure x_intersect and y_intersect are in lists
    
    return line1, line2, intersection_point


# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=70, interval=interval, blit=True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

# Save or display the animation
plt.show()
