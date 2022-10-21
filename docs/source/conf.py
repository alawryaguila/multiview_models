# Configuration file for the Sphinx documentation builder.
import datetime
# -- Project information

project = 'MultiAE'
author = 'Ana Lawry Aguila & Alejandra Jayme'
copyright = f"{datetime.datetime.now().year}, {author}"
release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

# -- sphinx.ext.autosummary
autosummary_generate = True

# -- sphinx.ext.autodoc
autodoc_member_order = "bysource"
autoclass_content = "both"

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
