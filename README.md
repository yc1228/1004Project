# 1004Project

### part1_yc1228

**In folder part1_yc1228, it contains 10 python scripts.**

1. 'Col_CRM_ATPT_CPTD_CD.py','Col_ID.py','Col_JURIS_DESC.py',''Col_KY_CD.py','Col_LAW_CAT_CD.py','Col_OFNS_DESC.py'
,'Col_PD_CD.py','Col_PD_DESC.py' generate outputs for each column. The output has three columns, which are values of each column in dataset, base type (INT,TEXT,etc), a label from the set['Null','Valid','Invalid'].
Sample codes used to run scripts using pyspark on dumbo: 
```
spark-submit Col_CRM_ATPT_CPTD_CD.py /user/yc1228/crime.csv
hfs -getmerge Col_CRM_ATPT_CPTD_CD.out Col_CRM_ATPT_CPTD_CD.out
```

2. 'Frequency.py' genereates output files containing number of unique values for each column.
Sampe codes used to run this script using pyspark on dumbo:
```
spark-submit Frequency.py /user/yc1228/crime.csv;
hfs -getmerge PD_CD_Freq.csv PD_CD_Freq.csv;
```

3. 'Plot.py' generates bar plots for each column by using dataframes generated from 'Frequency.py'.
Sampe code used to run this script in terminal:
```
python Plot.py
```

### Part1_Col14_Col24

**In folder Part1_Col14_Col24, it contains 12 python scripts and 1 python notebook file.**

1. The first 11 scripts: 'Col_Boro.py', 'Col_Precinct.py', 'Col_Loc.py', 'Col_Pre.py', 'Col_Park.py', 'Col_NYCHA.py', 'Col_Xcoord.py', 'Col_ycoord.py', 'Col_Latitude.py', 'Col_Longitude.py', 'Col_Latlon.py' generate outputs for each column 14 to column 24 in the dataset. The output has four columns, which are values of each column in dataset, base type (INT,TEXT,etc), semi type (Location, time, etc), and quality label from the set (Null, Valid, Invalid). Sample codes used to run scripts using pyspark on dumbo: 
```
spark-submit Col_Boro.py crime.csv;
hfs -get Col_Boro.out
hfs -getmerge Col_Boro.out Col_Boro_merge.out;
```

2. 'unique_value.py' is a reproducible function which output unique value for column 14 to column 24 at the sametime. Sample codes used to run scripts using pyspark on dumbo: 
```
spark-submit unique_value.py.py crime.csv;
hfs -get unique_value13.out
hfs -getmerge unique_value13.out unique_value13_merge.out;
hfs -get unique_value14.out
hfs -getmerge unique_value14.out unique_value14_merge.out;
```

3. Crime_Column14_24.ipynb reads the merged pyspark output from dumbo, and generate data summary including frequency tables and plots for column 14 to 24. Codes and results can be viewed in the notebook.


### part1_ym910

**In folder part1_col2-6, it contains 5 python scripts.**

1. 'Col_2.py','Col_3.py','Col_4.py','Col_5.py','Col_6.py',generate outputs for each column. The output has 6 columns for 3 date-related data, which are values of each column in dataset, base type (INT,time, date ,etc), 3 integers that indicates the year, month and day of each date, and a label from the set['Null','Valid','Invalid']; 5 columns for time-related data, which are values of each column in dataset, base type (INT,TEXT,etc), 2 integers that indicates the hour and minute of each time, and a label from the set['Null','Valid','Invalid'].
Sample codes used to run scripts using pyspark on dumbo: 
```
spark-submit Col_2.py crime.csv
hfs -getmerge Col_CMPLNT_FR_DT.out col_2_result.out
```

2. Crime_Column2-6.ipynb reads the merged pyspark output from dumbo, and generate data summary including frequency tables and plots for column 2 to 6. Codes and results can be viewed in the notebook.
```
python Plot.py
```

3. code used to count null in local pyspark
```
df=spark.read.csv("/Users/zoem/Documents/DS1004/term_project/data/crime.csv",header=True,mode="DROPMALFORMED")
null_date=df.filter(df.CMPLNT_FR_DT.isNull()).count()
```
