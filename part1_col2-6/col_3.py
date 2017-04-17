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
unique_value=lines.map(lambda x: (x[2],1)).reduceByKey(add).collect()
#print(unique_value)

def dictionary(x):
        if x[2]== "":
                return (x[2],'NA','NA','Time','CMPLNT_FR_TM','Null')
        else:
            try:
                dt=time.strptime(x[2],"%H:%M:%S")
                if dt[3]>23 or dt[3]<0:
                        return (x[2],str(dt[3]), str(dt[4]),'Time','CMPLNT_FR_TM','Invalid')
                if dt[4]>60 or dt[4]<0:
                        return (x[2],str(dt[3]), str(dt[4]),'Time','CMPLNT_FR_TM','Invalid')
                if dt[5]>60 or dt[5]<0:
                        return (x[2],str(dt[3]), str(dt[4]),'Time','CMPLNT_FR_TM','Invalid')
                else:
                        return (x[2],str(dt[3]), str(dt[4]),'Time','CMPLNT_FR_TM','Valid')
            except ValueError:
                return (x[2],'NA','NA','Time','CMPLNT_FR_TM','Invalid')


dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5])
#dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_cmplnt_fr_tm.out")
