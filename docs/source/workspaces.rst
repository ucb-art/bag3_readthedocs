BAG3++ Workspaces
=================

Workspaces are available for the following open source PDKs. Please git clone and follow the
instructions in the README.

.. note::

    We strongly recommend using the PyCharm editor for easily navigating across the function
    definitions and quickly viewing doc strings in the various python files. For convenience, the
    ``.idea`` folders are included in all the repositories so that PyCharm gets auto-configured
    correctly in each workspace.

Available workspaces
--------------------
#. `BAG3++ workspace for cds_ff_mpt <https://github.com/ucb-art/bag3_ams_cds_ff_mpt>`_: This is
   an academic FinFET PDK ``cds_ff_mpt`` from Cadence.

#. `BAG3++ workspace for SkyWater130 <https://github.com/ucb-art/bag3_skywater130_workspace>`_:
   This is configured for the ``s8`` version of the planar SkyWater 130nm PDK.

Updating path configurations
----------------------------

.. note::

   BWRC users: This section is not necessary since all the paths are already configured.

After git cloning the workspaces and recursively updating the submodules, make the following
changes.

#. In ``.bashrc_bag``, set:

    .. code-block:: bash

        export BAG_TOOLS_ROOT=/path/to/conda/env/envname

#. In ``.bashrc`` set

    .. code-block:: bash

    	export CMAKE_HOME=/path/to/programs/cmake-3.17.0

#. In ``.bashrc``, update the paths to the PDK installation directory and other programs.

#. For server traffic management and space utilization reasons, we recommend putting simulation
   results, output logs from DRC, LVS, etc, in a "scratch" space to avoid increasing the size of
   the workspace area. Configure BAG to use the "scratch" space by editing this line in ``.bashrc_bag``:

    .. code-block:: bash

        export BAG_TEMP_DIR=/path/to/scratch/space

#. Configure Virtuoso to put simulation results in the same "scratch" space by editing this line
   in ``.cdsenv``:

    .. code-block:: bash

        asimenv.startup projectDir string "/path/to/scratch/space"

#. Update the ``PDK`` symlink inside ``<tech_repo>/workspace_setup`` to point to the local PDK
   installation directory.
