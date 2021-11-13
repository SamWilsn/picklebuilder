# -*- coding: utf-8 -*-
"""
    picklebuilder.picklebuilder
    ===========================

    Sphinx extension to output pickle files.

    .. moduleauthor:: Sam Wilson <sam.wilson@mesh.xyz>

    :copyright: Copyright 2021 by Sam Wilson and contributors.
    :license: BSD, see LICENSE.txt for details.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

__version__ = '0.1.0'
__author__ = 'Sam Wilson <sam.wilson@mesh.xyz> and contributors'


def setup(app):
    # imports defined inside setup function, so that the __version__ can be
    # loaded, even if Sphinx is not yet installed.
    from .builders.pickle import PickleBuilder  # loads PickleWriter as well.
    from .builders.pickle64 import Pickle64Builder
    from .parsers.pickle import Parser

    app.require_sphinx('4.0')
    app.add_builder(PickleBuilder)
    app.add_builder(Pickle64Builder)
    app.add_source_suffix('.pickle64', 'pickle64')
    app.add_source_parser(Parser)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
