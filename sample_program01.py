from pyspark import SparkConf, SparkContext
import random
conf = (SparkConf()
        .setMaster("local")
        .setAppName("My app")
        .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)
text_file = sc.textFile("hdfs://localhost:1234/user/linbai023/text.txt")
counts = text_file.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("hdfs://localhost:1234/user/linbai023/wordcount02.txt")
