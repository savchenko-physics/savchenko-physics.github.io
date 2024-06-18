import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
g = 9.81  # acceleration due to gravity
L = 10  # length of spokes
num_spokes = 6  # number of spokes
time_duration = 5  # duration of the animation in seconds
fps = 30  # frames per second

# Spoke angles (equally distributed around a circle)
angles = np.linspace(-np.pi/3, np.pi/3+ np.pi/9, num_spokes, endpoint=False)

# Time array
t = np.linspace(0, time_duration, time_duration * fps)

# Initialize figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-L, L)
ax.set_ylim(-L, L)
ax.set_aspect('equal')

# Plot the spokes
for angle in angles:
    x_spoke = [0, L * np.sin(angle)]
    y_spoke = [0, -L * np.cos(angle)]
    ax.plot(x_spoke, y_spoke, 'k-')

# Beads positions initialization
beads, = ax.plot([], [], 'ro', color="blue")

# Function to update bead positions at each frame
def update(frame):
    x_positions = []
    y_positions = []
    for angle in angles:
        # Calculate the distance the bead has traveled along the spoke
        distance = 0.5 * g * (frame / fps)**2
        x = distance * np.sin(angle)
        y = -distance * np.cos(angle)
        x_positions.append(x )
        y_positions.append(y)
    
    beads.set_data(x_positions, y_positions)
    return beads,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=40, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=7, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)


# Show the animation
plt.show()
