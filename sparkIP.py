__author__ = 'vcoder'
import os
import sys


# os.environ['SPARK_HOME'] = "/home/vcoder/EDA/spark-1.5.0"
# sys.path.append("/home/vcoder/EDA/spark-1.5.0/python")

os.environ['SPARK_HOME'] = "/home/worker/software/spark-1.5.0"
sys.path.append("/home/worker/software/spark-1.5.0/python")

from pyspark import SparkContext
from pyspark import SparkConf

# import pymongo_spark
# pymongo_spark.activate()

sc = SparkContext(appName="sparkIP");

# a =[1,2,3,4,5];
# b = sc.parallelize(a);
# c = b.map(lambda k :2*k);
# print c.collect()

a = sc.textFile('csv/output.csv')
#print a.collect()[0]
b = a.map(lambda line: line.split(',')).map(lambda val:(val[1], val[2]))
print b.collect()[0:10]

import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['test']
ips = db.ips3
content = {"fileName": "testIP",
            "IPs": b.collect()[0:10]}
ips.insert_one(content)
aaa = ips.find()
print aaa[0]['IPs'][0][0]

sc.stop()