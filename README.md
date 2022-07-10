CONTENTS OF THIS FILE
---------------------
1. Introduction
2. Requirements
3. Variables
4. Maintainer


INTRODUCTION
-----------

WIKI_COMMON_WORDS
The code takes a wiki api json link and return title and n top common words.

REQUIREMENTS
-----------

Python3 and below dependent libraries.

Request Library:
The requests module allows you to send HTTP requests using Python.
The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

WordTokenize:
word_tokenize is a function in Python that splits a given sentence into words using the NLTK library.

Punkt :
Punkt Sentence Tokenizer. This tokenizer divides a text into a list of sentences by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences. 

Stopwords:
Stopwords are the English words which does not add much meaning to a sentence. 
They can safely be ignored without sacrificing the meaning of the sentence. For example, the words like the, he, have etc. Such words are already captured this in corpus named corpus. 
We first download it to our python environment.

Pandas:
Pandas is defined as an open-source library that provides high-performance data manipulation and Analysis in Python.

VARIABLES USED
-------------
number_of_words
page_id
