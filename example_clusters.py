# This is not the main demo script. It is simple a handy script generate more
# interesting data to try with the main demo script, `clustering.py`.
#
# This script is about setting up this more interesting data and then passing
# the data to `clustering.cluster_points(..)`, a key function `clustering.py`.

import numpy as np

from utilities import visualize_scatterplot
from clustering import cluster_points

# Set up three different clusters of data points
covariance = [[3, 0], [0, 3]]
n_points = 3
x0, y0 = np.random.multivariate_normal([0, 0], covariance, n_points).T
x1, y1 = np.random.multivariate_normal([10, 5], covariance, n_points).T
x2, y2 = np.random.multivariate_normal([5, 15], covariance, n_points).T

# Combine data points together into a list of tuples
# Note: data points now look like [(x0, y0), (x1, y1), ..]
xs = np.hstack([x0, x1, x2])
ys = np.hstack([y0, y1, y2])
xys = np.vstack([xs, ys]).T
scattered_points = list(map(tuple, xys))

# Save the original, un-clustered plot
visualize_scatterplot(scattered_points, "orig_plot.png")

# Run clustering script with scattered_points
cluster_points(scattered_points, "clustered_plot.png")