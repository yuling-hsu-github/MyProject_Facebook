import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

data = pd.read_csv('pseudo_facebook.csv')
df=data.drop(columns=['userid','www_likes_received','dob_month','dob_day'],axis=1)
# print(df)


plt.figure(figsize=(10,6))
# 計算性別的數量 male:58574 female:40254 在facebook 上的使用占比
# df_gender = df.groupby(['gender']).size().reset_index(name='count')
# print(df_gender)
# gender=['Male','Female']
# explode=[0,0]
# plt.title("Gender Ratio", {"fontsize" : 18})  # 設定標題及其文字大小
# cmap=plt.colormaps["Accent"]
# color=cmap([0,1])
# # colors=['y','olive']
# plt.pie(df_gender['count'],labels=gender,colors=color,explode=explode,shadow=True ,autopct="%1.1f%%")
# plt.show()


# Donut chart

# fig, ax = plt.subplots()
# size = 0.4
# ax.pie(df_gender['count'], labels=gender,
#         radius=1-size, wedgeprops=dict(width=size,edgecolor='w'))
# plt.title("Gender Ratio")
# plt.savefig("High resoltion.png",dpi=300)
# plt.show()

#bar#看年齡分布主要
# df_age = df.groupby(['age']).size().reset_index(name='count')
# print(df_age)
# from bokeh.plotting import figure, show
# p=figure(plot_width=500,plot_height=500)
# # print(df_age['age'])
# p.vbar(df_age['age'],top=df_age['count'],bottom=0,color='orange',alpha=0.8,line_width=2)
# show(p)



#根據15-30這個段落去做分析 1-12
df=pd.read_csv('pseudo_facebook.csv')
print(df.columns)
mask=(df['age'].between(15,30))

df_birth=df.groupby(['dob_month']).size().reset_index(name='count')



label=[i for i in range(1,13)]
man=[]
woman=[]
print(df_birth)
print(sum(mask))

        

