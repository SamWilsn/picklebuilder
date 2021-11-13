# -*- coding: utf-8 -*-
"""
    picklebuilder.writers.pickle
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Custom docutils writer for pickling document trees.

    :copyright: Copyright 2021 by Sam Wilson and contributors.
    :license: BSD, see LICENSE.txt for details.

    Based on sphinx.writers.text.TextWriter, copyright 2007-2014 by the Sphinx
        team.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

from typing import Any
import pickle

from docutils import writers


class PickleWriter(writers.UnfilteredWriter):
    supported = ('rpickle',)
    settings_spec = ('No options here.', '', ())
    settings_defaults = {}

    output = None

    def __init__(self, builder: Any = None) -> None:
        super().__init__()
        self.builder = builder

    def translate(self) -> None:
        self.document.transformer = None
        self.document.reporter = None
        self.output = pickle.dumps(self.document)


Writer = PickleWriter
