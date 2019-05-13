# coding: utf-8

import re
import nltk
import boto3
import codecs
import datetime
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext, Row
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

ACCESS_KEY = "AKIAZ3SCTMVTH72HUI4M"
SECRET_KEY = "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"
TOKEN = "aa"

conf = SparkConf().setAppName("spark_json")
sc = SparkContext(conf=conf)


def get_csv():
    objList = []
    titleList = ["business", "entertainment", "general", "health", "science", "sport", "technology"]
    bucket = "wildbuckets-scrapy-finance"
    file_name = "largeStream/2019_"
    s3 = boto3.client("s3",
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    for title in titleList:
        obj = s3.get_object(Bucket=bucket, Key=file_name + title + ".csv")
        objList.append(obj)
    print("*******************")
    print("s3: ")
    return objList


# read from csv file in S3
def get_csv_category(category):
    bucket = "wildbuckets-scrapy-finance"
    file_name = "largeStream/2019_" + category + ".csv"
    s3 = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY)
    obj = s3.get_object(Bucket=bucket, Key=file_name)
    body = obj['Body']
    return body


# the response of S3 bucket file is streamingBody
# read from streamingBody, paralize the file into rdd
def read_from_s3Body(category):
    body = get_csv_category(category)
    bodyList = []
    i = 0
    #     print(type(body))
    for ln in codecs.getreader('utf-8')(body):
        temp = []
        bodyTranslateList = ln.split(",")
        temp += bodyTranslateList
        bodyList.append(temp)
    re = sc.parallelize(bodyList)
    return re


def convertFromRddtoDF(category):
    spark = SparkSession.builder.appName("RDD_and_DataFrame").config("spark.some.config.option",
                                                                     "some-value").getOrCreate()
    rdd = read_from_s3Body(category)
    row_rdd = rdd.map(lambda x: Row(x))
    sqlContext = SQLContext(sc)
    df = sqlContext.createDataFrame(row_rdd, ['numbers'])
    pandas_df = df.toPandas()
    #     print(pandas_df)
    return pandas_df


def DF_reshape(df):
    dict_list = []
    for i in range(1, len(df)):
        line = df.loc[i]['numbers']
        l = len(line)
        temp_dict = {}
        temp_dict['url'] = line[0]
        temp_dict['date'] = line[-1]
        for j in range(1, l - 1):
            item = line[j]
            if j == 1:
                content = item
            else:
                content += item
        temp_dict['content'] = content
        dict_list.append(temp_dict)
        file = pd.DataFrame(dict_list)
    return file


def get_url(file):
    url = file['url']
    return url


def get_desc(file):
    desc = file['content']
    return desc


def get_date(file):
    url_date = file['date']
    return url_date


def get_url_index(file):
    url_list = get_url(file)
    index = {}
    v = 0
    for u in url_list:
        index[u] = v
        v += 1
    return index


def get_filtered_list(text, split=True, word=False):
    pattern1 = '[^\D]'  # all non-number
    pattern2 = '[^\w\s]'
    col = []
    stop_words = set(stopwords.words('english'))

    for s in text:
        s = str(s).lower()
        s = re.sub(pattern1, '', s)
        s = re.sub(pattern2, '', s)

        if split:
            s_splited = s.split()
            filtered_sentence = [w for w in s_splited if not w in stop_words]
            if word == False:
                col.append(filtered_sentence)
            else:
                for j in filtered_sentence:
                    col.append(j)
        else:
            col.append(s)
    return col


def find_similar_url(tfidf_matrix, index_matrix, url_list, url, top_n=10):
    index = index_matrix[url]
    cosine_similarities = linear_kernel(tfidf_matrix[index:index + 1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return [url_list[index] for index in related_docs_indices][0:top_n]


def get_recommend_news(url_list, file, index):
    u = get_url(file)
    d = get_desc(file)
    row = []
    for i in url_list:
        line = {}
        #         print(i)
        loc = int(index[i])
        #         print(loc)
        url = u[loc]
        desp = d[loc]
        line['url'] = url
        line['description'] = desp
        row.append(line)
    return row


def get_recommendation_from_url(category, url):
    df = convertFromRddtoDF(category)
    file = DF_reshape(df)
    description = get_desc(file)

    t = get_filtered_list(description, split=False)
    N_features = 10000
    tfid_stop_vec = TfidfVectorizer(analyzer='word', max_df=0.9, stop_words='english'
                                    , ngram_range=(1, 3), max_features=N_features)

    x_tfid_stop_train = tfid_stop_vec.fit_transform(t)
    sim = x_tfid_stop_train * x_tfid_stop_train.T
    index = get_url_index(file)
    url_list = get_url(file)
    sim_index = find_similar_url(x_tfid_stop_train, index, url_list, url)
    recommend = get_recommend_news(sim_index, file, index)
    return recommend


def exponential_decay(t, init=1, m=30, finish=0.5):
    alpha = np.log(init / finish) / m
    l = - np.log(init) / alpha
    decay = np.exp(-alpha * (t + l))
    return decay


def find_similar_matrix(tfidf_matrix, index_matrix, url, top_n=30):
    index = index_matrix[url]
    cosine_similarities = linear_kernel(tfidf_matrix[index:index + 1], tfidf_matrix).flatten()
    related_docs_indices = [i for i in cosine_similarities.argsort()[::-1] if i != index]
    return related_docs_indices[0:top_n]


def get_date_sim(date_list, sim_date):
    date_sim = []
    for i in sim_date:
        temp = date_list[i].replace('\r\n', '')
        date_sim.append(temp)
    return date_sim


def get_date_decay(date_sim):
    today = datetime.datetime.now()
    decay_list = []
    for i in date_sim:
        prev_day = datetime.datetime.strptime(i, '%Y_%m_%d')
        res = today - prev_day
        decay = exponential_decay(res.days)
        decay_list.append(decay)
    return decay_list


def get_decay_matrix(original_matrix, id_list, decay_list):
    for i in range(0, len(id_list)):
        decay = decay_list[i]
        decay_id = id_list[i]
        original_matrix[decay_id] = original_matrix[decay_id] * decay


def get_decayed_recommendation_from_url(category, url):
    df = convertFromRddtoDF(category)
    file = DF_reshape(df)
    description = get_desc(file)
    date = get_date(file)

    t = get_filtered_list(description, split=False)
    N_features = 10000
    tfid_stop_vec = TfidfVectorizer(analyzer='word', max_df=0.9, stop_words='english'
                                    , ngram_range=(1, 3), max_features=N_features)

    x_tfid_stop_train = tfid_stop_vec.fit_transform(t)

    index = get_url_index(file)
    url_list = get_url(file)

    sim_original = find_similar_matrix(x_tfid_stop_train, index, u)
    sim_date = get_date_sim(date, sim_original)
    decay_list = get_date_decay(sim_date)
    get_decay_matrix(x_tfid_stop_train, sim_original, decay_list)

    sim_index = find_similar_url(x_tfid_stop_train, index, url_list, url)
    recommend = get_recommend_news(sim_index, file, index)
    return recommend


# u = 'https://www.carltonfc.com.au/news/2019-04-26/davey-departs'
# ca = 'sport'
# rec = get_decayed_recommendation_from_url(ca, u)


