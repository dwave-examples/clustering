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
  blue. Therefore, if a data point is in the red cluster, it is not allowed
  to join the green nor blue clusters.
* This cluster membership rule is represented by the variable
  `choose_one_group`.

  ::
      choose_one_group = {(0, 0, 1), (0, 1, 0), (1, 0, 0)}

  


Close together data points should be in the same cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Far apart data points should be in different clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


References
----------

A. Person, "Title of Amazing Information",
`short link name <https://example.com/>`_


License
-------

Released under the Apache License 2.0. See `LICENSE <LICENSE>`_ file.
