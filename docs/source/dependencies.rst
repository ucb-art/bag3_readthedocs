Initial Server Setup
====================

.. note::

   BWRC users: Everything described in this page is already configured in ``/tools/C/bag``, so you can jump ahead to the next page.

BAG3++ requires multiple Python and C++ dependences. These instructions will install the dependencies on your machine.  

#. Install (on CentOS or Red Hat versions >=7):

    * httpd24-curl
    * httpd24-libcurl
    * devtoolset-8 (compilers)
    * rh-git218

#. Copy the ``environment.yml`` from this `link`_ in the documentation repo, and update the
   ``prefix`` in the last line to your desired location. Then build a miniconda3
   environment from the yml file:

    .. code-block:: bash
       
        $ conda env create -f environment.yml

    .. _link: https://github.com/ucb-art/bag3_readthedocs/blob/main/docs/source/environment.yml 

   Successful building should give all python dependencies, as well as the C++ fmt and spdlog packages. 

#. Create a directory to install programs in (referred to as ``/path/to/programs``). For all following program install steps, use the ``gcc`` that comes with ``devtoolset-8``.

#. Download and extract cmake 3.17.0, then build:

    .. code-block:: bash

        $ wget https://github.com/Kitware/CMake/releases/download/v3.17.0/cmake-3.17.0.tar.gz
        $ tar -xvf cmake-3.17.0.tar.gz
        $ cd cmake-3.17.0
        $ ./bootstrap --prefix=/path/to/conda/env/envname --parallel=4
        $ make -j4
        $ make install

#.  Install magic\_enum as follows:

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

#.  Install libfyaml:

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
        $ tar -xvf hd5f-1.10.6.tar.gz
        $ cd hd5f-1.10.6
        $ ./configure --prefix=/path/to/conda/env/envname
        $ make -j24
        $ make install

#.  Boost - download source, unzip. In directory, run:

    .. code-block:: bash

        $ wget https://boostorg.jfrog.io/artifactory/main/release/1.72.0/source/boost_1_72_0.tar.gz
        $ tar -xvf boost_1_72_0.tar.gz
        $ cd boost_1_72_0
        $ ./bootstrap.sh --prefix=/path/to/conda/env/envname

#.  In the resulting ``project-config.jam`` file, change the ``using python`` line to:

    .. code-block:: bash

        using python : 3.7 : /path/to/conda/env/envname : /path/to/conda/env/envname/include/python3.7m ;

    If it exists, delete the line:

    .. code-block:: bash

        path-constant ICU_PATH : /usr ;

#.  Run:

    .. code-block:: bash

        $ ./b2 --build-dir=_build cxxflags=-fPIC -j8 -target=shared,static --with-filesystem --with-serialization --with-program_options install | tee install.log

    Remember to check ``install.log`` to see if there's any error messages (like python build error, etc.). 


.. note::
    Some users report that ``source .bashrc`` after installing all programs will result in the following error:

    .. code-block:: bash
    
        $ rpm: /path/anaconda3/envs/bag_py3d7_c/lib/liblzma.so.5: version `XZ_5.1.2alpha` not found (required by /lib64/librpmio.so.3)
    
    To fix this, remove ``/path/to/conda/envs/bag_py3d7_c/lib/liblzma.so.5.2.5``. ``rpm`` will then function correctly, assuming the ``rpm`` used is in ``/usr/bin/rpm``.
