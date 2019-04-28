import urllib.request
import json
import datetime
import sys
import socket
import time
import requests
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='b30f535c6b624930bb419501ba02cece')

def getNews():
    api_url_us ='https://newsapi.org/v2/top-headlines?country=US&category=business&apiKey=b4556f6575d643c29ff519a37e93d6e0'
    api_url_gb ='https://newsapi.org/v2/top-headlines?country=GB&category=business&apiKey=b4556f6575d643c29ff519a37e93d6e0'
    api_url_ca ='https://newsapi.org/v2/top-headlines?country=CA&category=business&apiKey=b4556f6575d643c29ff519a37e93d6e0'
    api_url_au ='https://newsapi.org/v2/top-headlines?country=AU&category=business&apiKey=b4556f6575d643c29ff519a37e93d6e0'


    url_all_dict = dict()


for h in range(run_time):
# for h in range(2):
    url_img_dict = dict()
    url_title_dict = dict()
    url_desp_dict = dict()
    # for i in range(3):
    for i in range(4):
        response_us = requests.get(api_url_us)
        r1 = response_us.json()
        status = r1['status']
        if status == 'error':
            with open(file_name, 'a+') as csv_file:
                writer = csv.writer(csv_file)
                for key in url_img_dict.keys():
                    # print(key)
                    writer.writerow([key, url_title_dict[key], url_desp_dict[key], url_img_dict[key]], 'science')
            exit()
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

