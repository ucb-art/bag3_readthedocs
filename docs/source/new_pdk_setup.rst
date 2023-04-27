Developer's Guide: Setting up BAG 3++ in a new PDK
==================================================

Setting up BAG 3++ is a new PDK is a very complicated multi-step process. It involves the initial
basic setup step that can be done in about a week, followed by an exponential tail of months to
years long development optimizing various layout primitives and enabling special features, e.g.
guard rings, mimcaps, esds, blackboxing PDK provided pcells, etc. The following is a rough
guideline summarizing the basic steps, but specific PDKs often require special handling at
various steps, which are mostly determined by experience and trial-and-error. The ``cds_ff_mpt``
process is used as an example to explain some of the steps.

Since BAG 3++ is deeply tied in to the Cadence Virtuoso Design Suite, many of the setup steps
involve observing some PDK collateral (e.g. pcell CDF parameters for netlisting, etc) in Virtuoso
and replicating that in BAG 3++.

#. **Getting started**

    Copy over the ``cds_ff_mpt`` tech repository in BAG 3++ to use as a template, and update the
    ``PDK`` symlink inside ``workspace_setup`` to point to the local PDK installation directory.

#. **Resolution of the PDK and Dimension scaling**

    Run the following 3 SKILL commands in the Virtuoso CIW window, replacing ``cds_ff_mpt`` with
    the PDK library name:

    .. code-block:: bash

        techid=techGetTechFile(ddGetObj("cds_ff_mpt")))
        techGetMfgGridResolution(techid)
        techGetDBUPerUU(techid "maskLayout")

    The second line outputs ``0.001``, so the grid resolution is ``1 nm``.
    The third line outputs ``2000``, so the design rule resolution is ``1 um / 2000 = 0.5 nm``.

    In BAG 3++, all layout dimensions are specified in resolution units to enforce integer
    calculations, and avoid floating point rounding errors. Based on the above grid resolution and
    design rule resolution, all dimensions in BAG's yaml files will be ``1 nm / 0.5 nm = 2``
    times the physical dimensions. Hence the BAG 3++ dimension scaling for ``cds_ff_mpt`` is 2.
    Set up ``layout_unit`` and ``resolution`` in
    ``cds_ff_mpt/src/templates_cds_ff_mpt/data/tech_params.yaml`` accordingly.

#. **Techfile layer numbers**

    This mapping of layers to numbers is found in the "techfile" which is different from the
    "layermap". Go through the following steps to tell BAG 3++ about this mapping:

    #. Run the following in the workspace terminal, replacing ``cds_ff_mpt`` with the PDK library
       name

        .. code-block:: bash

            BAG_framework/run_scripts/write_tech_info.sh cds_ff_mpt test.yaml

    #. Copy the contents of the ``test.yaml`` into ``cds_ff_mpt/src/templates_cds_ff_mpt/data/tech_params.yaml``,
       replacing ``cds_ff_mpt`` with the PDK library name

        .. warning::

            Some entries like ``drawing``, ``label``, ``boundary``, ``pin``, ``drawing1``,
            ``drawing2``, ``drawing3``, etc may be missing from ``purpose``. Use the default
            settings for these from the ``tech_params.yaml`` of ``cds_ff_mpt``.

#. Compile the C++ back-end by running the following in the workspace terminal:

    .. code-block:: bash

        source .bashrc
        cd BAG_framework/pybag
        ./run_test.sh
        cd ..

#. **Schematic pCell setup**

    This step creates the ``BAG_prim`` cells that should be used to make schematic templates.
    The ``BAG_prim`` cells provide process agnostic wrappers so that the schematic templates
    don't reveal process information. By setting up the ``BAG_prim`` library for every specific
    PDK, the schematic templates get automatically configured for the PDK in Virtuoso.

    #. Populate the various ``mos``, ``res``, etc. lists in ``<tech_repo>/pcell_setup/gen_skill.py``

    #. Modify the ``prim_pcell_jinja2.il`` based on the CDF parameters of the PDK components. You
       can view the CDF parameters by going to ``Tools --> CDF --> Edit`` in the Virtuoso CIW and
       navigating to the relevant cell in the PDK library.

    #. Execute the ``gen_skill.py`` to create ``prim_pcell.il`` from the template
       ``prim_pcell_jinja2.il``.

    #. In the Virtuoso CIW, run ``load("/path/to/prim_pcell.il")`` to create the schematic pCells
       in the ``BAG_prim`` library.

    #. Using ``Tools --> CDF --> Edit`` in the Virtuoso CIW, setup the CDF parameters of the
       generated ``BAG_prim`` schematics.

        .. note::

            Refer to the CDF parameters for ``cds_ff_mpt`` ``BAG_prim`` cells.
            Set the ``Type`` as ``string`` for all the new parameters.
            Select ``yes`` in ``Store Default``.
            Remember to click ``Apply`` to save the edits.

    #. Create the symbols for each generated pCell using the recommended template in the
       ``BAG_prim`` library for ``cds_ff_mpt``.

    #. Import the ``BAG_prim`` cells into BAG 3++, by opening an IPython shell using
       ``./start_bag.sh`` and running the following:

        .. code-block:: python

            from bag.core import BagProject
            prj = BagProject()
            prj.import_design_library(<lib_name>)   # for importing the entire library
            prj.import_sch_cellview(<lib_name>, <cell_name>)    # for importing a specific cell

    .. warning::

        We have found that the pCell callbacks work in all FinFET and SOI processes, and some
        planar processes (e.g. SkyWater130), but not in certain other planar processes. We are not
        sure of the exact reason for the discrepancy. Perhaps it's because of older ICADV versions.
        If the pCell callbacks don't work, you can still use BAG's native netlister to serve
        all purposes, but generated schematics will have wrong parameters.

#. **Schematic netlist setup**

    BAG 3++ has native CDL, Spectre and SystemVerilog netlisters so that it can directly generate
    the netlists from the internal schematic circuit representation. To ensure that the generated
    CDL and Spectre netlists are consistent with the Virtuoso generated versions, we need to
    configure the header files that define the ``BAG_prim`` cells.

    #. Populate the various dictionaries in ``netlist_setup/gen_config.yaml``.

        * For CDL details, generate the CDL netlist using Virtuoso to view the relevant parameter
          names for every ``BAG_prim`` cell.

        * For Spectre netlist details, generate the scs netlist from ADE / Maestro to view the
          relevant parameter names for every ``BAG_prim`` cell.

    #. To create the ``BAG_prim`` CDL and spectre netlist headers, run:

        .. code-block:: bash

            $ BAG_framework/run_scripts/generate_netlist_config.sh

    This creates ``bag_prim.cdl``, ``bag_prim.scs``, ``netlist_setup.yaml`` inside
    ``<tech_repo>/netist_setup``.

    .. note::

        Since the parameter configuration differs significantly across PDKs, I invariably always
        have to add extra features in BAG 3++ framework to capture everything correctly. So this
        step is only guaranteed to work in the PDKs that we have already used, and may require some
        feature updates or modifications for a new PDK. In one rare SOI case, the pCell definitions
        required a very specific setting, so it was easier for me to directly edit the generated
        ``bag_prim.cdl`` and ``bag_prim.scs`` to enable that instead of implementing the feature
        in BAG 3++ framework.

#. **Simulation corners setup**

    Define the relevant corners in ``<tech_repo>/corners_setup.yaml`` (similar to the usual
    ``corner_setup.sdb`` that is loaded in ADE or Maestro). BAG 3++ knows how to use the
    specified pvt information in its Spectre netlister.

#. **Layout primitives setup**

    This is the most difficult step, and there are no generic instructions since this is totally
    dependent on the design rules of the PDK. The only recommendation is to pick an existing
    template (e.g. ``cds_ff_mpt`` for FinFETs, and ``SkyWater130`` for planar) and modify the
    primitives implementation until the cells pass LVS and DRC.

    The recommended approach is to natively implement the custom layout primitives in Python so
    that everything is fully programmable, and BAG 3++ knows the location of every internal pin and
    wire. Blackboxing layout pCells is not recommended because of a few reasons:

    * Layout pCells cannot be parameterized through BAG 3++. So multiple frozen instances of the
      layout pCells have to be created for different parameters, and then instantiated as black
      boxes.

    * Since BAG 3++ doesn't natively know the pin locations and internal wires of the black box,
      the developer has to specify all those details. This makes the overall setup so bulky and
      inconvenient that it's easier to natively implement the custom layout primitive instead.

    Blackboxing layout pCell is used in one rare FinFET case where the PDK prohibits us from
    drawing a particular device as a custom cell.

#. **Layout verification setup**

    #. Figure out the recommended LVS and DRC tools in your PDK.

    #. Create Jinja2 templates for the runsets that can be read by the relevant scripts in
       ``BAG_framework/src/verification/``.

        * ``calibre.py`` and ``pvs.py`` are up-to-date

        * ``icv.py`` has to be updated from BAG 2 to BAG 3++.

    #. Figure out the recommended extraction tool in your PDK.

    #. Create a Jinja2 template for its runset.

        * QRC, PEX, StarRC, xRC are up-to-date in ``calibre.py``.

        * QRC, PEX are up-to-date in ``pvs.py``.

        * Other combinations of LVS and extraction tools have to be setup or updated in BAG 3++.
