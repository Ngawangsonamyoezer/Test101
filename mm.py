import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the semiconductor lattice size
lattice_size = 10

# Create a lattice with random distribution of electrons (1) and holes (0)
np.random.seed(0)
lattice = np.random.choice([0, 1], size=(lattice_size, lattice_size), p=[0.2, 0.8])

# Function to update the lattice for the animation
def update_lattice(*args):
    global lattice
    # Randomly select an electron
    electron_positions = np.argwhere(lattice == 1)
    if electron_positions.size > 0:
        electron_choice = electron_positions[np.random.choice(electron_positions.shape[0])]
        x, y = electron_choice

        # Randomly select a direction to move the electron
        direction = np.random.choice(['up', 'down', 'left', 'right'])
        if direction == 'up' and x > 0:
            lattice[x, y], lattice[x-1, y] = lattice[x-1, y], lattice[x, y]
        elif direction == 'down' and x < lattice_size - 1:
            lattice[x, y], lattice[x+1, y] = lattice[x+1, y], lattice[x, y]
        elif direction == 'left' and y > 0:
            lattice[x, y], lattice[x, y-1] = lattice[x, y-1], lattice[x, y]
        elif direction == 'right' and y < lattice_size - 1:
            lattice[x, y], lattice[x, y+1] = lattice[x, y+1], lattice[x, y]

    # Update the plot
    mat.set_data(lattice)
    return mat,

# Set up the plot
fig, ax = plt.subplots()
mat = ax.matshow(lattice, cmap='viridis')
plt.title('Semiconductor Lattice Electron-Hole Movement Simulation')

# Animate the lattice
ani = animation.FuncAnimation(fig, update_lattice, interval=500, save_count=50)

# Show the animation
plt.show()
