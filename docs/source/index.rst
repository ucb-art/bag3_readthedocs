Welcome to BAG3++ documentation!
===================================

**BAG3++** (Berkeley Analog Generator, version 3++) is an updated release of BAG 3.0 from BWRC
(Berkeley Wireless Research Center). It removes the dependence on all closed-source CAD programs
except the complete Cadence Virtuoso Design Suite.

.. note::

    The BAG3++ files developed at BWRC are released under the BSD-3-Clause license. Some older
    files from the original BAG 3.0 are released under the Apache-2.0 license. For parsing
    simulation results, BAG3++ uses `libpsf <https://pypi.org/project/libpsf/>`_ which is released
    under the GNU Lesser General Public License v3.0. BAG3++ has an alternative native simulation
    parser that has some disadvantages. See :doc:`parsers` for more details.

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
   structure
   parsers
   inverter_beta_designer
   mos_characterization
   passives_characterization
   new_pdk_setup
