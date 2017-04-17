#!/usr/bin/python
import sys
from operator import add
from pyspark import SparkContext
from csv import reader
import re

sc = SparkContext()
lines_all = sc.textFile(sys.argv[1], 1)
lines_header = lines_all.take(1)[0]
lines=lines_all.filter(lambda line: line != lines_header)
lines = lines.mapPartitions(lambda x: reader(x))
#unique_value=lines.map(lambda x: (x[23],1)).reduceByKey(add).collect()
#print(unique_value)



#lines_filter=lines.map(lambda x: re.findall("\d+\.\d+", x[23]))
def dictionary(x):
	if x[23]=="":
		return (x[23],'String','Location','Null')
	else:
		lat_lon=re.findall("\d+\.\d+", x[23])
		#return (float(lat),float(lon))
		if lat_lon[0] != x[21] and lat_lon[1] != x[22]:
			return (x[23],'String','Location','Invalid')
		else:
			return (x[23],'String','Location','Valid')



#map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]).
dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3])
dic_value.saveAsTextFile("Col_Lat_lon.out")

