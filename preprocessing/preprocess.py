# -*- coding: utf-8 -*-
import json
from entity.input_data import fromJson
from util.preprocess_util import make_unigrams, make_bigrams
from entity.processed_data import ProcessedData 
from util.preprocess_util import splitParaIntoSentences

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\input_data.json') as file:
    data = json.load(file)

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file:
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
        sentence.strip()
        sentence = sentence[:-2]
        sentence = sentence.replace("\r"," ")
        sentence = sentence.replace("\n"," ")
        sentence = sentence.replace("\t"," ")
        sentence = sentence.replace("&#39;", "'")
        sentence = sentence.replace("&quot;",'\" ')
        sentence = sentence.replace("&nbsp;",' ')
        unigrams += make_unigrams(sentence)
        bigrams += make_bigrams(sentence)
    #print(unigrams)
    #print(bigrams)
    processedArticles.append(ProcessedData(article["date"], article["headline"], article["label"], article["delta"], unigrams, bigrams))

#print(json.dumps({"result":[ob.__dict__ for ob in processedArticles]}))

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json', 'w') as outfile:
    json.dump({"result":[ob.__dict__ for ob in processedArticles]}, outfile, indent=2)
