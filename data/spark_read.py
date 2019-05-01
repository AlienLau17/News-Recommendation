import pyspark
from pyspark import SQLContext
from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql import Row
import panda as pd

logfile = "business/2019_business.csv"
spark = SparkSession.builder.appName("test1").getOrCreate()
logdata = spark.read.csv(logfile)
if logdata:
    print("success")
    logdata.show()