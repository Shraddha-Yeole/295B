# -*- coding: utf-8 -*-

#Importing the libraries
from __future__ import division, print_function, unicode_literals
from __future__ import absolute_import
#Importing the libraries and utils
from itertools import chain
from ...utils import cached_property
from ..._compat import unicode_compatible
# DOM class for paragraphs, sentences, headings and words
@unicode_compatible
class ObjectDocumentModelMethod(object):
    def __init__(self, paragraphs_in):
        self._paragraphs_in = tuple(paragraphs_in)

    @property
    def paragraphs(self):
        return self._paragraphs_in

    @cached_property
    def sentences_C(self):
        sentences_var = (p.sentences_var for p in self._paragraphs_in)
        return tuple(chain(*sentences_var))

    @cached_property
    def headings(self):
        headings_var = (p.headings_var for p in self._paragraphs_in)
        return tuple(chain(*headings_var))

    @cached_property
    def words(self):
        words_var = (p.words_var for p in self._paragraphs_in)
        return tuple(chain(*words_var))

    def __unicode__(self):
        return "<DOM with %d paragraphs>" % len(self.paragraphs_in)

    def __repr__(self):
        return self.__str__()
