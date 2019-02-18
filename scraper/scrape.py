# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from urllib.request import Request, urlopen
from entity.input_data import InputData 

from bs4 import BeautifulSoup

#scrapes business standard website to get urls for company's news articles
def getNewsArticlesUrls(baseUrl, company):    
    newsArticlesUrls = []
    for pageNo in range(5):
        url = baseUrl + company + str(pageNo)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        wanted_text = soup.findAll('h2')
        for h2 in wanted_text:
            for link in h2.find_all('a'):
                print(baseUrl + link.get('href'))
                newsArticlesUrls.append('https://www.business-standard.com' + link.get('href'))
    return newsArticlesUrls

baseUrl = "https://www.business-standard.com"
company = "/topic/reliance-industries/"
#urls = getNewsArticlesUrls(baseUrl, company)

#get all the urls
with open("urls") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
urls = [x.strip() for x in content]
#print(urls)

input_data = []
for newsUrl in urls:
    #req = Request(newsUrl, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urlopen(newsUrl)
    except:
        continue
    soup = BeautifulSoup(html, 'lxml')
    wanted_text = soup.findAll('script', {'type': 'application/ld+json'})
    body = wanted_text[1].string
    body = body.strip()
    
    #get article body
    id1 = body.find("articleBody")
    id2 = body.find("articleSection")
    articleBody = body[id1+14:id2-3]
    articleBody = articleBody.strip()
    print(articleBody)
    
    #get headline
    id1 = body.find("headline")
    id2 = body.find("author")
    headline = body[id1+12:id2-3]
    headline = headline.strip()
    print(headline)
    
    #get date
    id1 = body.find("datePublished")
    id2 = body.find("dateModified")
    date = body[id1+17:id2-3]
    date = date.strip()
    print(date)

    #myDictObj = { "date":date, "headline":headline, "body":articleBody, "label":"", "delta":"" }
    '''
    data = {}
    data['date'] = date
    data['headline'] = headline
    data['body'] = articleBody
    data['label'] = ""
    data['delta'] = ""
    json_data = json.dumps(data)
    '''
    input_data.append(InputData(date, headline, articleBody, "", ""))
    
with open(r'/home/anany/Desktop/StockPrediction/input-datasets/input_data3.json', 'w') as outfile:
    #serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
    #print(serialized)
    json.dump({"data":[ob.__dict__ for ob in input_data]}, outfile, indent=2)