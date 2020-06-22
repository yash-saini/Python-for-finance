# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 15:38:06 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd

'''data1=quandl.get("NSE/IBULISL", authtoken="vYHnDsYFarRDC9L4J-5Q", start_date="2014-12-06")
df=pd.DataFrame(data1,index=data1.index) '''

df=pd.read_csv("NSE-IBULISL.csv",index_col='Date',parse_dates=True)

""" df.set_index('Date', inplace=True) 
 as we need to set index to datetime object
"""
ds=df.resample('A').mean() #end date of month
ds1=df.resample('Q').mean() #quaterly 
 
def first_day(entry):
    return entry[0]
r=df.resample('A').apply(first_day)
df['Turnover (Lacs)'].resample('A').mean().plot(kind='bar')
print(ds)
print "***********************************"
print(ds1)
""" for shifting upwards df=df.shift(period=1) 
Here first entry becomes NAN"""
 
""" for shifting downwards df=df.shift(period=-1) 
here last entry becomes NaN"""

"""
To shift index not data we have df.tshift(freq='M') 
shifts indexes to last date of the month.""" 