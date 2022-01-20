# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 09:44:41 2021

@author: Administrator
"""

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
fd='Tailand_Facebook Live Sellers  Data Set.csv'
with open(fd, encoding= 'utf8') as file2:
          csvReader= csv.reader(file2)
          listInput= list(csvReader) 
col=['status_id','status_type','status_published',
      'num_reactions','num_comments','num_shares',
      'num_likes','num_loves','num_wows','num_hahas',
      'num_sads','num_angrys','1','2','3','4']
df2=pd.DataFrame(listInput,columns=col)
#drop調不需要的列和欄
df=df2.drop(['status_id','status_published','num_loves','num_wows','num_hahas','num_sads','num_angrys','1','2','3','4'],axis=1)
Thailand=df2=df.drop([0],axis=0)

import sqlite3
conn=sqlite3.connect('Thailand.sqlite')
cursor=conn.cursor()
sqlstr='''CREATE TABLE IF NOT EXISTS Thailand \
    (
      "status_type" TEXT,
      "status_published" Text,
      "num_reactions" Integer,
      "num_comments" Integer,
      "num_shares" Integer,
      "num_likes" Integer
      );'''
conn.execute(sqlstr)
conn.commit()
Thailand.to_sql("Thailand",conn,if_exists='append',index=False)
conn.execute(sqlstr)
conn.commit()
sqlite=pd.read_sql('Select status_type,sum("num_reactions"),sum("num_comments"),sum("num_shares"),sum("num_likes") from "Thailand" group by status_type',conn);
print(sqlite)
conn.execute(sqlstr)
conn.commit()

f=["Reactions","Comments","Shares","Likes"]
label=[]
for i in range(4):
    label+=f

explode=[0,0,0,0]

fig, ax = plt.subplots(dpi=1000,figsize=(25,35))
size = 0.3

vals = np.array(sqlite)
link_sum=vals[0,1:5].sum()
photo_sum=vals[1,1:5].sum()
status_sum=vals[2,1:5].sum()
video_sum=vals[3,1:5].sum()
Sum_all=[link_sum,photo_sum,status_sum,video_sum]
v=vals[:,1:5]

labels=["Link","Photo","Status","Video"]

outer_colors = ["#DBE2EF","#3F72AF","#F9F7F7","#BFBFBF"]
inner_colors = ["#FFDEDE","#7878FF","#D6D6FF","#EDD4FF"]


ax.pie(Sum_all, radius=1-size,labels=labels,textprops={'fontsize': 50},
       colors=outer_colors,labeldistance=0.7,
       wedgeprops=dict(width=size, edgecolor='w'))
ax.legend(loc="upper right",fontsize=30)
ax.legend(fontsize=25)
ax.pie(v.flatten(), radius=1,textprops={'fontsize': 43},
       colors=inner_colors,labels=label,labeldistance=1.1,
       wedgeprops=dict(width=size, edgecolor='w'))

print(v.flatten())

ax.set_title("Thailand Live Sellers", fontdict={'fontsize':50, 'fontweight': 'medium'})
ax.set_axis_off()  
plt.show()

