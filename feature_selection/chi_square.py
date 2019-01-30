# -*- coding: utf-8 -*-
import json
#from sklearn.feature_selection import SelectKBest
#from sklearn.feature_selection import chi2

with open('/home/shivali/StockPrediction/input-datasets/processed_data.json') as file:
    data = json.load(file)

#with open('/home/shivali/StockPrediction/input-datasets/tf-idf_unigrams.json','r') as file:
#    bigram_list = json.load(file)









global_unigrams = [[],[]]
for article in data['data']:
    for value in article['unigrams']:
        global_unigrams[0].append(value)
        global_unigrams[1].append(article['label'])

length = len(global_unigrams[0])
#print(global_unigrams)
#for i in range(0,length):
#    print(global_unigrams[0][i] +' '+ str(global_unigrams[1][i]))
            

X = global_unigrams[0]
y = global_unigrams[1] 
print(X.shape)

#X_new = SelectKBest(chi2, k=2).fit_transform(X, y)
#X_new.shape
#(150, 2)
