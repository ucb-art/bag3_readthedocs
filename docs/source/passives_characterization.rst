Passives characterization
=========================

The passives characterization models the specified device-under-test (DUT) as a pi network and
estimates its capacitance / inductance / resistance.

#. Resistor characterization:

    .. code-block:: bash

        $ ./meas_cell.sh data/bag3_testbenches/specs_res_char/res_char.yaml

   Run with ``-x`` to characterize the extracted resistor instead of schematic only.

#. Capacitor characterization:

    .. code-block:: bash

        $ ./meas_cell.sh data/bag3_testbenches/specs_cap_char/momcap_char.yaml -x

   The BAG MOMCap doesn't have an equivalent schematic model, and can be characterized in
   extracted mode only.
   The script has also been used to characterize MIMCaps in processes that have MIMCaps.


.. note::

   In ``cds_ff_mpt``, resistors (poly and metal) extract incorrectly, so the extracted netlist
   runs into simulation errors. So the above two examples won't work in that PDK in extracted mode.
