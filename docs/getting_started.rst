Getting Started
===============

When documenting Python code, it is common to put a lot of documentation in the source files, in documentation strings. Sphinx 
supports the inclusion of docstrings from your modules with an extension (an extension is a Python module that provides additional 
features for Sphinx projects) called autodoc.

In order to use autodoc, you need to activate it in conf.py by putting the string 'sphinx.ext.autodoc' into the list assigned to
the extensions config value. Then, you have a few additional directives at your disposal.

For example, to document the function io.open(), reading its signature and docstring from the source file.
