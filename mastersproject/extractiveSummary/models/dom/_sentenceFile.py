# -*- coding: utf-8 -*-
#Importing the libraries
from __future__ import division, print_function, unicode_literals
from __future__ import absolute_import

#importing the reuired util and libraries for model
from ..._compat import to_unicode, to_string, unicode_compatible
from ...utils import cached_property




@unicode_compatible
class Sentence01(object):
    __slots__ = ("_txt", "_cached_property_words", "_tokenizer_in", "_is_heading_in",)

    def __init__(self, txt, tokenier_in, is_heading_in=False):
        self._txt = to_unicode(txt).strip()
        self._tokenizer_in = tokenizer_in
        self._is_heading_in = bool(is_heading_in)

    @cached_property
    def words(self):
        return self._tokenizer_in.to_words(self._txt)

    @property
    def is_heading_in(self):
        return self._is_heading_in

    def __eq__(self, sentence_in):
        assert isinstance(sentence_in, Sentence01)
        return self._is_heading_in is sentence_in._is_heading_in and self._txt == sentence._txt

    def __ne__(self, sentence_in):
        return not self.__eq__(sentence_in)

    def __hash__(self):
        return hash((self._is_heading_in, self._txt))

    def __unicode__(self):
        return self._txt

    def __repr__(self):
        return to_string("<%s: %s>") % (
            "Heading" if self._is_heading_in else "Sentence",
            self.__str__()
        )
