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
    for value in data['data'][i]['bigrams']:
        if value == term:
            cnt = cnt + 1
    return cnt


'''
X1() - Dictionary
'''


def find_X_bigrams():
    global_bigrams = []
    for article in data['data']:
        for value in article['bigrams']:
            # print(value)
            if value not in global_bigrams:
                global_bigrams.append(value)

    length = len(global_bigrams)
    # create sparse matrix
    X = numpy.zeros((NUMBER_OF_ARTICLES, length))
    for i in range(NUMBER_OF_ARTICLES):
        for j in range(length):
            if global_bigrams[j] in data['data'][i]['bigrams']:
                f = find_term_frequency(global_bigrams[j], i)
                X[i][j] = X[i][j] + f
            # print(str(global_bigrams[j]) + " " + str(X[i][j]))
    return X


'''
labels for all articles
'''


def find_Y_bigrams():
    y = []
    for i in range(NUMBER_OF_ARTICLES):
        y.append(data['data'][i]['label'])
    return y
# print(y)
