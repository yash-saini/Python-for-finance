# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 19:12:26 2018

@author: YASH SAINI
"""
""" In this file we are interested in finding which all portfolio values 
have the best sharpe ratio. 
Monte Carlo simulation :- Random values
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
# 1) Random assignment of portfolios
stocks=pd.concat([aapl['Adj. Close'],cisco['Adj. Close'],ibm['Adj. Close'],amazon['Adj. Close']],axis=1)
stocks.columns=['aapl','cisco','ibm','amazon']
print stocks.pct_change(1).mean()
print stocks.pct_change(1).corr()

""" Log return """
log_ret= np.log(stocks/stocks.shift(1))
log_ret.hist(bins=100,figsize=(10,8))
plt.tight_layout()
plt.show()
# covariance of log_ret

log_ret.cov()

log_ret.cov()* 252
""" For only once run this, to generate random values 
    We need loops to run this 
"""

"""
np.random.seed(101)
weights= np.array(np.random.random(4))

print (" /n Rebalance weights:= :")
weights = weights/np.sum(weights)
print weights
# Expected return
exp_ret=np.sum((log_ret.mean()*weights)*252)
print "Expected return", exp_ret
#Expected Volatility
exp_vol=np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
print "Expected volatility", exp_vol
#sharpe ratio
print "/n Sharpe ratio "
SR=exp_ret/exp_vol
print SR
"""
'''
np.random.seed(101)
num_ports=5000
all_weights=np.zeros((num_ports,len(stocks.columns)))
ret_arr=np.zeros(num_ports)
vol_arr=np.zeros(num_ports)
sharpe_arr=np.zeros(num_ports)

for ind in range(num_ports):
    weights= np.array(np.random.random(4))


    weights = weights/np.sum(weights)
    all_weights[ind,:]=weights
    
    # Expected return
    ret_arr[ind]=np.sum((log_ret.mean()*weights)*252)
    
    #Expected Volatility
    vol_arr[ind]=np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
    
    #sharpe ratio
    
    sharpe_arr[ind]=ret_arr[ind]/vol_arr[ind]
print "/nMAx sharp ratio is" , sharpe_arr.max()
print"/n Values at max sharp ratio are:", all_weights[sharpe_arr.argmax(),:]

plt.figure(figsize=(10,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')

plt.colorbar(label="sharpe ratio")
plt.xlabel('Volatility')
plt.ylabel('Return')
#MAx sharpe ratio
plt.scatter(vol_arr[sharpe_arr.argmax()],ret_arr[sharpe_arr.argmax()],c='purple',s=50)
'''




""" Optimization of weights"""
def get_ret_vol_sr(weights):
    weights=np.array(weights)
    ret=np.sum((log_ret.mean()*weights)*252)
    vol=np.sqrt(np.dot(weights.T,np.dot(log_ret.cov()*252,weights)))
    sr=ret/vol
    return np.array([ret,vol,sr])
from scipy.optimize import minimize

def neg_sharpe(weights):
    return get_ret_vol_sr(weights)[2] * (-1)
def check_sum(weights):
    # return 0 if sum of weights is 1
    return np.sum(weights) - 1
cons=({'type':'eq','fun':check_sum})
bounds=((0,1),(0,1),(0,1),(0,1))
initial_guess=[0.25,0.25,0.25,0.25]
opt_results= minimize(neg_sharpe,initial_guess,method="SLSQP",bounds=bounds,constraints=cons)

print "return, volatility and sharpe ratios are:" ,get_ret_vol_sr(opt_results.x)
#Efficient frontier (lowest risk)

''' since the graph from random allocation is from 0-0.3 we do the following'''
frontier_y=np.linspace(0,0.3,100)
def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]
frontier_volatility=[]
for possible_return in frontier_y:
    cons=({'type':'eq','fun':check_sum},({'type':'eq','fun':lambda w:get_ret_vol_sr(w)[0]-possible_return}))
    results=minimize(minimize_volatility,initial_guess,method="SLSQP",bounds=bounds,constraints=cons)
    frontier_volatility.append(results['fun'])
    
''' frontier plot'''
plt.figure(figsize=(10,8))
plt.scatter(vol_arr,ret_arr,c=sharpe_arr,cmap='plasma')

plt.colorbar(label="sharpe ratio")
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.plot(frontier_volatility,frontier_y,'g--',linewidth=3)
#MAx sharpe ratio
plt.scatter(vol_arr[sharpe_arr.argmax()],ret_arr[sharpe_arr.argmax()],c='purple',s=50)
plt.show()



