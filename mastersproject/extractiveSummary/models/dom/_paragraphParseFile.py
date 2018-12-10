# -*- coding: utf-8 -*-
#Importing the libraries
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
#Importing the libraries and Utils
from itertools import chain
from ..._compat import unicode_compatible
from ...utils import cached_property
#Importing sentence parser
from ._sentenceFile import Sentence01

@unicode_compatible
class ParagraphCls(object):
    __slots__ = (
        "_sentences_var",
        "_cached_property_sentences",
        "_cached_property_headings",
        "_cached_property_words",
    )

    def __init__(self, sentences_var):
        sentences_var = tuple(sentences_var)
        for sentence_var in sentences_var:
            if not isinstance(sentence_var, Sentence01):
                raise TypeError("Instances of the class 'Sentence' are allowed Only.")

        self._sentences_var = sentences_var

    @cached_property
    def sentences(self):
        return tuple(s for s in self._sentences_var if not s.is_heading_in)

    @cached_property
    def headings(self):
        return tuple(s for s in self._sentences_var if s.is_heading_in)

    @cached_property
    def words(self):
        return tuple(chain(*(s.words_var for s in self._sentences_var)))

    def __unicode__(self):
        return "<Paragraph with %d headings & %d sentences>" % (
            len(self.headings_in),
            len(self.sentences_in),
        )

    def __repr__(self):
        return self.__str__()
