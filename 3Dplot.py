import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
trios_op1 = 10  # Intra oral scanner 1 operated by Operator 1
trios_op2 = 9   # Intra oral scanner 1 operated by Operator 2
aor_op1 = 8     # Intra oral scanner 2 operated by Operator 1
aor_op2 = 9     # Intra oral scanner 2 operated by Operator 2

# Labels for the x, y, and z axes
operators = ['Operator 1', 'Operator 2']
scanners = ['Intra Oral Scanner 1', 'Intra Oral Scanner 2']

# Values for the z-axis (amount of correct predictions out of 10)
values = np.array([[trios_op1, aor_op1],
                  [trios_op2, aor_op2]])

# Define colors for the bars of different scanners
colors = np.array(['skyblue', 'lightgreen'])

# Define the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set the positions of the bars on the x and y axes
xpos, ypos = np.meshgrid(range(values.shape[0]), range(values.shape[1]))

# Flatten the values array
zpos = np.zeros_like(values).flatten()
dx = dy = 0.4  # Increase the spacing between bars
dz = values.flatten()

# Create the array of colors for the bars
bar_colors = np.repeat(colors, len(dz) // len(colors))

# Create the 3D bar chart with different colors for scanners
ax.bar3d(xpos.flatten(), ypos.flatten(), zpos, dx, dy, dz, color=bar_colors)

# Set the labels for the x, y, and z axes
# ax.set_xlabel('Operator')
# ax.set_ylabel('Scanner')
ax.set_zlabel('Correct Predictions')

# Set the ticks and tick labels for the x and y axes
ax.set_xticks(np.arange(values.shape[0]) + dx / 2)
ax.set_yticks(np.arange(values.shape[1]) + dy / 2)
ax.set_xticklabels(operators)
ax.set_yticklabels(scanners)

# Rotate the x and y axis tick labels for better visibility
ax.set_xticklabels(operators, rotation=45)
ax.set_yticklabels(scanners, rotation=-30)

# Show the plot
plt.show()
