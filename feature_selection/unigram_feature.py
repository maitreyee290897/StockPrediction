# -*- coding: utf-8 -*-
import json
import numpy

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
numberOfArticles = int(config["training-data-size"])

def find_freq(term, i):
    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)
    cnt = 0
    for value in data['data'][i]['unigrams']:
        if(value == term):
            cnt = cnt + 1
    return cnt;


def find_X():
   # with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

   # with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
   # numberOfArticles = int(config["training-data-size"])
    global_unigrams = []
    for article in data['data']:
        for value in article['unigrams']:
            if(value not in global_unigrams):
                global_unigrams.append(value)

    length = len(global_unigrams)
    #create sparse matrix
    X = numpy.zeros((numberOfArticles, length))
    for i in range(numberOfArticles):
        for j in range(length):
            if global_unigrams[j] in data['data'][i]['unigrams']:
                f = find_freq(global_unigrams[j], i)
                X[i][j] = X[i][j] + f
        
    return X;

#print(X.shape)
def find_Y():
   # with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

   # with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
   # numberOfArticles = int(config["training-data-size"])
    y = []
    for i in range(numberOfArticles):
        y.append(data['data'][i]['label'])
    return y;
#print(y)
