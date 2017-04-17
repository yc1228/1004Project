# 1004Project

In folder part1_yc1228, it contains 10 python scripts. 

'Col_CRM_ATPT_CPTD_CD.py','Col_ID.py','Col_JURIS_DESC.py',''Col_KY_CD.py','Col_LAW_CAT_CD.py','Col_OFNS_DESC.py'
,'Col_PD_CD.py','Col_PD_DESC.py' generate outputs for each column. The output has three columns, which are 
values of each column in dataset, base type (INT,TEXT,etc), a label from the set['Null','Valid','Invalid'].
Sample codes used to run scripts on dumbo:
    spark-submit Col_CRM_ATPT_CPTD_CD.py /user/yc1228/crime.csv
    hfs -getmerge Col_CRM_ATPT_CPTD_CD.out Col_CRM_ATPT_CPTD_CD.out

'Frequency.py' genereates output files containing number of unique values for each column.
Sampe codes used to run this script on dumbo:
    spark-submit Frequency.py /user/yc1228/crime.csv
    hfs -getmerge PD_CD_Freq.csv PD_CD_Freq.csv

'Plot.py' generates bar plots for each column by using dataframes generated from 'Frequency.py'.
Sampe code used to run this script in terminal:
    python Plot.py

