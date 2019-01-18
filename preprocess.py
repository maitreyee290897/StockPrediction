# -*- coding: utf-8 -*-
import json
from entity.input_data import fromJson
from util.preprocess_util import make_unigrams, make_bigrams
from entity.processed_data import ProcessedData 
from util.preprocess_util import splitParaIntoSentences

with open('input-datasets/input_data.json') as file:
    data = json.load(file)

with open('config.json') as file:
    config = json.load(file)

numberOfNewsArticles = int(config["training-data-size"])
newsArticles = []
for i in range(numberOfNewsArticles):
    newsArticles.append(fromJson(json.dumps(data["data"][i])))
    
print(len(newsArticles))
processedArticles = []
for article in newsArticles:
    sentenceList = splitParaIntoSentences(article["body"])
    unigrams = []
    bigrams = []
    for sentence in sentenceList:
        #unigrams += make_unigrams(sentence)
        bigrams += make_bigrams(sentence)
    #print(unigrams)
    print(bigrams)
    break
    """
    processedArticles.append(json.dumps(ProcessedData(article["date"], article["headline"], article["label"], article["delta"], unigrams, bigrams).__dict__))
    """

"""
with open('input-datasets/processed_data.json', 'w') as outfile:
    json.dumps({"data":processedArticles})
"""