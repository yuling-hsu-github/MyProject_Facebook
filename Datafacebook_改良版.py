# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:27:05 2021

@author: user
"""
import matplotlib.pyplot as plt
import csv
import pandas as pd
fn='dataset_Facebook.csv'
with open(fn, encoding= 'utf8') as file:
          csvReader= csv.reader(file)
          listInput= list(csvReader) 
          df=pd.DataFrame(listInput)
col=['Page total likes','Type','Category',
     'Post Month','Post Weekday','Post Hour','Paid',
     'Lifetime Post Total Reach',
     'Lifetime Post Total Impressions',
     'Lifetime Engaged Users','Lifetime Post Consumers',
     'Lifetime Post Consumptions',
     'Lifetime Post Impressions by people who have liked your Page',
     'Lifetime Post reach by people who like your Page',
     'Lifetime People who have liked your Page and engaged with your post',
     'comment','like','share','Total Interactions']
'''一開始沒發現檔案都是; 且電腦轉不過dataframe所以 
之後到csv記事簿檔 取代掉就可以做使用 以避開一開始就使用dataframe做篩選的方式
以list先把兩個資料放一起再dataframe來做
將list裡的數轉成int然後整理totalike兩個搭配的'''
a=[]
b=[]
c=[]
d=[]
for i in range(1,501):
    # a.append(listInput[i][9])
    b.append(listInput[i][0])
    c.append(listInput[i][13])
    d.append(listInput[i][12])
results=list(map(int,a))
result=list(map(int,b))
result1=list(map(int,c))
result2=list(map(int,d))
zipped=list(zip(result,results))
zipped1=list(zip(result,results,result2))
df_Engaged=pd.DataFrame(zipped)
df_Engaged1=pd.DataFrame(zipped1)
#Reactions、Comment 、Share 、Post Click(都包括在裡面)
d=df_Engaged.groupby([0]).agg('mean')
# e=df_Engaged1.groupby([0]).agg('mean')


d.sort_index(ascending=True)
# e.sort_index(ascending=True)
plt.xlabel('Page total likes',fontsize=20)
plt.ylabel('Average Engaged users',fontsize=20)


plt.figure(figsize=(50,5))
# plt.figure(dpi=800)
plt.plot(d.index,d[1],'-o')
# ,d.index,d[2],'-o'
# x.index,x,'-o',color="#808cba"
plt.title('Impressions by people who have liked your Page & Post reach by people who like your Page',fontsize=25)
plt.grid()
plt.show()