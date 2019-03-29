# -*- coding: utf-8 -*-
import csv
import json
from datetime import datetime
from paths import STOCKS_CSV_DATA_PATH
from paths import INPUT_DATA_PATH
from paths import LABELLED_DATA_PATH

DATE_FORMAT_STOCKS_CSV = '%d-%B-%Y'
DATE_FORMAT_ARTICLES = '%Y-%m-%d'
START_DATE = '1-January-2016'
END_DATE = '15-February-2019'

# create list from the stock price data
with open(STOCKS_CSV_DATA_PATH) as stocks_file:
    stocks_reader = csv.reader(stocks_file)
    stock_data = [[], [], []]
    for row in stocks_reader:
        # extract the datetime object from the existing date pattern (dd-full month-full year)
        date = datetime.strptime(row[0], DATE_FORMAT_STOCKS_CSV).date()
        stock_data[0].append(date)  # Date
        stock_data[1].append(row[1])  # Delta
        stock_data[2].append(row[2])  # Label

# specify the start and end of stock data set
first_date = datetime.strptime(START_DATE, DATE_FORMAT_STOCKS_CSV).date()
last_date = datetime.strptime(END_DATE, DATE_FORMAT_STOCKS_CSV).date()

# load the unlabelled json file and modify the data
with open(INPUT_DATA_PATH) as unlabelled_jsonfile:
    working_data = json.load(unlabelled_jsonfile)
    # search each article's date in the stock_data and update delta/label
    for article in working_data['data']:
        article['date'] = article['date'][0:10]
        article_date = datetime.strptime(article['date'], DATE_FORMAT_ARTICLES).date()
        # find corresponding stock date
        if article_date > last_date or article_date < first_date:
            print(article_date)
            print('Out of date range!')  # skip this article as label not known
        else:
            if article_date in stock_data[0]:
                stock_date = article_date
            else:
                # select a valid stock date
                for i in range(len(stock_data[0])):
                    if article_date < stock_data[0][i]:
                        stock_date = stock_data[0][i - 1]
                        break;
            delta = stock_data[1][stock_data[0].index(stock_date)]
            label = stock_data[2][stock_data[0].index(stock_date)]
            article['delta'] = delta
            article['label'] = label

# dump the labelled data
with open(LABELLED_DATA_PATH, 'w') as labelled_jsonfile:
    json.dump(working_data, labelled_jsonfile, indent=2)
