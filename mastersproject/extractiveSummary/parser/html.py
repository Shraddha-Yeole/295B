# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from breadability.readable import Article
from ..utils import cached_property, fetch_url
from ..models.dom import Sentence01, ParagraphCls, ObjectDocumentModelMethod
from .parser import DocumentParser


class HtmlParser(DocumentParser):
    SIGNIFICANT_TAGS = (
        "b",  "big",
        "dfn",
        "em",
        "h1", "h2", "h3",
        "strong",
    )

    @classmethod
    def from_string(cls, string, url, tokenizer):
        return cls(string, tokenizer, url)

    @classmethod
    def from_file(cls, file_path, url, tokenizer):
        with open(file_path, "rb") as file:
            return cls(file.read(), tokenizer, url)

    @classmethod
    def blogFromUrl(cls, url, tokenizer):
        content = fetch_url(url)
        return cls(content, tokenizer, url)

    def __init__(self, html_content, tokenizer, url=None):
        super(HtmlParser, self).__init__(tokenizer)
        self._article = Article(html_content, url)

    @cached_property
    def significant_words(self):
        wordsList = []
        for paragraph in self._article.main_text:
            for text, annotations in paragraph:
                if self._contains_any(annotations, *self.SIGNIFICANT_TAGS):
                    wordsList.extend(self.tokenize_words(text))

        if wordsList:
            return tuple(wordsList)
        else:
            return self.SIGNIFICANT_WORDS

    @cached_property
    def stigma_words(self):
        wordsList = []
        for paragraph in self._article.main_text:
            for text, annotations in paragraph:
                if self._contains_any(annotations, "a", "strike", "s"):
                    wordsList.extend(self.tokenize_words(text))

        if wordsList:
            return tuple(wordsList)
        else:
            return self.STIGMA_WORDS

    def _contains_any(self, seq, *args):
        if seq is None:
            return False

        for i in args:
            if i in seq:
                return True

        return False

    @cached_property
    def document(self):
        annotated_text = self._article.main_text

        paragraphList = []
        for paragraph in annotated_text:
            sentenceList = []

            current_text = ""
            for text, annotations in paragraph:
                if annotations and ("h1" in annotations or "h2" in annotations or "h3" in annotations):
                    sentenceList.append(Sentence(text, self._tokenizer, is_heading=True))
                elif not (annotations and "pre" in annotations):
                    current_text += " " + text

            newSentences = self.tokenize_sentences(current_text)
            sentenceList.extend(Sentence(s, self._tokenizer) for s in newSentences)
            paragraphList.append(Paragraph(sentenceList))

        return ObjectDocumentModelMethod(paragraphs)
