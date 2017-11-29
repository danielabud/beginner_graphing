
# coding: utf-8

# In[19]:


#the goal of this project is to explore the popularity of certain
#majors with their respective income right out of college

import pandas as pd
import matplotlib as plt

get_ipython().magic('matplotlib inline')

recent_grads = pd.read_csv("recent-grads.csv")

#return the first row to see what it looks like
recent_grads.iloc[0]

#to get a better idea of what our data looks like, check out
#the head and the tail! Then some basic data with "describe"
recent_grads.describe()
recent_grads.head()
recent_grads.tail()


# In[13]:


#let's drop any blank rows for simplicity and to avoid errors in
#matplotlib. Only 1 row is dropped
raw_data_count = len(recent_grads)
print(raw_data_count)
recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads)
print(recent_grads_count)


# In[8]:


#this graph will essentially be a sideways normal distribution,
#since it shows incomes vs. their sample size - very large and
#very small incomes represent a small portion of the population,
#many standard deviations away, while the mean represents the largest
#sample size
recent_grads.plot(x='Sample_size', 
                  y='Median', 
                  kind='scatter', 
                  title='Sample size vs. Median', 
                  figsize=(5,10))

#very similar to the above graph,e xcept that this time with
#the unemployment rate
recent_grads.plot(x='Sample_size', 
                  y='Unemployment_rate', 
                  kind='scatter', 
                  title='Sample size vs. Unemployment', 
                  figsize=(5,10))

#not terribly insightful, as most jobs are full time
recent_grads.plot(x='Full_time', 
                  y='Median', 
                  kind='scatter', 
                  title='Full Time vs. Median', 
                  figsize=(5,10))

recent_grads.plot(x='ShareWomen', 
                  y='Unemployment_rate', 
                  kind='scatter', 
                  title='Share of Women vs. Unemployment Rate', 
                  figsize=(5,10))

recent_grads.plot(x='Men', 
                  y='Median', 
                  kind='scatter', 
                  title='Men vs. Median', 
                  figsize=(5,10))

recent_grads.plot(x='Women', 
                  y='Median', 
                  kind='scatter', 
                  title='Women vs. Median', 
                  figsize=(5,10))

recent_grads.plot(x='ShareWomen', 
                  y='Median', 
                  kind='scatter', 
                  title='Share of Women vs. Median', 
                  figsize=(5,10))

#sample size here represents how many people were majoring in
#a particular subject.
#Students in more popular majors DO NOT tend to earn more money.
#In fact, it seems that the most popular majors earn BELOW average.
#This could possibly be beacuse students follow their dreams rather
#than their paychecks - they will worry about that at a later age :)

#Students that majored in subjects that were majority female make
#less money - this is a very clear trend in the data. This is
#a well studied phenomenon.

#There seems to be little correlation between the number of 
#full-time employees and median salary, probably because most
#recent grads are full time employees.


# In[13]:


#To have more control over your histograms, use the following:
#recent_grads['Sample_size'].hist(bins=25, range=(0,5000))

cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]

#for i in cols:
#    recent_grads[i].plot(kind='hist', rot = 45)

#recent_grads['Sample_size'].plot(kind='hist')
#recent_grads['Median'].plot(kind='hist')
#recent_grads['Employed'].plot(kind='hist')
recent_grads['Full_time'].plot(kind='hist')
#recent_grads['ShareWomen'].plot(kind='hist')
#recent_grads['Unemployment_rate'].plot(kind='hist')
#recent_grads['Men'].plot(kind='hist')
#recent_grads['Women'].plot(kind='hist')

#It appears that predominantly-female majors are more common
#than predominantly male majors.
#The most common median salary range is about $30-$40k/yr


# In[19]:


#to rapidly look for stories in our data, we want to print out
#matrices to help us see correlation in our data. To really dive
#into the data, you will need to create more matrices!

from pandas.tools.plotting import scatter_matrix
scatter_matrix(recent_grads[['Sample_size', 'Median']], figsize=(10,10))

scatter_matrix(recent_grads[['Sample_size', 'Median','Unemployment_rate']], figsize=(10,10))


# In[17]:


recent_grads[:10].plot.bar(x='Major', y='ShareWomen')
recent_grads[163:].plot.bar(x='Major', y='ShareWomen')
recent_grads[:10].plot.bar(x='Major', y='Unemployment_rate')
recent_grads[163:].plot.bar(x='Major', y='Unemployment_rate')

#one thing I find pretty astounding from this data is the share
#that women make up for the 10 lowest-paying majors! They are almost
#exclusively filled by women


# In[26]:


#Just wanted to play around with hexbin plots!

import matplotlib.pyplot as plt

recent_grads.plot.hexbin(x='Unemployment_rate', y='Median', gridsize=20)

