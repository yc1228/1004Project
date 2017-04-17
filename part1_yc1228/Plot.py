from __future__ import print_function

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#plot Col_ATPT_CPTP
df1 = pd.read_csv('ATPT_CPTD_Freq.csv',names=["Status","Freq"])
df1["Status"] = df1["Status"].str[2:-1]
df1["Status"][0] = "Null"
df1["Freq"] = df1["Freq"].str[:-1].astype(int)
y_pos1 = np.arange(len(df1["Status"]))
plt.bar(y_pos1,df1["Freq"],width=0.9)
plt.xticks(y_pos1,df1["Status"],rotation=45)
plt.xlabel('Indicator of whether crime was successfully completed or attempted')
plt.ylabel('Freqency')
plt.title('Freqency of crime status')
plt.show()

#Plot Col_JURIS_DESC
df2 = pd.read_csv('JURIS.csv',names=["Status","Freq"])
df2["Status"] = df2["Status"].str[2:-1]
df2["Freq"] = df2["Freq"].str[:-1].astype(int)
df2 = df2.sort(["Freq"])
df2 = df2.tail(10)
y_pos2 = np.arange(len(df2["Status"]))
plt.bar(y_pos2,df2["Freq"],width=0.5)
plt.xticks(y_pos2,df2["Status"],rotation=45)
plt.xlabel('Jurisdiction responsible for incident')
plt.ylabel('Freqency')
plt.title('Top 10 Most Frequent Jurisdiction Responsible for Incident')
plt.show()


#Plot Col_LAW_CAT_CD
df3 = pd.read_csv('LAW_CAT_CD.csv',names=["Status","Freq"])
df3["Status"] = df3["Status"].str[2:-1]
df3["Freq"] = df3["Freq"].str[:-1].astype(int)
y_pos3 = np.arange(len(df3["Status"]))
plt.bar(y_pos3,df3["Freq"],width=0.6)
plt.xticks(y_pos3,df3["Status"],rotation=45)
plt.xlabel('Level of Offense')
plt.ylabel('Freqency')
plt.title('Frequency of Each Level of Offense')
plt.show()


#Plot Col_KY_CD&DESC
df4 = pd.read_csv('KY_CD_Freq.txt',sep=",",header=None,names=["KYCD","KYDESC","Freq"])
df4["KYCD"]=df4['KYCD'].str[3:-1]
df4["KYDESC"]=df4['KYDESC'].str[:-1]
df4["Freq"]=df4['Freq'].str[:-1].astype(int)
df4=df4.sort(["Freq"])
df4=df4.tail(20)
print(df4)

y_pos4 = np.arange(len(df4["KYCD"]))
plt.bar(y_pos4, df4["Freq"], label=df4["KYDESC"],width=0.5)
plt.xticks(y_pos4, df4["KYDESC"],rotation=45,fontsize=8)
plt.xlabel('Offense Classification Code')
plt.ylabel('Frequency')
plt.title('Top 20 most frequently happened offense (code & description)')
plt.show()


#Plot Col_PD_CD&DESC
df5 = pd.read_csv('PD_CD_Freq.txt',sep=",",header=None,names=["PDCD","PDDESC","Freq"])
df5["PDCD"]=df5['PDCD'].str[3:-1]
df5["PDDESC"]=df5['PDDESC'].str[:-1]

df5["Freq"]=df5['Freq'].str[:-1].astype(int)


df5=df5.sort(["Freq"])
df5=df5.tail(20)

y_pos5 = np.arange(len(df5["PDCD"]))
plt.bar(y_pos5, df5["Freq"], label=df5["PDDESC"],width=0.5)
plt.xticks(y_pos5, df5["PDDESC"],rotation=45,fontsize=8)
plt.xlabel('Internal Classification Code')
plt.ylabel('Frequency')
plt.title('Top 20 most frequently happened offense (code & description)')
plt.show()


