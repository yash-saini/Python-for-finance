# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:33:28 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

airline= pd.read_csv('AirPassengers.csv',index_col='Month',parse_dates=True)
airline.dropna(inplace=True)
''' Choosing of model is done on seeing the graph (# passengers on x axis),
 if its linear then additive else mul'''
result=seasonal_decompose(airline['#Passengers'],model='multiplicative')

'''          result.seasonal.plot()
             result.trend.plot()
'''
result.plot()
#Residual refers to the part no explained by trend or seasonality