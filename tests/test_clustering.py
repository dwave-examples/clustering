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
import unittest

from clustering import Coordinate, get_distance, get_max_distance


class TestHelperFunctions(unittest.TestCase):
    def test_get_distance(self):
        coord0 = Coordinate(2.5, 3)
        coord1 = Coordinate(10, -2)

        distance = get_distance(coord0, coord1)
        self.assertAlmostEqual(9.01387818866, distance)

    def test_get_max_distance(self):
        coords = [Coordinate(-1, 0), Coordinate(-.5, 3), Coordinate(-4, 4)]
        max_distance = get_max_distance(coords)

        self.assertEqual(5, max_distance)

