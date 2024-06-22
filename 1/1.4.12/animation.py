import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
  # velocity of the body (m/s)
u = 1  # velocity of the walls (m/s)
L = 10  # initial distance between walls (m)
dt = 0.01  # time step (s)
v_y = 1
v1 = 10
v = v1
n=0
# Initial positions
body_x = 0
wall_left_x = -L/2
wall_right_x = L/2
body_y = 4


# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-15, 15)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')

# Plot elements
body, = ax.plot([], [], 'ro', markersize=10)
wall_left, = ax.plot([], [], 'k', lw=5)
wall_right, = ax.plot([], [], 'k', lw=5)

def init():
    body.set_data([], [])
    wall_left.set_data([], [])
    wall_right.set_data([], [])
    return body, wall_left, wall_right

def update(frame):
    global body_x, wall_left_x, wall_right_x, v, body_y, v_y,v1,n
    
    # Update positions
    body_x += v * dt *5
    body_y += v_y * dt 

    v_y = -(n-1) * L*0.981/(v1-u)
    print(frame)
    wall_left_x += u * dt
    wall_right_x += u * dt
    
    if (body_x <= wall_left_x+1):
        v = v1
        n = n+ 1

    if body_x >= wall_right_x-1:
        v = -(v1 - 2*u) 
        n = n+ 1

    # Update plot elements
    body.set_data([body_x], [body_y])
    wall_left.set_data([wall_left_x, wall_left_x], [-5, 5])
    wall_right.set_data([wall_right_x, wall_right_x], [-5, 5])
    
    return body, wall_left, wall_right

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 1.8, dt), init_func=init, blit=True)
Writer = animation.writers['ffmpeg']
writer = Writer(fps=70, metadata=dict(artist='Me'), bitrate=1800)
ani.save('animation.gif', writer=writer)

plt.show()
