# Configuration file for the Sphinx documentation builder.

import os
import sys
# sys.path.insert(0, os.path.abspath('../../src'))
# # sys.path.insert(-1, os.path.abspath('../../src/bag/'))
# sys.path.insert(-1, os.path.abspath('../../pybag'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../../xbase/src'))

# from glob import glob
# from distutils.dir_util import copy_tree
# import subprocess

# currentfolder = os.path.abspath('./') # aka docs/
# rootfolder = os.path.abspath('../')
# tmpfolder = "{}/tmp".format(currentfolder)
# globdir = '{}/repo-*/repo'.format(rootfolder)
# subprocess.check_call(["mkdir", "-p", tmpfolder]) # make sure temporary folder exists 

# all_sub_dir_paths = glob(globdir) # returns list of sub directory paths
# for subdir in all_sub_dir_paths:
#     print("subdir: {} to tmp folder: {}".format(subdir, tmpfolder))
#     copy_tree(subdir, tmpfolder) # copy all folders to docs/tmp/repo/*

# autoapi_dirs = [tmpfolder]
# sys.path.insert(0, tmpfolder)
# autoapi_python_use_implicit_namespaces = True


# -- Project information

project = 'BAG3++'
copyright = '2023, Ayan Biswas'
author = 'Ayan Biswas'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'autoapi.extension'
]


autoapi_dirs = ['../../bag/src/bag',
                '../../bag3_testbenches/src/bag3_testbenches',
                '../../bag3_analog/src/bag3_analog',
                '../../bag3_digital/src/bag3_digital',
                '../../bag3_magnetics/src/bag3_magnetics',
                '../../xbase/src/xbase',   ]
autoapi_add_toctree_entry = False
autoapi_python_use_implicit_namespaces = True
autoapi_file_patterns = ['*.py']
autoapi_options = [ 'members', 'undoc-members', 'private-members', 'show-inheritance', 'show-module-summary', 'special-members']
suppress_warnings = ["autoapi"]

# autosummary_generate = False
# autodoc_mock_imports = ["pybag", "ruamel", "srr", "libpsf", "lark", "bag3_digital", 
#                         "srr_python", "openmdao", "ocean", "dc", 'bag.tech', 'bag.interface.simulator'
                        # ]

exclude_patterns = ['_build', '_templates', "../../xbase/src/xbase/__init__.py"]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']
templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

