# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:04:57 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import statsmodels.api as sm

df=sm.datasets.macrodata.load_pandas().data
df.set_index('year', inplace=True)
# or use df.index=pd.Index(sm.tsa.datetools.dates_from_range('1959Q1','2009Q3'))
# (sm.datasets.macrodata.NOTE)

gdp_cycle,gdp_trend= sm.tsa.filters.hpfilter(df['realgdp'])
df['trend']=gdp_trend
df[['realgdp','trend']].plot(figsize=(10,8))
plt.legend()
plt.show()
