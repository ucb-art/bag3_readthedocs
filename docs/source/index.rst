Welcome to BAG3++ documentation!
===================================

**BAG3++** is BWRC's release of BAG 3.0. It removes the dependence on all closed-source CAD tools
except the complete Cadence Virtuoso Design Suite.

BAG3++ is predominantly a Python project. Users write layout and schematic generators, and
measurement managers and design scripts in Python. However most of the back-end infrastructure is
implemented in C++ for faster execution. Hence the compilation of the C++ back-end requires the
installation of various C++ dependencies. Additionally, there are a few standard Python
dependencies that need to be installed to execute the generators.

Please go through the :doc:`dependencies` section for detailed instructions about configuring the
server to be able to run BAG3++. Then use the publicly available workspaces to run some example
BAG scripts.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   dependencies
   workspaces
