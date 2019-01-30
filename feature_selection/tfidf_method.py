# -*- coding: utf-8 -*-
import json
from entity.processed_data import fromJson
import math

with open('/home/shivali/StockPrediction/input-datasets/processed_data.json','rb') as file:
    data = json.load(file)

with open('/home/shivali/StockPrediction/config.json') as file:
    config = json.load(file)

numberOfAritcles = int(config["training-data-size"])

globalUnigramsList = []
for i in range(numberOfAritcles):
    globalUnigramsList.append(fromJson(json.dumps(data["result"][i]["unigrams"])))
globalBigrams = []
for i in range(numberOfAritcles):
    globalBigrams.append(fromJson(json.dumps(data["result"][i]["bigrams"])))

globalBigramsList=[]
for l in globalBigrams:
    couplesListPerArticle = []
    for l1 in l:
        couple = (l1[0], l1[1])
        couplesListPerArticle.append(couple)
    globalBigramsList.append(couplesListPerArticle)

#print(globalBigramsList)

#-------------Calculating tf-idf values for all ngrams------------------------#
def buildDictionary(nGramsList):
    dictionary = {}
    for items in nGramsList:
        dictionary[items] = nGramsList.count(items)
        return dictionary

def df(term, documentDictionaries):
    cnt = 0;
    for dictionary in documentDictionaries:
        if term in dictionary:
            cnt = cnt + 1
            return cnt

def calculateVector(documentDictionary, numberOfdocs, documentDictionaries):
	documentVector = []
	for term in documentDictionary:
		idf_t = math.log10((1 + numberOfdocs)/(1 + df(term, documentDictionaries))) + 1;
		tfidf = documentDictionary[term] * idf_t
		documentVector.append((term, tfidf))
	return documentVector
#-----------------------------------------------------------------------------#

documentDictionariesUnigrams = []
documentVectorsUnigrams = []
documentDictionariesBigrams = []
documentVectorsBigrams = []
for sublist in globalUnigramsList:
    dictionary = buildDictionary(sublist)
    documentDictionariesUnigrams.append(dictionary)
    
for sublist in globalBigramsList:
    dictionary = buildDictionary(sublist)
    documentDictionariesBigrams.append(dictionary)

for Dict in documentDictionariesUnigrams:
    documentVectorUnigrams = calculateVector(Dict, numberOfAritcles, documentDictionariesUnigrams)
	documentVectorsUnigrams.append(documentVectorUnigrams)

for Dict in documentDictionariesBigrams:
	documentVectorBigrams = calculateVector(Dict, numberOfAritcles, documentDictionariesBigrams)
	documentVectorsBigrams.append(documentVectorBigrams)

#print(documentVectorsUnigrams)
#print(documentVectorsBigrams)
       
with open('/home/shivali/StockPrediction/input-datasets/tf-idf_bigrams.json', 'w') as outfile:
    json.dump({"result":[ob for ob in documentVectorsBigrams]}, outfile, indent=2)
    
with open('/home/shivali/StockPrediction/input-datasets/tf-idf_unigrams.json', 'w') as outfile:
    json.dump({"result":[ob for ob in documentVectorsUnigrams]}, outfile, indent=2)
