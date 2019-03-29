# -*- coding: utf-8 -*-
import json
import math
import numpy
from paths import PREPROCESSED_DATA_PATH
from paths import CONFIG_PATH

with open(PREPROCESSED_DATA_PATH) as file:
    data = json.load(file)

with open(CONFIG_PATH) as file:
    config = json.load(file)
NUMBER_OF_ARTICLES = int(config["training-data-size"])

'''
finds frequency of term in ith document
'''


def find_term_frequency(term, i, ngrams):
    cnt = 0
    for value in data['data'][i][ngrams]:
        if value == term:
            cnt = cnt + 1
    return cnt


'''
finds number of documents containing term
'''


def find_doc_term_frequency(term, ngrams):
    cnt = 0
    for doc in range(NUMBER_OF_ARTICLES):
        for value in data['data'][doc][ngrams]:
            if value == term:
                cnt = cnt + 1
                break
    return cnt


'''
finds tfidf value of a term in a doc
'''


def find_tfidf_value(term, doc, ngrams):
    idf_t = math.log10((1 + NUMBER_OF_ARTICLES) / (1 + find_doc_term_frequency(term, ngrams))) + 1
    tfidf = find_term_frequency(term, doc, ngrams) * idf_t
    return tfidf


'''
finds tfidf value of a term in a doc
'''


def find_tfidf_unigrams():
    global_unigrams = []
    for article in data['data']:
        for value in article['unigrams']:
            if value not in global_unigrams:
                global_unigrams.append(value)

    length = len(global_unigrams)
    # create sparse matrix
    X = numpy.zeros((NUMBER_OF_ARTICLES, length))
    for i in range(NUMBER_OF_ARTICLES):
        for j in range(length):
            X[i][j] = find_tfidf_value(global_unigrams[j], i, 'unigrams')
    return X


'''
finds tfidf value of a term in a doc
'''


def find_tfidf_bigrams():
    global_bigrams = []
    for article in data['data']:
        for value in article['bigrams']:
            if value not in global_bigrams:
                global_bigrams.append(value)

    length = len(global_bigrams)
    # create sparse matrix
    X = numpy.zeros((NUMBER_OF_ARTICLES, length))
    for i in range(NUMBER_OF_ARTICLES):
        for j in range(length):
            X[i][j] = find_tfidf_value(global_bigrams[j], i, 'bigrams')
    return X


# -----------------------------------------------------------------------------#

unigrams_tfidf = find_tfidf_unigrams()
bigrams_tfidf = find_tfidf_bigrams()
print(unigrams_tfidf)
print(bigrams_tfidf)
