import matplotlib.pyplot as plt
import numpy as np

def hexagon(x_center, y_center, size):
    """Generate the x and y coordinates of a hexagon."""
    angle_offset = np.pi / 6  # To orient the hexagon flat
    angles = np.linspace(0, 2 * np.pi, 7) + angle_offset
    x_hexagon = x_center + size * np.cos(angles)
    y_hexagon = y_center + size * np.sin(angles)
    # print(angles)
    return x_hexagon, y_hexagon

def plot_hexagon_grid(rows, cols, size):
    """Plot a grid of hexagons."""
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # angles = np.linspace(0, 2 * np.pi, 7)

    # Constants to calculate hexagon positions
    dx = size * np.sqrt(3)/2
    dy = size * 3

    for row in range(rows):
        for col in range(cols):
            # Offset odd rows by half the hexagon width
            x_offset = col * dx
            y_offset = row * dy
            if col % 2 == 1:
                y_offset += dy / 2
            x_hexagon, y_hexagon = hexagon(x_offset, y_offset, size)
            ax.fill(x_hexagon, y_hexagon, edgecolor='black', facecolor='none')

    plt.show()

# Customize grid size and hexagon size
plot_hexagon_grid(rows=10, cols=30, size=1)
