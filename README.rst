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

Notable parts of the code implementation.

This is the place to:

* Highlight a part of the code implementation
* Talk about unusual or potentially difficult parts of the code
* Explain a code decision

Note: there is no need to repeat everything that is already well-documented in
the code.


References
----------

A. Person, "Title of Amazing Information",
`short link name <https://example.com/>`_


License
-------

Released under the Apache License 2.0. See `LICENSE <LICENSE>`_ file.
