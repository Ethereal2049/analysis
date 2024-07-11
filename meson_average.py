import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.genfromtxt('meson.txt', names=['start_of_bin', 'end_of_bin', 'height', 'error'])

# Calculate the top (height + error)
error_over_height=data['error']/data['height']



ax = plt.plots()

for i in range(len(data)):
    while data['height'][i] != 0 :

        bin_center = (data['start_of_bin'][i] + data['end_of_bin'][i]) / 2
        bin_width = data['end_of_bin'][i] - data['start_of_bin'][i]

        # Plot the white bottom part of the bar (height)
        ax.bar(bin_center, error_over_height[i], width=bin_width, color='white', edgecolor='black')
        break
    else:
        pass




ax.set_xlabel('')
ax.set_ylabel('')

# Adjust y-axis limits for better visualization
# Adjust y-axis limits for better visualization
plt.ylim(-0.0005, 0.001)
plt.xlim(0, 0.21)


plt.title('')

# Show the plot
plt.show()
