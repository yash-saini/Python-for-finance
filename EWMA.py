# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:01:56 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
airline= pd.read_csv('AirPassengers.csv',index_col='Month',parse_dates=True)

""" Simple Moving Average"""
airline['6 Month MA'] = airline['#Passengers'].rolling(window=6).mean()
airline['12 Month MA'] = airline['#Passengers'].rolling(window=12).mean()
airline.plot(figsize=(10,8 ))
plt.show()

""" Exponential Weighted MA"""
airline['EWMA-12']=airline['#Passengers'].ewm(span=12).mean()
airline[['#Passengers','EWMA-12']].plot(figsize=(10,8))
plt.show()