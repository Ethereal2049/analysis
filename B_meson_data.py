import numpy as np
import matplotlib.pyplot as plt

# Read data from the file
data = np.genfromtxt('meson.txt', names=['start_of_bin', 'end_of_bin', 'height', 'error'])

# Calculate the top (height + error)
top=data['height']+data['error']
middle = data['height'] 
bottom = data['height'] - data['error']


# Plot the histogram bars and error lines individually
fig, ax = plt.subplots()

for i in range(len(data)):
    while data['height'][i] != 0 :
    
        bin_center = (data['start_of_bin'][i] + data['end_of_bin'][i]) / 2
        bin_width = data['end_of_bin'][i] - data['start_of_bin'][i]

        # Plot the white bottom part of the bar (height)
        ax.bar(bin_center, top[i], width=bin_width, color='white', edgecolor='black')

        #height + error
        ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [top[i], top[i]], color='blue', linewidth=1)
        #height
        ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [middle[i], middle[i]], color='green', linewidth=1)
        #height - error
        ax.plot([bin_center - bin_width / 2, bin_center + bin_width / 2], [bottom[i], bottom[i]], color='red', linewidth=1)
        break
    else:
        pass

ax.set_xlabel('')
ax.set_ylabel('')

# Adjust y-axis limits for better visualization
plt.ylim(-0.0000000035, 0.000000001)
plt.xlim(0, 0.21)


plt.title('')

# Show the plot
plt.show()
