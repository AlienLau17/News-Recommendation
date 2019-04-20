import requests
import time
from time import sleep
import collections
# import nltk
import csv

articles = dict()
url ='https://newsapi.org/v2/top-headlines?country=US&category=business&apiKey=b30f535c6b624930bb419501ba02cece'
response = requests.get(url)
r1 = response.json()
# articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
r2 = r1['articles']
for r in r2:
    if r['url'] not in articles:
        url = r['url']
        content = r['description']
        # if content:
        #     words = content.split(" ")
        #     lines = collections.defaultdict(lambda: 0)
        #     for w in words:
        #         if w.isalpha():
        #             lines[w] += 1

        articles[url] = content
print (articles)
