# -*- coding: utf-8 -*-
import json
import numpy
from paths import PREPROCESSED_DATA_PATH
from paths import CONFIG_PATH

with open(PREPROCESSED_DATA_PATH) as file: data = json.load(
    file)

with open(CONFIG_PATH) as file: config = json.load(file)
NUMBER_OF_ARTICLES = int(config["training-data-size"])

'''
finds frequency of term in ith document
'''


def find_term_frequency(term, i):
    cnt = 0
    for value in data['data'][i]['unigrams']:
        if value == term:
            cnt = cnt + 1
    return cnt


'''
labels for all articles
'''


# Contingency table
def find_X_unigrams():
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
            if global_unigrams[j] in data['data'][i]['unigrams']:
                f = find_term_frequency(global_unigrams[j], i)
                X[i][j] = X[i][j] + f
    return X


'''
labels for all articles
'''


# Target vector
def find_Y_unigrams():
    y = []
    for i in range(NUMBER_OF_ARTICLES):
        y.append(data['data'][i]['label'])
    return y
