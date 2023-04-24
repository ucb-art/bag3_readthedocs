Workspace Components
====================

In the spirit of enabling process agnostic generators, the BAG workspace has some process
agnostic generator repositories, and one process specific primitives library.

Process agnostic submodules
---------------------------

A typical BAG workspace will have the following process agnostic submodules:

* **BAG_framework**: The core framework, defining base classes for generators, interfaces with
  simulation and verification tools, etc

    * **pybag**: This defines the python bindings for the C++ implementation of the back-end.

        * **cbag**: This contains the C++ implementation of the back-end.

* **xbase**: The core layout framework (XBase), that defines the various layout base classes like
  MOSBase, ArrayBase, ResArrayBase, etc.

* **bag3_testbenches**: This defines the various generic testbenches (DCTB, ACTB, SPTB, PSSTB,
  etc) that are used in MeasurementManagers.

* **bag3_digital**: Repository with generators for "digital" custom cells

* **bag3_analog**: Repository with generators for "analog" custom cells

* **bag3_magnetics**: Repository with generators for magnetic passives like inductor, t-coil

Process specific submodules
---------------------------

A typical BAG workspace will have the following process specific submodules:

* **<tech repo>**: This usually has the same name as the PDK, and contains implementations of the
  layout primitives, ``BAG_prim`` schematics, netlisting setup, verification tools setup, etc.

* **data/xbase**: Process specific yamls for executing **xbase** generators.

* **data/bag3_testbenches**: Process specific yamls for executing **bag3_testbenches** generators.

* **data/bag3_digital**: Process specific yamls for executing **bag3_digital** generators.

* **data/bag3_analog**: Process specific yamls for executing **bag3_analog** generators.

* **data/bag3_magnetics**: Process specific yamls for executing **bag3_magnetics** generators.
