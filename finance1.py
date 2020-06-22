# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 00:13:09 2018

@author: YASH SAINI
"""
import quandl
import pandas_datareader.data as web
from pandas_datareader import Options
import datetime
start=datetime.datetime(2015,1,1)
end=datetime.datetime(2017,1,1)
f=web.DataReader('FB','yahoo',start,end)
'''fb_options=Options('FB','google')
options_df=fb_options.get_options_data(expiry=fb_options.expiry_dates[0])
'''
mydata=quandl.get("EIA/PET_RWTC_D")
data1=quandl.get("WIKI/AAPL")
data1=quandl.get("WIKI/AAPL.1") # for first column