Initial Server Setup
====================

.. note::

   BWRC users: Everything described in this page is already configured in ``/tools/C/bag``, so you can jump ahead to the next page.

BAG3++ requires multiple Python and C++ dependences.
These instructions will install the dependencies on your server; typically the one that also hosts your EDA toolchain (e.g. Virtuoso).

#. Install basic tools for fetching and building dependencies, via YUM/DNF:

    * curl
    * make
    * wget
    * openssl-devel (needed for compiling cmake)
    * gcc
    * gdb
    * autoconf (needed for compiling libfyaml)
    * automake
    * libtool

#. Install SCL packages via YUM/DNF (on CentOS or RHEL versions >=7):

    * httpd24-curl
    * httpd24-libcurl
    * devtoolset-8 (For newer versions of compilers)
    * rh-git218 (git with nice visual colors; newer git versions don't track symlinks)
   
   If not already done, the `Software Collections (SCL) repositories <https://wiki.centos.org/AdditionalResources/Repositories/SCL>`_ must first be enabled by installing the 
   packages ``centos-release-scl`` and ``centos-release-scl-rh``, followed by running ``sudo yum-config-manager --enable rhel-server-rhscl-7-rpms``.

#. Create a directory to install programs in (referred to as ``/path/to/programs``). Subsequent steps occur inside this directory.
   
   
#. Install miniconda, if not already available. Python 3.7 is supported/tested. Follow prompts, to create environment and set custom location if desired.

    .. code-block:: bash

        $ cd /path/to/programs
        $ wget https://repo.anaconda.com/miniconda/Miniconda3-py37_23.1.0-1-Linux-x86_64.sh
        $ bash Miniconda3-py37_23.1.0-1-Linux-x86_64.sh -b -f -p ./miniconda3

#. Download the ``environment.yml`` from this `link`_ in the documentation repo. Then build a miniconda3 environment from the .yml file, where ``/path/to/conda/env/envname`` is the full path to desired environment name.

    .. code-block:: bash
              
        $ wget https://raw.githubusercontent.com/ucb-art/bag3_readthedocs/main/docs/source/environment.yml
        $ env create -f environment.yml --force -p ./path/to/conda/env/envname

   .. _link: https://github.com/ucb-art/bag3_readthedocs/blob/main/docs/source/environment.yml 

   Successful environment creation should provide all python dependencies, as well as the C++ fmt and spdlog packages. 

#. Download and extract cmake 3.17.0, then build with updated GCC:

    .. code-block:: bash

        $ wget https://github.com/Kitware/CMake/releases/download/v3.17.0/cmake-3.17.0.tar.gz
        $ tar -xvf cmake-3.17.0.tar.gz
        $ cd cmake-3.17.0
        $ scl enable devtoolset-8 bash
        $ ./bootstrap --prefix=/path/to/conda/env/envname --parallel=4
        $ make -j4
        $ make install

#.  Install magic\_enum:

    .. code-block:: bash

        $ git clone https://github.com/Neargye/magic_enum.git
        $ cd magic_enum
        $ cmake -H. -Bbuild -DCMAKE_BUILD_TYPE=Release -DMAGIC_ENUM_OPT_BUILD_EXAMPLES=FALSE -DMAGIC_ENUM_OPT_BUILD_TESTS=FALSE -DCMAKE_INSTALL_PREFIX=/path/to/conda/env/envname
        $ cmake --build build
        $ cd build
        $ make install

#.  Install yaml-cpp:

    .. code-block:: bash

        $ git clone https://github.com/jbeder/yaml-cpp.git
        $ cd yaml-cpp
        $ cmake -B_build -H. -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_INSTALL_PREFIX=/path/to/conda/env/envname
        $ cmake --build _build --target install -- -j 4

#.  Install libfyaml: (if configure step fails, try running ``$ autoreconf -vif``)

    .. code-block:: bash

        $ git clone https://github.com/pantoniou/libfyaml.git
        $ cd libfyaml
        $ ./bootstrap.sh
        $ ./configure --prefix=/path/to/conda/env/envname
        $ make -j12
        $ make install

#.  Download HDF5 1.10 (h5py-2.10 does not work with 1.12 yet), then install:

    .. code-block:: bash

        $ wget https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.6/src/hdf5-1.10.6.tar.gz
        $ tar -xvf hdf5-1.10.6.tar.gz
        $ cd hdf5-1.10.6
        $ ./configure --prefix=/path/to/conda/env/envname
        $ make -j24
        $ make install

#.  Acquire Boost 1.72.0. First download, extract and configure:

    .. code-block:: bash

        $ wget https://boostorg.jfrog.io/artifactory/main/release/1.72.0/source/boost_1_72_0.tar.gz
        $ tar -xvf boost_1_72_0.tar.gz
        $ cd boost_1_72_0
        $ ./bootstrap.sh --prefix=/path/to/conda/env/envname

#.  Next, in the resulting ``project-config.jam`` file, change the ``using python`` line to:

    .. code-block:: bash

        using python : 3.7 : /path/to/conda/env/envname : /path/to/conda/env/envname/include/python3.7m ;

    Then delete the line:

    .. code-block:: bash

        path-constant ICU_PATH : /usr ;

#.  Finally, run:

    .. code-block:: bash

        $ ./b2 --build-dir=_build cxxflags=-fPIC -j8 -target=shared,static --with-filesystem --with-serialization --with-program_options install | tee install.log

Remember to check ``install.log`` to see if there's any error messages (like python build error, etc.). 
