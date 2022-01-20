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
df=pd.DataFrame(listInput,columns=col).drop([0],axis=0)
#drop調不需要的列和欄
df_type=df.groupby('Type')
Totallink=sum(df_type.groups['Link'])
Totalphoto=sum(df_type.groups['Photo'])
Totalstatus=sum(df_type.groups['Status'])
Totalvideo=sum(df_type.groups['Video'])

df["like"].values.tolist()
df["comment"].values.tolist()
df["share"].values.tolist()
df["Total Interactions"].values.tolist()

list_like = list(map(int,df["like"]))

網路討論度高的成本
a=df['Lifetime Engaged Users'][1:500]
df_like = df.groupby(['Page total likes',int('Lifetime Engaged Users')]).size().reset_index(name='count')




import matplotlib.pyplot as plt
import csv
import pandas as pd
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

label=["Reactions","Comments","Shares","Likes"]
size=sqlite.index[0][:]
explode=[0,0,0,0]
plt.pie(size,explode=explode,labels=label)
plt.show()
#進度



#印出photo link
df2_type=df2.groupby('status_type')
print(len(df2_type.get_group("link")))
print(len(df2_type.get_group("photo")))
print(len(df2_type.get_group("video")))
#分別劃出出photo link vedio起的作用以comment的不同曝光率來說(share/comment/reaction/like)
import pandas as pd
import numpy as np
data = pd.read_csv('pseudo_facebook.csv')
#希望可以drop掉很多)的資料以求準確定
df=data.drop(columns=['userid','www_likes_received','dob_month','dob_day'],axis=1)
print(df)
names = ['link', 'photo', 'video']
values = [len(df2_type.get_group("link")),len(df2_type.get_group("photo")),len(df2_type.get_group("video"))]
values2 = [Totallink, Totalphoto,Totalstatus,Totalvideo]
name2=['Link','Photo','Status','Video']
explode=[0,0,0,1]
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.bar(names, values,color='#3b5998')
# plt.subplot(132)
# plt.scatter(names, values,color='#3b5998')
plt.subplot(122)
plt.pie(values2,labels=name2,colors=['#3b5998','#9BAF8E','#AEBBC7','#C1D2D6'],explode=explode)
plt.suptitle('The ratio that which way could attract people most')

plt.legend()
plt.show()


#看比例photo拿到的讚和其他兩個比較 list14
df_likecomparison = df.groupby(df['Type']).sum("Lifetime People who have liked your Page and engaged with your post")

