import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D Axes
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
import math

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

data = np.genfromtxt('Moment/W1.dat', names=['q', 'u', 'w', 'wu', 'wd'])

x = data['q']
y = data['u']
z = data['w']

mask = (x == 0.175) & (z > 0)
filtered_y = y[mask]
filtered_z = z[mask]


def fit_function(y, a, b, c, f):
    return a * np.log(y)/y + b/y + c * y + f

# Use curve_fit to find the best-fit parameters
params, covariance = curve_fit(fit_function, filtered_y, filtered_z)

# Extract the optimized parameters
a_fit, b_fit, c_fit, f_fit= params


print("Optimized parameters:")
print(f"a_fit: {round(a_fit,4)}")
print(f"b_fit: {round(b_fit,4)}")
print(f"c_fit: {round(c_fit,4)}")
print(f"f_fit: {round(f_fit,4)}")

# Print the covariance matrix
print("\nCovariance matrix:")
print(covariance)





# Generate y_values for the best-fit line
y_values = np.arange(0.015, 0.655, 0.01)
z_values_fit = fit_function(y_values, a_fit, b_fit, c_fit, f_fit)


# Plot the data points
plt.scatter(filtered_y, filtered_z, color='blue', label='Data points')

# Plot the best-fit line
plt.plot(y_values, z_values_fit, color='red', label='Best Fit Line')




# Set labels and title
plt.xlabel('u')
plt.ylabel('w')
plt.title('0.035')

# Set the limits of the axes
plt.xlim(0, 0.7)
plt.ylim(0, 20)

# Add legend
plt.legend()

# Show the plot
plt.show()
'''
# Plotting the scatter plot in 3D
#ax.scatter(x,y,z)

# Labeling the axes
#ax.set_xlabel('q')
#ax.set_ylabel('u')
#ax.set_zlabel('w')
plt.show()
'''
