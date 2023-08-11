Tutorial: Inverter Beta Designer
================================

This section walks through a simple tutorial, highlighting the various BAG3 helper shell scripts.

All the following scripts can be executed stand-alone. Run each script with ``-h`` to see the
various execution options. 

#. Running a schematic generator of a simple inverter:

    .. code-block:: bash

        $ ./gen_cell.sh data/bag3_digital/specs_blk/inv/gen_sch.yaml

This scipt passes these

    .. code-block:: yaml
        


#. Transient simulation of an inverter with clock input:

    .. code-block:: bash

        $ ./sim_cell.sh data/bag3_digital/specs_blk/inv/sim_tran.yaml

#. Measure the rise and fall times of an inverter output from a transient simulation:

    .. code-block:: bash

        $ ./meas_cell.sh data/bag3_digital/specs_blk/inv/meas.yaml

#. Size the pmos and nmos of an inverter to match the rise and fall times:

    .. code-block:: bash

        $ ./dsn_cell.sh data/bag3_digital/specs_blk/inv/dsn.yaml


 