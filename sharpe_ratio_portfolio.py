# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:52:58 2018

@author: YASH SAINI
"""
import datetime
import numpy as np
import quandl
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
'''
start=datetime.datetime(2012,1,1)
end=datetime.datetime(2017,1,1)
aapl=quandl.get("WIKI/AAPL.11",start_date=start,end_date=end)
cisco=quandl.get("WIKI/CSCO.11",start_date=start,end_date=end)
ibm=quandl.get("WIKI/IBM.11",start_date=start,end_date=end)
amazon=quandl.get("WIKI/AMZN.11",start_date=start,end_date=end)
'''
print aapl.iloc[0]['Adj. Close']
for stock_df in (aapl,cisco,ibm,amazon):
    stock_df['Cumulative Return']=stock_df['Adj. Close']/stock_df.iloc[0]['Adj. Close']
    
''' 
30% portfolio in aapl
20% portfolio in cisco
40% in ibm
10% in amazon
'''
for stock_df,allo in zip((aapl,cisco,ibm,amazon),[0.3,0.2,0.4,0.1]):
    stock_df['Allocation']=stock_df['Cumulative Return'] * allo 
    #Normed return is cumulative daily return 
    
# Gives us an account of total price of stock on each day. if we consider each day to be 1million dollars
for stock_df in (aapl,cisco,ibm,amazon):
    stock_df['Position Values']=stock_df['Allocation'] * 1000000# investment of 1 million dollars

l=[aapl['Position Values'],cisco['Position Values'], ibm['Position Values'],amazon['Position Values']]
portfolio_val=pd.concat(l,axis=1)
portfolio_val.columns=['AAPL','CISCO','IBM','AMZn']
portfolio_val['Total pos']=portfolio_val.sum(axis=1)
portfolio_val.drop('Total pos',axis=1).plot(figsize=(10,8))
plt.legend()
plt.show()
portfolio_val.plot(figsize=(10,8))
plt.legend()
plt.show()
    
# Process to calculate sharpe ratio
portfolio_val['Daily Return']= portfolio_val['Total pos'].pct_change(1)
overall_cumulative_return= 100 * (portfolio_val['Total pos'][-1]/portfolio_val['Total pos'][0]-1)

SR=portfolio_val['Daily Return'].mean()/portfolio_val['Daily Return'].std()

# Annualized Sharpe Ratio = (252)^0.5 * SR (k=252 for daily returns)
ASR=((252)**0.5) * SR
print "Sharpe ratio is:",SR
print "/nAnnualized Sharpe ratio is:",ASR


