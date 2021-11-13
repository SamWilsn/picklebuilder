# -*- coding: utf-8 -*-
"""
    picklebuilder.builders.pickle64
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pickle Sphinx builder.

    :copyright: Copyright 2021 by Sam Wilson and contributors.
    :license: BSD, see LICENSE.txt for details.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

from ..writers.pickle64 import Pickle64Writer
from .pickle import PickleBuilder


class Pickle64Builder(PickleBuilder):
    name = 'pickle64'
    format = 'pickle64'
    file_suffix = '.pickle64'
    link_suffix = None  # defaults to file_suffix

    def prepare_writing(self, docnames):
        super().prepare_writing(docnames)
        self.writer = Pickle64Writer(self)
