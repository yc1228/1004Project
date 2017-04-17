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
#unique_value=lines.map(lambda x: (x[22],1)).reduceByKey(add).collect()
#print(unique_value)

def dictionary(x):
    if x[22]== "":
    	return (x[22],'String','Location','Null')
    try:
    	float(x[22])
    	if float(x[22])<-74.257159 and float(x[22])>-73.699215:
    		return (x[22],'String','Location','Invalid')
    	else:
    		return (x[22],'String','Location','Valid')
    except ValueError:
    	return (x[22],'String','Location','Invalid')
       
dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]).collect()
dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_Longitude.out")