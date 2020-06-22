# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 20:12:10 2018

@author: YASH SAINI
"""

import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA

df=pd.read_csv('monthly-milk-production-pounds-p.csv')
df.columns=['Month','Milk in Pounds per Cow']
df.drop(168,axis=0,inplace=True)

""" 1) Visualizing the data"""
# convert index to timeseries
df['Month']=pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True) 
'''
print df.describe().transpose()

df['Milk in Pounds per Cow'].rolling(12).mean().plot(figsize=(10,8),label="12 Ma")
df['Milk in Pounds per Cow'].rolling(12).std().plot()
df['Milk in Pounds per Cow'].plot()
plt.legend()
plt.show()

result=seasonal_decompose(df['Milk in Pounds per Cow'],model='additive')
result.plot()
plt.show()
'''
""" 2) Make data Stationary"""

def make_stationary(time_series):
    df['First Difference']=time_series-time_series.shift(1)
    df['First Difference'].plot()
    adf_check(df['First Difference'].dropna())
    


def adf_check(time_series):
    r1=adfuller(time_series)
    print "Augmented Dicky-Fuller Test"
    labels=['ADF test stats','p-value','# of lags','# of observations used']
    for value,i in zip(r1,labels):
        print(i + ':' + str(value))
    if r1[1]<=0.05:
        print "Strong evidence against null hypothesis"
        print "reject null hypo"
        print "Data has no unit root and is stationary"
    else:
        print "Weak evidence against null hypothesis"
        print "Fail to reject null hypo"
        print "Data has  unit root and is NON-stationary"
        make_stationary(time_series)
adf_check(df['Milk in Pounds per Cow'])

# Now again check the adf to calculate 2nd difference
df['Second Difference']=df['First Difference']-df['First Difference'].shift(1)
adf_check(df['Second Difference'].dropna())

#For seasonal Difference
df['Seasonal Difference']=df['Milk in Pounds per Cow']-df['Milk in Pounds per Cow'].shift(12)
print ("********************************\n")
adf_check(df['Seasonal Difference'].dropna())

# For seasonal First difference

df['First Seasonal Difference']=df['First Difference']-df['First Difference'].shift(12)


''' 3) Autocorrelation plots and partial auto correlation plots'''

fig_first=plot_acf(df['First Seasonal Difference'].dropna())
plt.show()
fig_2=plot_pacf(df['First Seasonal Difference'].dropna())
plt.show()

""" 4) Construct ARIMA plot """
model=sm.tsa.statespace.SARIMAX(df['Milk in Pounds per Cow'],order=(0,1,0),seasonal_order=(1,1,1,12))
r2=model.fit()
print r2.summary()
# r2.resid :- signifies the residual value r2.resid.plot()

#Forecasting of known data
df['forecast']=r2.predict(start=150,end=250)
df[['Milk in Pounds per Cow','forecast']].plot(figsize=(10,8))
plt.show()

''' To add your own data (timestamps) (rows) in existing data we do the following'''
from pandas.tseries.offsets import DateOffset
future_dates=[df.index[-1]+ DateOffset(months=x) for x in range(1,24)]
future_df= pd.DataFrame(index=future_dates,columns=df.columns)

final_df= pd.concat([df,future_df])

""" 5) Predict unknown values """
    
final_df['forecast']=r2.predict(start=168,end=192)
final_df[['Milk in Pounds per Cow','forecast']].plot(figsize=(10,8))
plt.show()
