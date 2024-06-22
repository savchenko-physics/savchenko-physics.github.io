import matplotlib.pyplot as plt

# Create the figure and axis
fig, ax = plt.subplots()

# Draw the fixed bars A and B
ax.plot([-1, 1], [1, 1], color='black', linewidth=2)  # Bar A
ax.plot([-1, 1], [-1, -1], color='black', linewidth=2)  # Bar B

# Draw the circle representing the wheel
circle = plt.Circle((0, 0), 1, color='black', fill=False)
ax.add_patch(circle)

# Draw the points A, B, and O
ax.plot([0, 0], [1, -1], 'ko')  # Points A and B
ax.plot(0, 0, 'ko')  # Point O

# Draw the velocity vectors V1 and V2
ax.arrow(1, 1, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')  # V1
ax.arrow(1, -1, 0.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')  # V2

# Annotate the points and vectors
ax.text(0, 1.1, 'A', fontsize=12, ha='center')
ax.text(0, -1.2, 'B', fontsize=12, ha='center')
ax.text(0, 0.1, 'O', fontsize=12, ha='center')
ax.text(1.6, 1.1, 'V1', fontsize=12, ha='center')
ax.text(1.6, -1.2, 'V2', fontsize=12, ha='center')

# Set the limits and aspect ratio
ax.set_xlim(-1.5, 2)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')

# Remove the axes for clarity
ax.axis('off')

# Show the plot
plt.show()
