# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 15:03:14 2018

@author: YASH SAINI
"""

import datetime
import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import pandas_datareader as web
#Market index

spy_etf=web.DataReader("SPY","yahoo")
start=datetime.datetime(2014,1,4)
end=datetime.datetime(2017,7,25)
# Apple index
aapl=web.DataReader("AAPL",'yahoo',start,end)
aapl['Cumulative Return']=aapl['Close']/aapl.iloc[0]['Close']
spy_etf['Cumulative Return']=spy_etf['Close']/spy_etf.iloc[0]['Close']

spy_etf['Cumulative Return'].plot(label="SPY INDEX",figsize=(10,8))
aapl['Cumulative Return'].plot(label="Apple",figsize=(10,8))
plt.legend()
plt.show()

aapl['Daily Return']=aapl['Close'].pct_change(1)
spy_etf['Daily Return']=spy_etf['Close'].pct_change(1)

plt.scatter(aapl['Daily Return'],spy_etf['Daily Return'][:896:],alpha=0.25)


beta,alpha,r_value,p_value,std_err=stats.linregress(aapl['Daily Return'].iloc[1:],spy_etf['Daily Return'][:896:].iloc[1:])

# Creating Noise

noise=np.random.normal(0,0.001,len(spy_etf['Daily Return'][:896:].iloc[1:]))
fake_stock=spy_etf['Daily Return'][:896:].iloc[1:] + noise
plt.scatter(fake_stock,spy_etf['Daily Return'][:896:].iloc[1:])

beta,alpha,r_value,p_value,std_err=stats.linregress(fake_stock,spy_etf['Daily Return'][:896:].iloc[1:])
"""
If stock lines with the market we have beta close to 1 and really small alpha
"""
# Thus CAPM works as expected




