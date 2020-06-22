# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 15:00:58 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd

'''data1=quandl.get("NSE/IBULISL", authtoken="vYHnDsYFarRDC9L4J-5Q", start_date="2014-12-06")
df=pd.DataFrame(data1,index=data1.index) '''

df=pd.read_csv("NSE-IBULISL.csv",index_col='Date',parse_dates=True)

df['Turnover (Lacs) Mean']=df['Turnover (Lacs)'].rolling(20).mean()
df['upper']=df['Turnover (Lacs) Mean'] + 2*(df['Turnover (Lacs)'].rolling(20).std())

df['lower']=df['Turnover (Lacs) Mean'] - 2*(df['Turnover (Lacs)'].rolling(20).std())

df[['Turnover (Lacs)','Turnover (Lacs) Mean','upper','lower']].plot(figsize=(10,10))
