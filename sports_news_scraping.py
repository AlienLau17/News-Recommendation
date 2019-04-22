import requests
import time
from time import sleep
import csv

category = 'sports_'
date = time.strftime('%Y_%m_%d', time.localtime(time.time()))
file_name = category+date+'.csv'

url_img_dict = dict()
url_title_dict = dict()
url_desp_dict = dict()

with open(file_name, 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['url', 'title', 'description', 'urlToImage'])

run_time = 5 # hours

for i in range(run_time*60):
    url ='https://newsapi.org/v2/top-headlines?country=US&category=sport&apiKey=b30f535c6b624930bb419501ba02cece'
    response = requests.get(url)
    r1 = response.json()
    # articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
    r2 = r1['articles']
    for r in r2:
        if r['url'] not in url_img_dict:
            url = r['url']
            description = r['description']
            title = r['title']
            image_url = r['urlToImage']

            url_img_dict[url] = image_url
            url_title_dict[url] = title
            url_desp_dict[url] = description
    sleep(60)# Scraping news per minute

with open(file_name, 'a+') as csv_file:
    writer = csv.writer(csv_file)
    for key in url_img_dict.keys():
        # print(key)
        writer.writerow([key, url_title_dict[key], url_desp_dict[key], url_img_dict[key]])
