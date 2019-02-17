# -*- coding: utf-8 -*-
import json
import numpy

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
numberOfArticles = int(config["training-data-size"])


def find_freq1(term, i):
    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)
    cnt = 0
    for value in data['data'][i]['bigrams']:
        if(value == term):
            cnt = cnt + 1
    return cnt;

def find_X1():
    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
    #numberOfArticles = int(config["training-data-size"])
    global_bigrams = []
    for article in data['data']:
        for value in article['bigrams']:
            #print(value)
            if(value not in global_bigrams):
                global_bigrams.append(value)

    length = len(global_bigrams)
    #create sparse matrix
    X = numpy.zeros((numberOfArticles, length))
    for i in range(numberOfArticles):
        for j in range(length):
            if global_bigrams[j] in data['data'][i]['bigrams']:
                f = find_freq1(global_bigrams[j], i)
                X[i][j] = X[i][j] + f
            print(str(global_bigrams[j]) + " " + str(X[i][j]))
    return X;

def find_Y1():
    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\input-datasets\processed_data.json',"rb") as file: data = json.load(file)

    #with open(r'C:\Users\Maitreyee Gadwe\Desktop\StockPrediction\config.json') as file: config = json.load(file)
    #numberOfArticles = int(config["training-data-size"])
    y = []
    for i in range(numberOfArticles):
        y.append(data['data'][i]['label'])
    return y;
#print(y)