# -*- coding: utf-8 -*-
import json
from entity.input_data import from_json
from preprocessing.preprocess_util import make_bigrams
from preprocessing.preprocess_util import make_unigrams
from preprocessing.preprocess_util import GARBAGE_LIST
from entity.processed_data import ProcessedData
from preprocessing.preprocess_util import split_para_into_sentences
from paths import CONFIG_PATH
from paths import PREPROCESSED_DATA_PATH
from paths import INPUT_DATA_PATH

with open(INPUT_DATA_PATH) as file:
    data = json.load(file)

with open(CONFIG_PATH) as file:
    config = json.load(file)

NUMBER_OF_ARTICLES = int(config["training-data-size"])

news_articles = []
for i in range(NUMBER_OF_ARTICLES):
    news_articles.append(from_json(json.dumps(data["data"][i])))

processedArticles = []
for article in news_articles:
    sentenceList = split_para_into_sentences(article["body"])
    unigrams = []
    bigrams = []
    for sentence in sentenceList:
        sentence.strip()
        sentence = sentence[:-2]
        for garbage in GARBAGE_LIST:
            sentence = sentence.replace(garbage[0], garbage[1])
        unigrams += make_unigrams(sentence)
        bigrams += make_bigrams(sentence)
    # print(unigrams)
    # print(bigrams)
    processedArticles.append(
        ProcessedData(article["date"], article["headline"], article["label"], article["delta"], unigrams, bigrams))

with open(PREPROCESSED_DATA_PATH, 'w') as outfile:
    json.dump({"data": [ob.__dict__ for ob in processedArticles]}, outfile, indent=2)
