from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines_all = sc.textFile(sys.argv[1], 1)
lines_header = lines_all.first()
lines=lines_all.filter(lambda line: line != lines_header)
lines = lines.mapPartitions(lambda x: reader(x))
unique_value=lines.map(lambda x: (x[10],1)).reduceByKey(add).collect()
#print(unique_value)
#print([i[0] for i in unique_value])
unique_list = [i[0] for i in unique_value]

def dictionary(x):
    if x[10]== "":
        return (x[10],'TEXT','Indicator of whether crime was successfully completed or attempted','Null')
    else:
        if x[10].upper() in unique_list:
            return (x[10],'TEXT','Indicator of whether crime was successfully completed or attempted','Valid')
        else:
            return (x[10],'TEXT','Indicator of whether crime was successfully completed or attempted','Invalid')

dic_value= lines.map(lambda x: dictionary(x)).map(lambda x: "{0}\t{1}\t{2}\t{3}".format(x[0], x[1], x[2], x[3]))
#dic_value=sc.parallelize(dic_value)
dic_value.saveAsTextFile("Col_CRM_ATPT_CPTD_CD.out")



