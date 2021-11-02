# -- Project information -----------------------------------------------------

project = 'YARD Stick One'
copyright = '2021, Great Scott Gadgets'
author = 'Great Scott Gadgets'

version = ''
release = ''


# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = []
source_suffix = '.rst'
master_doc = 'index'
language = None
pygments_style = None


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
