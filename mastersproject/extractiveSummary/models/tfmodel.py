# -*- coding: utf-8 -*-
#importing the reuired util and libraries for model
from __future__ import division, print_function, unicode_literals
from __future__ import absolute_import
#Importing formating and util libraries
from collections import Sequence
from .._compat import to_unicode, unicode, string_types, Counter
from pprint import pformat

#Importing Math Library

import math

class TfDocumentModelCls(object):
    """Document model for Term-Frequency where (term = word)."""
    def __init__(self, words_var, tokenizer_in=None):
        if isinstance(words_var, string_types) and tokenizer_in is None:
            raise ValueError(
                "Tokenizer to be assigned if ``words`` is not present in the sequence.")
        elif isinstance(words_var, string_types):
            words_var = tokenizer_in.to_words(to_unicode(words_var))
        elif not isinstance(words_var, Sequence):
            raise ValueError(
                "Parameter ``words`` need to be a sequence or string along with the given tokenizer.")

        self._terms_var = Counter(map(unicode.lower, words_var))
        self._max_frequency_var = max(self._terms_var.values()) if self._terms_var else 1

    @property
    def magnitude(self):
        """
        Vector representation of the document:Length or magnitude.
        denoted as ||d||.
        """
        return math.sqrt(sum(t**2 for t in self._terms_var.values()))

    @property
    def terms(self):
        return self._terms_var.keys()

    def most_frequent_terms(self, count=0):
        """
        Returns terms count sorted in descending order
        by frequency.

        :parameter int count:
            return maximum number of terms, where 0 means no limit.
        """
        # sort terms by number of occurrences in descending order
        terms_var = sorted(self._terms_var.items(), key=lambda i: -i[1])

        terms_var = tuple(i[0] for i in terms_var)
        if count == 0:
            return terms_var
        elif count > 0:
            return terms_var[:count]
        else:
            raise ValueError(
                "Negative values are not allowed.")

    def term_frequency(self, term):
        """
        Returns frequency of term present in the document.

        :returns int:
            Returns count of words present in the document.
        """
        return self._terms_var.get(term, 0)

    def normalized_term_frequency(self, term_var, smooth_var=0.0):
        """
        Returns terms normalized frequency.

        :parameter float smooth_var:
            0.0 <= smooth_var <= 1.0, usually set to 0.4.
            It is scaling down the TF by the largest TF
            value available in document.
        :returns float:
            Frequency lies between 0.0 and 1.0, where 0 is no occurence
            and 1 is most occured.
        """
        frequency_var = self.term_frequency(term_var) / self._max_frequency
        return smooth_var + (1.0 - smooth_var)*frequency_var

    def __repr__(self):
        return "<TfDocumentModel %s>" % pformat(self._terms_var)
