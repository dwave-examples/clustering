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
import math

import dwavebinarycsp
import dwave.inspector
from dwave.system import EmbeddingComposite, DWaveSampler


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # coordinate labels for groups red, green, and blue
        label = "{0},{1}_".format(x, y)
        self.r = label + "r"
        self.g = label + "g"
        self.b = label + "b"


def is_positive_sum(*args):
    return sum(args) > 0


def get_distance(coordinate_0, coordinate_1):
    diff_x = coordinate_0.x - coordinate_1.x
    diff_y = coordinate_0.y - coordinate_1.y

    return math.sqrt(diff_x**2 + diff_y**2)


def get_max_distance(coordinates):
    max_distance = 0
    for i, coord0 in enumerate(coordinates[:-1]):
        for coord1 in coordinates[i+1:]:
            distance = get_distance(coord0, coord1)
            max_distance = max(max_distance, distance)

    return max_distance


def main():
    # Set up problem
    scattered_points = [(0, 0), (1, 1), (2, 4), (3, 2)]
    coordinates = [Coordinate(x, y) for x, y in scattered_points]
    max_distance = get_max_distance(coordinates)

    # Build constraints
    csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)

    # Apply constraint: coordinate can only be in one colour group
    choose_one_group = {(0, 0, 1), (0, 1, 0), (1, 0, 0)}    # TODO: remove hardcode
    for coord in coordinates:
        csp.add_constraint(choose_one_group, (coord.r, coord.g, coord.b))

    # Apply constraint: all colours must be used at least once
    # csp.add_constraint(is_positive_sum, [coord.r for coord in coordinates])
    # csp.add_constraint(is_positive_sum, [coord.g for coord in coordinates])
    # csp.add_constraint(is_positive_sum, [coord.b for coord in coordinates])

    # Build initial BQM
    bqm = dwavebinarycsp.stitch(csp)

    # Edit BQM to bias for short edges
    for i, coord0 in enumerate(coordinates[:-1]):
        for coord1 in coordinates[i+1:]:
            d = get_distance(coord0, coord1) / max_distance
            bqm.add_interaction(coord0.r, coord1.r, -math.cos(d * math.pi))
            bqm.add_interaction(coord0.g, coord1.g, -math.cos(d * math.pi))
            bqm.add_interaction(coord0.b, coord1.b, -math.cos(d * math.pi))

    for i, coord0 in enumerate(coordinates[:-1]):
        for coord1 in coordinates[i+1:]:
            d = get_distance(coord0, coord1) / max_distance
            bqm.add_interaction(coord0.r, coord1.b, -d / (1+d))
            bqm.add_interaction(coord0.r, coord1.g, -d / (1+d))
            bqm.add_interaction(coord0.b, coord1.r, -d / (1+d))
            bqm.add_interaction(coord0.b, coord1.g, -d / (1+d))
            bqm.add_interaction(coord0.g, coord1.r, -d / (1+d))
            bqm.add_interaction(coord0.g, coord1.b, -d / (1+d))

    # Submit problem to solver
    solver = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))
    sampleset = solver.sample(bqm)
    best_sample = sampleset.first.sample

    # Visualize problem
    dwave.inspector.show(bqm, sampleset)



if __name__ == "__main__":
    main()
