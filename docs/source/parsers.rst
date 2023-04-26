Simulation Results Parser
=========================

Currently, the only circuit simulation program supported by BAG3++ is Spectre. For parsing the
Spectre simulation results, BAG3++ currently has two available options, with some limitations:

#. **psfbin**: This result format is enabled by default in BAG3++.

    .. warning::

        * It uses `libpsf <https://pypi.org/project/libpsf/>`_ which is released under the GNU
          Lesser General Public License v3.0.

        * It sometimes errors if > 10 signals are saved in transient simulations.

#. **nutbin**: This is the alternative format that is parsed natively in BAG3++. This can
   enabled by setting ``format: nutbin`` instead of ``format: psfbin`` in ``bag_config.yaml``.

    .. warning::

        * This format does not support multi threading and multi processing.

        * In PAC simulations, this format does not support ``maxsideband > 0``.

        * Cadence's Viva waveform viewer cannot read this format.
