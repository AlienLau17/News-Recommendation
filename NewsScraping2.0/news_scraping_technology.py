import requests
import time
from time import sleep
import csv

run_time = 13 # hours
category = 'h_technology'
date = time.strftime('%Y_%m_%d_%H_', time.localtime(time.time()))

file_name = date + str(run_time) + category + '.csv'
# api:lb2
api_url_us ='https://newsapi.org/v2/top-headlines?country=US&category=technology&apiKey=af49402fd1814e8c8987623836708c3b'
api_url_gb ='https://newsapi.org/v2/top-headlines?country=GB&category=technology&apiKey=af49402fd1814e8c8987623836708c3b'
api_url_ca ='https://newsapi.org/v2/top-headlines?country=CA&category=technology&apiKey=af49402fd1814e8c8987623836708c3b'
api_url_au ='https://newsapi.org/v2/top-headlines?country=AU&category=technology&apiKey=af49402fd1814e8c8987623836708c3b'

# url_img_dict = dict()
# url_title_dict = dict()
# url_desp_dict = dict()

url_all_dict = dict()

with open(file_name, 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['url', 'title', 'description', 'urlToImage'])

for h in range(run_time):
# for h in range(2):
    url_img_dict = dict()
    url_title_dict = dict()
    url_desp_dict = dict()
    for i in range(4):
    # for i in range(1):
        response_us = requests.get(api_url_us)
        r1 = response_us.json()
        # articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
        status = r1['status']
        if status == 'error':
            with open(file_name, 'a+') as csv_file:
                writer = csv.writer(csv_file)
                for key in url_img_dict.keys():
                    # print(key)
                    writer.writerow([key, url_title_dict[key], url_desp_dict[key], url_img_dict[key]], 'science')
            exit()
        r2 = r1['articles']
        for r in r2:
            if r['url'] not in url_all_dict:
                url = r['url']
                url_all_dict[url] = 1
                if r['url'] not in url_img_dict:
                    url = r['url']
                    description = r['description']
                    title = r['title']
                    image_url = r['urlToImage']

                    url_img_dict[url] = image_url
                    url_title_dict[url] = title
                    url_desp_dict[url] = description

        response_gb = requests.get(api_url_gb)
        r1 = response_gb.json()
        # articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
        r2 = r1['articles']
        for r in r2:
            if r['url'] not in url_all_dict:
                url = r['url']
                url_all_dict[url] = 1
                if r['url'] not in url_img_dict:
                    url = r['url']
                    description = r['description']
                    title = r['title']
                    image_url = r['urlToImage']

                    url_img_dict[url] = image_url
                    url_title_dict[url] = title
                    url_desp_dict[url] = description

        response_ca = requests.get(api_url_ca)
        r1 = response_ca.json()
        # articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
        r2 = r1['articles']
        for r in r2:
            if r['url'] not in url_all_dict:
                url = r['url']
                url_all_dict[url] = 1
                if r['url'] not in url_img_dict:
                    url = r['url']
                    description = r['description']
                    title = r['title']
                    image_url = r['urlToImage']

                    url_img_dict[url] = image_url
                    url_title_dict[url] = title
                    url_desp_dict[url] = description

        response_au = requests.get(api_url_au)
        r1 = response_au.json()
        # articles: source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content'
        r2 = r1['articles']
        for r in r2:
            if r['url'] not in url_all_dict:
                url = r['url']
                url_all_dict[url] = 1
                if r['url'] not in url_img_dict:
                    url = r['url']
                    description = r['description']
                    title = r['title']
                    image_url = r['urlToImage']

                    url_img_dict[url] = image_url
                    url_title_dict[url] = title
                    url_desp_dict[url] = description

        sleep(900) # Scraping news per 120 seconds

    with open(file_name, 'a+') as csv_file:
        writer = csv.writer(csv_file)
        for key in url_img_dict.keys():
            # print(key)
            writer.writerow([key, url_title_dict[key], url_desp_dict[key], url_img_dict[key]])
