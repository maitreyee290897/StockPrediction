# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from entity.input_data import InputData

from bs4 import BeautifulSoup
from paths import INPUT_DATA_PATH
from paths import URLS_PATH

BASE_URL = "https://www.business-standard.com"
COMPANY_RELIANCE = "/topic/reliance-industries/"
PAGE_NO = 3


# scrapes business standard website to get urls_Reliance for company's news articles
def get_news_articles_urls(base_url, company):
    news_articles_urls = []
    for pageNo in range(PAGE_NO):
        url = base_url + company + str(pageNo)
        html = urlopen(url)
        soup = BeautifulSoup(html, 'lxml')
        wanted_text = soup.findAll('h2')
        for h2 in wanted_text:
            for link in h2.find_all('a'):
                # print(baseUrl + link.get('href'))
                news_articles_urls.append(BASE_URL + link.get('href'))
    return news_articles_urls


# read all urls_Reliance for a particular company from file
def fetch_all_urls_from_file(company):
    # get all the urls_Reliance
    with open(URLS_PATH) as f:
        content = f.readlines()
    urls = [x.strip() for x in content]
    # print(urls_Reliance)
    return urls


# urls_Reliance = get_news_articles_urls(BASE_URL, COMPANY_RELIANCE)
# with open(URLS_PATH, 'w') as f:
#     for item in urls_Reliance:
#         f.write("%s\n" % item)
#
urls = fetch_all_urls_from_file(URLS_PATH)

input_data = []
for newsUrl in urls:
    # send a request to url and get the news content
    try:
        html = urlopen(newsUrl)
        soup = BeautifulSoup(html, 'lxml')
        wanted_text = soup.findAll('script', {'type': 'application/ld+json'})
        body = wanted_text[1].string
        body = body.strip()

        # get article body
        id1 = body.find("articleBody")
        id2 = body.find("articleSection")
        articleBody = body[id1 + 14:id2 - 3]
        articleBody = articleBody.strip()
        # print(articleBody)

        # get headline
        id1 = body.find("headline")
        id2 = body.find("author")
        headline = body[id1 + 12:id2 - 3]
        headline = headline.strip()
        # print(headline)

        # get date
        id1 = body.find("datePublished")
        id2 = body.find("dateModified")
        date = body[id1 + 17:id2 - 3]
        date = date.strip()
        print(date)
    except:
        continue

    input_data.append(InputData(date, headline, articleBody, "", ""))

# dump news articles data as json file
with open(INPUT_DATA_PATH, 'w') as outfile:
    json.dump({"data": [ob.__dict__ for ob in input_data]}, outfile, indent=2)
