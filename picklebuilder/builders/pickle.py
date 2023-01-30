# -*- coding: utf-8 -*-
"""
    picklebuilder.builders.pickle
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Pickle Sphinx builder.

    :copyright: Copyright 2021 by Sam Wilson and contributors.
    :license: BSD, see LICENSE.txt for details.
"""

from __future__ import (print_function, unicode_literals, absolute_import)

from os import path

from gzip import GzipFile

from sphinx.builders import Builder
from sphinx.util.osutil import ensuredir
from ..writers.pickle import PickleWriter


class PickleBuilder(Builder):
    name = 'rpickle'
    format = 'pickle'
    file_suffix = '.pickle'
    link_suffix = None  # defaults to file_suffix

    def init(self):
        """Load necessary templates and perform initialization."""
        self.link_suffix = self.file_suffix

        # Function to convert the docname to a pickle file name.
        def file_transform(docname):
            return docname + self.file_suffix

        # Function to convert the docname to a relative URI.
        def link_transform(docname):
            return docname + self.link_suffix

        self.file_transform = file_transform
        self.link_transform = link_transform

    def get_outdated_docs(self):
        """
        Return an iterable of input files that are outdated.
        """
        # This method is taken from TextBuilder.get_outdated_docs()
        # with minor changes.
        for docname in self.env.found_docs:
            if docname not in self.env.all_docs:
                yield docname
                continue
            sourcename = path.join(self.env.srcdir, docname +
                                   self.file_suffix)
            targetname = path.join(self.outdir, self.file_transform(docname))
            # print (sourcename, targetname)

            try:
                targetmtime = path.getmtime(targetname)
            except Exception:
                targetmtime = 0
            try:
                srcmtime = path.getmtime(sourcename)
                if srcmtime > targetmtime:
                    yield docname
            except EnvironmentError:
                # source doesn't exist anymore
                pass

    def get_target_uri(self, docname, typ=None):
        return self.link_transform(docname)

    def prepare_writing(self, docnames):
        self.writer = PickleWriter(self)

    def write_doc(self, docname, doctree):
        outfilename = path.join(self.outdir, self.file_transform(docname))
        ensuredir(path.dirname(outfilename))
        destination = GzipFile(filename=outfilename, mode='wb', compresslevel=5)

        try:
            self.writer.write(doctree, destination)
        finally:
            destination.close()

    def finish(self):
        pass
