# Make Python 2/3 compatible codebase
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals


from django.http import HttpResponse
from django.shortcuts import render

from extractiveSummary.parser.html import HtmlParser
from extractiveSummary.nlp.tokenizers import Tokenizer
from extractiveSummary.summarizer.lsa import LsaSummarizer as Summarizer
from extractiveSummary.nlp.stemmers import Stemmer
from extractiveSummary.utils import get_stop_words


LANGUAGE = "english"



def homepage(request):
	return render(request, 'home.html')

def count(request):
	URL = request.GET.get('urlvalue')
	SENTENCES_COUNT = request.GET.get('SENTENCES_COUNT')
	parser = HtmlParser.blogFromUrl(URL, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	result = []
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
    		result.append(sentence)

		
	return render(request, 'count.html', {'result': result})
	
