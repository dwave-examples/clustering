==========
Clustering
==========

Clusters data points.

.. image:: readme_imgs/clustered_plot.png


Usage
-----

.. code-block:: bash

  python clustering.py

This provide a visualization of the problem on the D-Wave Inspector and save
the solution in a plot, ``plot.png``.

Code Overview
-------------

The D-Wave quantum computer solves a particular type of mathematical model
called the Binary Quadratic Model. The goal here is to build a BQM such that
it represents of our clustering problem. Namely, we want a BQM such that a
low-energy solution found by the D-Wave quantum computer would correspond to a
solution to our clustering problem.

Key properties of the clustering problem that we need to capture in our BQM:

* Each data point can only be a part of one cluster
* Data points that are close together should be a part of the same cluster
* Data points that are far apart should be in different clusters


Code Specifics
--------------

Let's go through how we implement each of the key properties of our clustering
problem.

Each data point can only join one cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The code is only considering three different cluster labels: red, green, and
  blue.
* The rule that a data point may only join one cluster is represented by the
  variable ``choose_one_group`` (shown below). Each three-item-tuple below can
  be interpreted as ``(<join-red>, <join-green>, <join-blue>)``, where the
  ``1``s and ``0``s indicate true and false, respectively. Hence, the
  ``choose_one_group`` is a set of all valid states. (e.g. ``(1, 1, 0)`` is not
  valid because a data point is not allowed to be in both red and green clusters
  at once).

  ::

      choose_one_group = {(0, 0, 1), (0, 1, 0), (1, 0, 0)}

Close together data points should be in the same cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* In order to encourage nearby points to be in the same cluster, we apply
  weights to the BQM such that choosing nearby data points to be in the same
  cluster would lead to a lower energy solution (something that the D-Wave
  Quantum Computer solves for).
* These weights are dependent on distance. In order to keep the weights within
  a reasonable range, the distances are all scaled with respect to the
  ``max_distance``, the largest distance between any two points in the dataset.
* Below is the function used to determine the weight to encourage close together
  points to be in the same cluster

  ::

      d = get_distance(coord0, coord1) / max_distance  # rescale distance
      weight = -math.cos(d*math.pi)

* We can apply many different types of functions for generating the weight.
  In this case, we chose a cosine function. The main idea is that we simply
  need short distances (nearby points) to generate a strong negative value
  towards putting the points in the same cluster (i.e. encourage the D-Wave
  solver to pick this configuration), while points with large distances are
  only mildy affected.

Far apart data points should be in different clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


References
----------

A. Person, "Title of Amazing Information",
`short link name <https://example.com/>`_


License
-------

Released under the Apache License 2.0. See `LICENSE <LICENSE>`_ file.
