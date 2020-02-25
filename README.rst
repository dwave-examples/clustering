==========
Clustering
==========

TODO: talk about how in machine learning how we can get information out of
unlabeled data by clustering. Example: house square footage and house price data -->
clusters of data can indicate different neighbourhoods. A boolean vector of tv shows
that consumer watches --> close together vectors may indicate the size of a particular
demographic.

TODO: if you have a couple labelled pieces of data in your cluster, perhaps you can label
the whole cluster with a single labelled member. i.e. we can infer information by clustering data.

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
* Since a qubit can only end up in one of two states (i.e. it can only
  answer yes or no questions)

TODO: PUT INSPECTOR IMAGE WITH HERE

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

* Here, we want to encourage far apart data points to be in different clusters.
  Again, since the D-Wave Quantum Computer solves for low-energy solutions, we
  need to make far apart data points correspond to a low energy.
* We do this by choosing a strong negative weight for far apart points. Hence,
  the choice of the ``tanh`` function.

  ::

      d = math.sqrt(get_distance(coord0, coord1) / max_distance)
      weight = -math.tanh(d) * 0.1

* Note that a scalar of ``0.1`` was applied in order to prevent this weight from
  washing out the other weights in the BQM. The ``0.1`` is arbitrary and was
  found by tinkering with the code.


License
-------

Released under the Apache License 2.0. See `LICENSE <LICENSE>`_ file.
