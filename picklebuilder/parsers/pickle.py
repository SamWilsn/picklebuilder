# -*- coding: utf-8 -*-
"""
    picklebuilder.parsers.pickle
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Custom docutils parser for pickled document trees.

    :copyright: Copyright 2021 by Sam Wilson and contributors.
    :license: BSD, see LICENSE.txt for details.
"""

from base64 import b64decode
import pickle

import docutils.parsers
from docutils.nodes import NodeVisitor


class Parser(docutils.parsers.Parser):
    supported = ('pickle64',)

    def parse(self, inputstring, document):
        self.setup_parse(inputstring, document)

        if isinstance(inputstring, str):
            text = inputstring
        else:
            text = "".join(inputstring)

        raw = b64decode(text)

        cucumber = pickle.loads(raw)

        document.extend(cucumber.children)

        document.walk(_FixDocument(document))

        self.finish_parse()


class _FixDocument(NodeVisitor):
    def dispatch_visit(self, node):
        if hasattr(node, "document"):
            node.document = self.document
