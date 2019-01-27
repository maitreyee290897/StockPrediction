# -*- coding: utf-8 -*-
import json
from entity.processed_data import fromJson
import math
#d='C:/Users/Maitreyee Gadwe/Desktop/StockPrediction/feature-selection/input-datasets'
with open('input-datasets/processed_data.json',"rb") as file:
    data = json.load(file)

with open('config.json') as file:
    config = json.load(file)
numberOfAritcles = int(config["training-data-size"])
#print(numberOfAritcles)
Unigrams = []
for i in range(numberOfAritcles):
    Unigrams.append(fromJson(json.dumps(data["result"][i]["unigrams"])))
#print(Unigrams)
documentDictionaries = []
documentVectors = []
def buildDictionary(nGramsList):
 dictionary = {}
 for items in nGramsList:
	 dictionary[items] = nGramsList.count(items)
 return dictionary

for sublist in Unigrams:
    dictionary = buildDictionary(sublist)
    #print(dictionary)       
    documentDictionaries.append(dictionary)

#print(documentDictionaries)       
#print(type(documentDictionaries))
#print(type(dictionary))   

def df(term):

 cnt = 0;
 for dictionary in documentDictionaries:
	 if term in dictionary:
		 cnt = cnt + 1
 return cnt

def calculateVector(documentDictionary, numberOfdocs):

	documentVector = []
	for term in documentDictionary:
		idf_t = math.log10((1 + numberOfdocs)/(1 + df(term))) + 1;
		tfidf = documentDictionary[term] * idf_t
		documentVector.append((term, tfidf))
	#X = [value for (key, value) in documentVector]
	#X_normalized = preprocessing.normalize(X, norm='l2')
	#for value in X_normalized:
	#	key, val = documentVector.pop(0)
	#	normalizedDocumentVector.append((key, value))
	return documentVector


for Dict in documentDictionaries:
	   documentVector = calculateVector(Dict, numberOfAritcles)
	   documentVectors.append(documentVector)

print(documentVectors)