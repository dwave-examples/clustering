# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This is not the main demo script. It is simple a handy script generate more
# interesting data to try with the main demo script, `clustering.py`.
#
# This script is about setting up this more interesting data and then passing
# the data to `clustering.cluster_points(..)`, a key function `clustering.py`.

import argparse
import numpy as np

from utilities import visualize_scatterplot
from clustering import cluster_points

parser = argparse.ArgumentParser()
parser.add_argument('--no-problem-inspector', action='store_false', dest='problem_inspector', help='do not show problem inspector')
args = parser.parse_args()


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
orig_filename = "nine_points.png"
visualize_scatterplot(scattered_points, orig_filename)

# Run clustering script with scattered_points
clustered_filename = "nine_points_clustered.png"
cluster_points(scattered_points, clustered_filename, args.problem_inspector)

print("Your plots are saved to '{}' and '{}'.".format(orig_filename,
                                                 clustered_filename))
