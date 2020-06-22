# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:03:55 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd

'''data1=quandl.get("NSE/IBULISL", authtoken="vYHnDsYFarRDC9L4J-5Q", start_date="2014-12-06")
df=pd.DataFrame(data1,index=data1.index) '''

df=pd.read_csv("NSE-IBULISL.csv",index_col='Date',parse_dates=True)

s=df.rolling(30).mean()
df['Turnover (Lacs)'].plot(figsize=(10,10))
s['Turnover (Lacs)'].plot()

#Legend
df['Turnover (Lacs) 30 Day MA']=df['Turnover (Lacs)'].rolling(30).mean()
df[['Turnover (Lacs) 30 Day MA','Turnover (Lacs)']].plot(figsize=(12,12))

# Avg of every thing before the current time stamp
df['Turnover (Lacs)'].expanding().mean().plot(figsize=(10,10))