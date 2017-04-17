#!/usr/bin/python
import sys
from operator import add
from pyspark import SparkContext
from csv import reader
import time

sc = SparkContext()
lines_all = sc.textFile(sys.argv[1], 1)
lines_header = lines_all.first()
lines=lines_all.filter(lambda line: line != lines_header)
lines = lines.mapPartitions(lambda x: reader(x))
unique_value=lines.map(lambda x: (x[5],1)).reduceByKey(add).collect()
#print(unique_value)

def dictionary(x):
        if x[5]== "":
                return (x[5],'NA','NA','NA','Text','RPT_DT','Null')
        else:
                dt=time.strptime(x[5],"%m/%d/%Y")
                if dt[0]>2016 or dt[0]<2005:
                        return (x[5],str(dt[0]), str(dt[1]),str(dt[2]),'Date','RPT_DT','Invalid')
                if dt[2]>31 or dt[2]<0:
                        return (x[5],str(dt[0]), str(dt[1]),str(dt[2]),'Date','RPT_DT','Invalid')
                if dt[1]>12 or dt[1]<0:
                        return (x[5],str(dt[0]), str(dt[1]),str(dt[2]),'Date','RPT_DT','Invalid')
                else:
                        return (x[5],str(dt[0]), str(dt[1]),str(dt[2]),'Date','RPT_DT','Valid')

dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
#dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_rpt_dt.out")
