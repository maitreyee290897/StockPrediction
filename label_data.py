# -*- coding: utf-8 -*-
import csv
import json
from datetime import datetime

#create list from the stock price data
with open('/home/shivali/StockPrediction/input-datasets/last5year_short.csv') as stocks_file:
    stocks_reader = csv.reader(stocks_file)
    stock_data = [[],[],[]]
    for row in stocks_reader:
        #extract the datetime object from the existing date pattern
        date = datetime.strptime(row[0],'%d-%B-%Y').date()
        stock_data[0].append(date)    #Date
        stock_data[1].append(row[1])  #Delta
        stock_data[2].append(row[2])  #Label

#specify the start and end of stock data set
first_date = datetime.strptime('1-January-2016','%d-%B-%Y').date()
last_date = datetime.strptime('31-December-2018','%d-%B-%Y').date()

#load the unlabelled json file and modify the data
with open('/home/shivali/StockPrediction/input-datasets/input_data.json') as unlabelled_jsonfile:  
    working_data = json.load(unlabelled_jsonfile)
    #search each article's date in the stock_data and update delta/label
    for article in working_data['data']:
        article_date = datetime.strptime(article['date'],'%d-%B-%Y').date()
        #find corresponding stock date
        if(article_date > last_date or article_date < first_date):
            print(article_date)
            print('Out of date range!')#skip this article as label not known
        else:
            if(article_date in stock_data[0]):
                stock_date = article_date
            else:
                #select a valid stock date
                for i in range(len(stock_data[0])):
                    if(article_date < stock_data[0][i]):
                        stock_date = stock_data[0][i-1]
                        break;
            delta = stock_data[1][stock_data[0].index(stock_date)]
            label = stock_data[2][stock_data[0].index(stock_date)]
            article['delta'] = delta
            article['label'] = label

#dump the labelled data
with open('/home/shivali/StockPrediction/input-datasets/labelled_data.json', 'w') as labelled_jsonfile:  
    json.dump(working_data, labelled_jsonfile, indent=2)
