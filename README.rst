.. -*- restructuredtext -*-

=========================
README for Pickle Builder
=========================

Sphinx_ extension to pickle documents.

In itself, the extension is fairly straightforward -- it takes the parsed reST
file from Sphinx_ and pickles it to a file.

Installing
==========

Using pip
---------

::

    pip install picklebuilder

Usage
=====

- Set the builder as a extension in ``conf.py``::

    extensions = ['picklebuilder.picklebuilder']

- Run sphinx-build with target ``rpickle``::

    sphinx-build -b rpickle -c . build/pickle

Further Reading
===============

.. _Sphinx: http://sphinx-doc.org/

Feedback
========

The pickle builder is in a preliminary state. It's not (yet) widely used, so
any feedback is particularly welcome.
