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
KY_CD=lines.map(lambda x: ((x[6],x[7]),1)).reduceByKey(add)
KY_CD_sorted = KY_CD.sortBy(lambda a: a[0][1])
KY_CD_sorted.saveAsTextFile("KY_CD_Freq.csv")

PD_CD=lines.map(lambda x: ((x[8],x[9]),1)).reduceByKey(add)
PD_CD_sorted = PD_CD.sortBy(lambda a: a[0][1])
PD_CD_sorted.saveAsTextFile("PD_CD_Freq.csv")

ATPT_CPTD=lines.map(lambda x: (x[10],1)).reduceByKey(add)
ATPT_CPTD.saveAsTextFile("ATPT_CPTD_Freq.csv")

LAW_CAT_CD=lines.map(lambda x: (x[11],1)).reduceByKey(add)
LAW_CAT_CD.saveAsTextFile("LAW_CAT_CD.csv")

JURIS=lines.map(lambda x: (x[12],1)).reduceByKey(add)
JURIS.saveAsTextFile("JURIS.csv")






