import urllib.request
import json
import datetime
import sys
import socket
import time
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# Create a receiving socket object
while True:
    TCP_IP = socket.gethostname()
    TCP_PORT = 9998

    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server on local computer
    receiver.connect((TCP_IP, TCP_PORT))
    print("Receiver connect to socket")
    sc = SparkContext(master = "local[2]", appName = "bus")
    sc.setLogLevel("ERROR")
    ssc = StreamingContext(sc, 1)
    # Create a DStream that will connect to hostname:port, like localhost:9999
    lines = ssc.socketTextStream(TCP_IP, TCP_PORT)

    # Split each line into words
    words = lines.flatMap(lambda line: line.split(","))

    # Count each word in each batch
    pairs = words.map(lambda word: (word, 1))
    wordCounts = pairs.reduceByKey(lambda x, y: x + y)

    # Print each batch
    wordCounts.pprint()

    ssc.start()             # Start the computation
    ssc.awaitTermination()  # Wait for the computation to terminate

    time.sleep(0.1)
receiver.close()


# print(receiver.recv(1024).decode('utf-8'))
