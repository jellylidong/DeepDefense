__author__ = 'vcoder'
#from pyspark import SparkContext
import os
import sys

# Set the path for spark installation
# this is the path where you have built spark using sbt/sbt assembly
os.environ['SPARK_HOME'] = "/home/vcoder/EDA/spark-1.5.0"
# os.environ['SPARK_HOME'] = "/home/jie/d2/spark-0.9.1"
# Append to PYTHONPATH so that pyspark could be found
sys.path.append("/home/vcoder/EDA/spark-1.5.0/python")
# sys.path.append("/home/jie/d2/spark-0.9.1/python")

# Now we are ready to import Spark Modules
try:
    from pyspark import SparkContext
    from pyspark import SparkConf

except ImportError as e:
    print ("Error importing Spark Modules", e)
sc = SparkContext(appName="PythonWordCount");

a =[1,2,3,4,5];
b = sc.parallelize(a);
c = b.map(lambda k :2*k);
print c.collect()