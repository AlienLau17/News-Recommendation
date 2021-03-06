import requests
import time
from time import sleep
import collections
# import nltk
import csv
# from nltk.corpus import stopwords
# nltk.download('stopwords')

articles = dict()
for i in range(60):
    url ='https://newsapi.org/v2/top-headlines?contry=us&apiKey=b30f535c6b624930bb419501ba02cece'
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
    sleep(900)
    # time.sleep(30)

print(articles)

with open('sample3.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in articles.items():
        writer.writerow([key, value])
