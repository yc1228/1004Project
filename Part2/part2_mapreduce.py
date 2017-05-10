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

def year_borough(x):
       
        if x[1]== "" or x[13]=="":
                return ('Invalid', 'Invalid')
        else:
                dt=time.strptime(x[1],"%m/%d/%Y")
                if dt[0]>2016 or dt[0]<2006:
                        return ('Invalid', x[13])
                if dt[2]>31 or dt[2]<0:
                        return ('Invalid', x[13])
                if dt[1]>12 or dt[1]<0:
                        return ('Invalid', x[13])
                else:
                        return (str(dt[0]), x[13])
def year_KYPD(x):
       
        if x[1]== "" or x[6]=="":
                return ('Invalid', 'Invalid')
        else:
                dt=time.strptime(x[1],"%m/%d/%Y")
                if dt[0]>2016 or dt[0]<2006:
                        return ('Invalid', x[6])
                if dt[2]>31 or dt[2]<0:
                        return ('Invalid', x[6])
                if dt[1]>12 or dt[1]<0:
                        return ('Invalid', x[6])
                else:
                        return (str(dt[0]), x[6])

def year_type(x):
       
        if x[1]== "" or x[7]=="":
                return ('Invalid', 'Invalid')
        else:
                dt=time.strptime(x[1],"%m/%d/%Y")
                if dt[0]>2016 or dt[0]<2006:
                        return ('Invalid', x[7])
                if dt[2]>31 or dt[2]<0:
                        return ('Invalid', x[7])
                if dt[1]>12 or dt[1]<0:
                        return ('Invalid', x[7])
                else:
                        return (str(dt[0]), x[7])
def month_borough(x):
       
        if x[1]== "" or x[13]=="":
                return ('Invalid', 'Invalid','Invalid')
        else:
                dt=time.strptime(x[1],"%m/%d/%Y")
                if dt[0]>2016 or dt[0]<2006:
                        return ('Invalid','Invalid', x[13])
                if dt[2]>31 or dt[2]<0:
                        return ('Invalid', 'Invalid',x[13])
                if dt[1]>12 or dt[1]<0:
                        return ('Invalid','Invalid', x[13])
                else:
                        return (str(dt[0]), str(dt[1]), x[13])


dic_value= lines.map(lambda x: year_borough(x)).map(lambda x: ((x[0],x[1],x[2]),1)).reduceByKey(add).filter(lambda x: x[0][0] != 'Invalid')
dic_value=dic_value.map(lambda x: x[0][0]+"\t"+x[0][1]+"\t"+str(x[1])).collect()
dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("part2.out")

