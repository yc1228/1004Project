#!/usr/bin/python
import sys
from operator import add
from pyspark import SparkContext
from pyspark.sql import SparkSession
from csv import reader
import matplotlib.pyplot as plt

sc = SparkContext()
lines_all = sc.textFile(sys.argv[1], 1)
lines_header = lines_all.first()
lines=lines_all.filter(lambda line: line != lines_header)
lines = lines.mapPartitions(lambda x: reader(x))
def unique_value(i):
	unique_value=lines.map(lambda x: (x[i],1)).reduceByKey(add).collect()
	unique_value=sc.parallelize(unique_value)
	unique_value.saveAsTextFile("unique_value"+str(i)+".out")

unique_value(13)
unique_value(14)
unique_value(15)
unique_value(16)
unique_value(17)
unique_value(18)
unique_value(19)
unique_value(20)
unique_value(21)
unique_value(22)
unique_value(23)