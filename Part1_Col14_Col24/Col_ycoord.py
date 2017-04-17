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
#unique_value=lines.map(lambda x: (x[20],1)).reduceByKey(add).collect()
#print(unique_value)



def dictionary(x):
	if x[20]== "":
		return (x[20],'String','Location','Null')
	elif x[20].isdigit():
		#float(x[20])
		if float(x[20])>272844.293640 and float(x[20])<120121.779352:
			return (x[20],'String','Location','Invalid')
		else:
			return (x[20],'String','Location','Valid')
	else:
		return (x[20],'String','Location','Invalid')


dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]).collect()
dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_ycoord.out")