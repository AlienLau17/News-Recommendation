import urllib.request
import json
import datetime
import sys
import socket
import time

def getBuses(route=''):

    #Base URL for MARTA API
    base = 'http://developer.itsmarta.com/BRDRestService/RestBusRealTimeService/'

    # If user does not input a value for route number, use 'GetAllBus' API call
    if route == '':
        query = 'GetAllBus'

    # Else, use 'GetBusByRoute' API call with user-defined route number
    else:
        query = 'GetBusByRoute/' + route

    # Formulate URL request and format response as json object
    full_api = base+query
    response = urllib.request.urlopen(full_api, timeout=30)
    str_response = response.read().decode('utf-8')
    buses = json.loads(str_response)

    # Prints entirety of json response
    #print(buses)
    #print(bus['ROUTE'] + '  LAT:' + bus['LATITUDE'] + '  LON:' + bus['LONGITUDE'] + '  ADHER:' + bus['ADHERENCE'] + '  VEHICLE:' + bus['VEHICLE'] + '\n')
    return buses

# while True:
TCP_IP = socket.gethostname()
TCP_PORT = 9998
# socket.setdefaulttimeout(30)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
s.bind((TCP_IP, TCP_PORT))
print('Socket bind complete')
s.listen(1)
print('Socket now listening')
print("Waiting for TCP connection...")

c, addr = s.accept()
print('Got connection from', addr)

while True:
    resp = getBuses()
    bus = resp[0]
    print(bus)

    info = bus['ROUTE'] + ','+ bus['DIRECTION'] +','+bus['MSGTIME']+','+bus['STOPID']+ ','+bus['TIMEPOINT']+ ',' +bus['LATITUDE']+ ','+bus['LONGITUDE']+ ','+ '\n'
    c.sendall(info.encode('utf-8'))
    time.sleep(0.5)

s.close()
