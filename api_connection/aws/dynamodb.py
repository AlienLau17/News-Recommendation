import json,time,sys
# sys.path.append('/home/ec2-user/lab3/utils')
# import tripupdate,vehicle,alert,mtaUpdates,aws
from collections import OrderedDict
from threading import Thread
import boto3
from boto3.dynamodb.conditions import Key,Attr
import time
import csv
import collections

def convert_csv_to_json_list():
   items = []
   file = "/Users/zs/Dropbox/largestream/News-Recommendation/sports_2019_04_22.csv"
   with open(file) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          data = {}
        #   data = collections.defaultdict(dict)
          data['url'] = row['url']
          data['title'] = row['title']
          data['description'] = row['description']
          data['urlToImage'] = row['urlToImage']

          print(data)
          #populate remaining fields here
          #................
          items.append(data)
   return items

def batch_write(items):
   dynamodb = boto3.resource('dynamodb')
   db = dynamodb.Table('newsDemoTable2')

   with db.batch_writer() as batch:
      for item in items:
         batch.put_item(Item=item)
         print("put: ", item)
        


if __name__ == '__main__':
   json_data = convert_csv_to_json_list()
   batch_write(json_data)


# class dynamoMethods:

#     def __init__(self, dbName):
#         self.dbName = dbName
#         self.resource = boto3.resource('dynamodb')