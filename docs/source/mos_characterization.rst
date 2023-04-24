Transistor characterization
===========================

The transistor characterization consists of 2 main steps: characterization and query.

Creating the characterization database
--------------------------------------

This step characterizes a fixed sized transistor in 3 steps:

#. **DC sweep**: Run a DC sweep on a diode connected transistor to find ``vgs_min`` and ``vgs_max``
                 where the drain current is within some specified range ``ibias_min`` and
                 ``ibias_max``. This is essentially finding the ``vgs`` range when the transistor is "on".

#. **s parameter sweep**: Run a multidimensional SP sweep across ``vgs``, ``vds``, ``vbs`` to
                          compute the small signal parameters like ``gm``, various parasitic caps
                          (``cgg``, ``cgs``, ``cgd``, etc).

#. **noise sweep**: This estimates the thermal noise factor ``gamma`` from the total integrated
                    noise. This is an approximation, and is valid only if the min frequency of the
                    noise integration is above the frequency corner for flicker noise.

.. code-block:: bash

    $ ./meas_cell.sh data/bag3_testbenches/specs_mos_char/nch_*.yaml
    $ ./meas_cell.sh data/bag3_testbenches/specs_mos_char/pch_*.yaml

Run with ``-x`` to characterize the extracted transistor instead of schematic only.

At the end of the characterization, a database is created in the specified ``root_dir``.

Querying the characterization database
--------------------------------------

This step queries the small signal parameters per finger of the pre-characterized transistor at the
desired bias point

.. code-block:: bash

    $ ./run_bag.sh bag3_testbenches/run_scripts/test_mos_char.py data/bag3_testbenches/specs_mos_char/test_char.yaml
