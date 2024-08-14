import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
# todo Sample data
data = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]

# Calculate the histogram
hist, bin_edges = np.histogram(data, bins=5)

print("Histogram counts:", hist)
print("Bin edges:", bin_edges)

# todo Sample data
x = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]
y = [1, 1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 10]

# Calculate the 2D histogram
hist, x_edges, y_edges = np.histogram2d(x, y, bins=5)

print("2D Histogram counts:\n", hist)
print("X bin edges:", x_edges)
print("Y bin edges:", y_edges)

# Plotting the 2D histogram
plt.imshow(hist, interpolation='nearest', origin='lower', extent=[x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]])
plt.colorbar(label='Counts')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Histogram')
plt.show()
