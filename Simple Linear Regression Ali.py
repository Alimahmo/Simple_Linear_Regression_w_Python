#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Import the relevant libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
#the library for running regressions
import seaborn as sns
sns.set()      # sets a default theme, to override Matplotlib style

### Load the data
data = pd.read_csv('1.01. Simple linear regression.csv')
data
data.describe()

 
  
### Define the dependent and independent variables

y = data ['GPA']
x1 = data ['SAT']


### Explore the data
plt.scatter(x1,y)
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

### Regression itself

x = sm.add_constant(x1)       
# this “Method” defines x0 within itself which equals to 1
results = sm.OLS(y,x).fit()    
# results will contain the output of the Ordinary Least Squares regression
# fit()will apply a specific estimation technique (OLS here) to obtain the fit of the model
results.summary()


  
### Let’s plot the Regression Line

plt.scatter(x1,y)
yhat = 0.0017*x1 + 0.275
fig = plt.plot(x1,yhat, lw=4, c='orange', label ='regression line')
#lw:line width; c:color
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()


  
### The Null Hypothesis (H0)
### b = 0
### Answers: is this a useful variable?

plt.scatter(x1,y)
yhat = 0.0017*x1 + 0      # What if the Coefficient of Intercept (b0) was Zero?
fig = plt.plot(x1,yhat, lw=4, c='green', label ='regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.xlim(0)
plt.ylim(0)    #to also see the origin of the plot
plt.show()

plt.scatter(x1,y)
yhat = 0*x1 + 0.275          # What if the Coefficient of Indpndnt Var (b1) was Zero?
fig = plt.plot(x1,yhat, lw=4, c='red', label ='regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()


# In[ ]:




