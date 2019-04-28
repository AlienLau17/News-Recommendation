import json,time,sys
sys.path.append('/home/ec2-user/lab3/utils')
import tripupdate,vehicle,alert,mtaUpdates,aws
from collections import OrderedDict
from threading import Thread
import boto3
from boto3.dynamodb.conditions import Key,Attr
import time



class dynamoMethods:

    def __init__(self, dbName):
        self.dbName = dbName
        self.resource = boto3.resource('dynamodb')
        try:
            self.resource.create_table(TableName=dbName, KeySchema=[{'AttributeName': 'tripId', 'KeyType': 'HASH'}, ],
            AttributeDefinitions=[{'AttributeName': 'tripId', 'AttributeType': 'S'}, ],
            ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5})
            self.table = self.resource.Table(dbName)
            time.sleep(15)
        except Exception as e:
            print 'Table already exists'
            self.table = self.resource.Table(dbName)
        self.count1 = 0
        self.count2 = 0


    def add(self, dict):
        try:
            response = self.table.put_item(Item = dict)
            self.count1 += 1
        except Exception as e:
            print str(e)
            print "empty row found"


    def delete(self, dict):
        response = self.table.delete_item(Key = dict)
        print response

    def delete_before(self):
        response = self.table.scan(ProjectionExpression="#id", ExpressionAttributeNames={"#id":"tripId"})
        # response = self.table.query(KeyConditionExpression=Key('deviceid').eq('20191919'))
        for i in response['Items']:
            try:
                self.table.delete_item(Key={'tripId': i['tripId']},
                                       ConditionExpression=Attr('timeStamp').lt(str(time.time()-120)))
                self.count2 += 1

            except Exception as e:
                pass

def put(a):
    try:
        while True:
            mta = mtaUpdates.mtaUpdates('34a41fb28d7324dcd8faedb0b98a1614')
            message = mta.getTripUpdates()
            map(a.add, message)
            print 'add ', a.count1
            a.count1 = 0
            time.sleep(30)
    except KeyboardInterrupt:
        print "put stop"

def de(a):
    try:
        while True:
            time.sleep(60)
            a.delete_before()
            print 'delete', a.count2
            a.count2 = 0

    except KeyboardInterrupt:
        print 'de stop'

db = dynamoMethods('mtaData')


try:
    t1 = Thread(target=put, args=(db,))
    t2 = Thread(target=de, args=(db,))
    t1.start()
    t2.start()
    # # t1.join()
    # t2.join()
except KeyboardInterrupt:
    exit()
