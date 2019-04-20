import requests

articles = []
url ='https://newsapi.org/v2/top-headlines?country=us&apiKey=b30f535c6b624930bb419501ba02cece'
response = requests.get(url)
r1 = response.json()
r2 = r1['articles']
length = len(r2)
for i in range(length):
    articles.append(r2[i]['content'])

with open('sample.txt', 'w') as f:
    for item in articles:
        f.write("\n")
        f.write(item)
