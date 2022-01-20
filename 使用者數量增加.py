"""
"""
import matplotlib.pyplot as plt
import csv
import pandas as pd
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
fn='使用者增加數量FB2012-2020.csv'
with open(fn, encoding= 'utf8') as file:
          csvReader= csv.reader(file)
          listInput= list(csvReader) 

#a=日期b=使用人口
a=[]
b=[]
#每年使用人口相加 以免做出來的圖太大
for i in range(1,2077):
    a.append(listInput[i][0])
    b.append(listInput[i][6]) 

results=list(a)
result=list(map(int,b))
zipped=list(zip(result,results))

df=pd.DataFrame({'year':pd.to_datetime(results),'number of people':result})
year= list(map(int,df['year'].dt.year))
df0=pd.DataFrame({'year':year,"population":result})
c=df0.groupby(['year']).sum()


plt.figure(dpi=1000,figsize=(10,5))
plt.fill_between(c.index[0:9],c['population'],color='#3b5998')

plt.ylabel("Users activity record",fontsize=20)
plt.xlabel("Time line",fontsize=20)
plt.show()

year=np.array(year)
users=np.array(result)
x=pd.DataFrame(year,columns=["Year"])
y=pd.DataFrame(users,columns=["Users"])
lm = LinearRegression()
lm.fit(x,y)
print(lm.coef_)
print(lm.intercept_ )
new_year=pd.DataFrame(np.array([2021,2022]),columns=["Year"])
predict_users=lm.predict(new_year)
print(predict_users)