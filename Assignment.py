#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Sales Assignment
import numpy as np
import pandas as pd
import datetime as dt
df=pd.DataFrame(pd.read_excel("SaleData.xlsx"))
def least_sales(df):
    ls=df.groupby("Item")["Sale_amt"].min().reset_index()
    return ls
def sales_year_region(df):
    ls=df.groupby(['Region',df['OrderDate'].dt.year])["Sale_amt"].sum().reset_index()
    return ls
def days_diff(df,pre_date):
    df['Days_Diff']=(pd.to_datetime(df.OrderDate,dayfirst=True)-pd.to_datetime(pre_date,dayfirst=True)).dt.days
    return df
def mgr_slsmn(df):
    ls=pd.pivot_table(df,index=["Manager","SalesMan"])
    return ls
def slsmn_units(df):
    ls=pd.pivot_table(df,index=['Region'],values=['SalesMan','Units'],aggfunc={'SalesMan':len,'Units':[np.sum]})
    return ls
def sales_pct(df):
    ts=df['Units'].sum()
    df1=df.groupby(["Manager"])["Units"].sum()/ts*100
    return df1


# In[11]:


#IMDB Assignment

import numpy as np
import pandas as pd
df=pd.DataFrame(pd.read_csv("imdb.csv",error_bad_lines=False))
def fifth_movie(df):
    return(df.imdbRating[4])
def sort_df(df):
    df=df.sort_values(by="year",ascending=True)
    df=df.sort_values(by="imdbRating",ascending=False)
    return df
def subset_df(df):
    ls=df.loc[((df['duration']/60)>30) & ((df['duration']/60)<180)]
    return ls


# In[ ]:


#Diamonds Assignment

import numpy as np
import pandas as pd
df=pd.DataFrame(pd.read_csv("diamonds.csv"))
def dupl_rows(df):
    return(df.duplicated(subset=None, keep='first').count())
def drop_row(df):
    df.dropna(axis=0,how='any',subset=['carat','cut'],inplace=True)
    return df
def sub_numeric(df):
    df=df.select_dtypes(include=np.number)
    return df
def volume(df,x,y,z):
    if(df.depth>80):
        return(x*y*z)
    else:
        return(8)
def impute(df):
    if(len(df.price)==0):
        df.price=(df.price).mean()
    return df


# In[12]:


#Bonus Question 1

import numpy as np
import pandas as pd

d=pd.read_csv("imdb.csv",escapechar="\\")
df=pd.DataFrame(d)
def genre_com(df):
    df1=df.groupby("year").sum()
    df2=df1.loc[0:,'Action':'Western']
    df3=pd.DataFrame(df.year)
    df3['Genre_combo']=df2.apply(lambda x: ",".join(x.index[x>=1]),axis=1)
    df3['type']=df["type"].str.split(".", n = 1, expand = True)[1]
    df4=df.groupby('year').agg({'imdbRating': ['mean','min', 'max'],'duration':['sum']}).dropna()
    df4.columns=['avg_rating','min_rating','max_rating','total_run_time_mins ']
    return (pd.merge(df3,df4,on='year'))


# In[14]:


#Bonus Question 2

import numpy as np 
import pandas as pd

df=pd.DataFrame(pd.read_csv("imdb.csv",error_bad_lines=False))
def rel(df):
    df['len_title']=df.wordsInTitle.str.len()
    print(df[['len_title','imdbRating']].corr(method="spearman"))
    df1=df.groupby('year')['len_title'].agg([('min_len','min'),('max_len','max')]).reset_index()
    df2=pd.DataFrame(df.year)
    df2['vid_less_than_25Per']=(df.len_title < df.len_title.quantile(.25))
    df2['vid_25_50Per']=(df.len_title >= df.len_title.quantile(.25)) & (df.len_title <= df.len_title.quantile(.50))
    df2['vid_50_75Per']=(df.len_title >df.len_title.quantile(.50)) & (df.len_title <= df.len_title.quantile(.75))
    df2['videos_greater_than_75Per']=df.len_title > df.len_title.quantile(.75)
    df3=df2.groupby('year').sum().reset_index()
    df4=pd.merge(df1, df3, how ='inner', on ='year')
    return df4


# In[ ]:


#Bonus Question 5
import numpy as np
import pandas as pd

df=pd.DataFrame(pd.read_csv("imdb.csv",error_bad_lines=False))
def dec(df):
    df['Decile'] = pd.qcut(df['duration'], 10, labels=False)
    df.drop(df[['fn', 'tid', 'title', 'wordsInTitle', 'url', 'imdbRating',
                'ratingCount', 'duration', 'year', 'type','nrOfPhotos', 
                'nrOfNewsArticles', 'nrOfUserReviews','nrOfGenre']],axis=1,inplace=True)
    df1=df.groupby('Decile', sort=True).sum()
    df2=df[['Decile', 'nrOfWins', 'nrOfNominations']]
    df2=df.groupby('Decile').sum()
    df3=df1.drop(df1[['nrOfWins', 'nrOfNominations']],axis=1)
    df4 = pd.DataFrame(df3.columns.values[np.argsort(-df3.values, axis=1)[:, :3]],
                   index=df3.index,columns = ['Max_1','Max_2','Max_3'])
    return df4

