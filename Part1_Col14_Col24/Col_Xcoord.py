#!/usr/bin/python
import sys
from operator import add
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines_all = sc.textFile(sys.argv[1], 1)
lines_header = lines_all.take(1)[0]
lines=lines_all.filter(lambda line: line != lines_header)
lines = lines.mapPartitions(lambda x: reader(x))
#unique_value=lines.map(lambda x: (x[19],1)).reduceByKey(add).collect()
#print(unique_value)

def dictionary(x):
	if x[19]== "":
		return (x[19],'String','Location','Null')
	elif x[19].isdigit():
		if float(x[19])<913174.999355 and float(x[19])>1067382.508423:
			return (x[19],'String','Location','Invalid')
		else:
			return (x[19],'String','Location','Valid')
	else:
		return (x[19],'String','Location','Invalid')



dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]).collect()
dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_Xcoord.out")

