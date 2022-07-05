# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>

import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

os.environ["DJANGO_SETTINGS_MODULE"] = "rtd_settings"

import aiida
from aiida.manage.configuration import settings

# We set that we are in documentation mode - even for local compilation
settings.IN_DOC_MODE = True

# on_rtd is whether we are on readthedocs.org, this line of code grabbed
# from docs.readthedocs.org
# NOTE: it is needed to have these lines before load_dbenv()
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = "sphinx_rtd_theme"
    # Loading the dbenv. The backend should be fixed before compiling the
    # documentation.
    aiida.load_profile()
else:
    # Back-end settings for readthedocs online documentation.
    # from aiida.manage.configuration import settings
    settings.IN_RT_DOC_MODE = True
    settings.BACKEND = "django"
    settings.AIIDADB_PROFILE = "default"

import aiida_tools

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "sympy": ("http://docs.sympy.org/latest", None),
    "h5py": ("http://docs.h5py.org/en/latest", None),
}

nitpick_ignore = [("py:obj", "")]

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
# ~ master_doc = 'index'
master_doc = "index"

# General information about the project.
project = "aiida-tools"
copyright = f"2017-{time.localtime().tm_year}, ETH Zurich"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ".".join(aiida_tools.__version__.split(".")[:2])
# The full version, including alpha/beta/rc tags.
release = aiida_tools.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["doc.rst"]
# ~ exclude_patterns = ['index.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

html_search_language = "en"

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = "aiida_tools_doc"
