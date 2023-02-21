#!/usr/bin/env python
# coding: utf-8

# In[25]:


#import packages in python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[2]:


#read globalsuperstore dataset
file=pd.read_excel('Global superstore.xls')
file.head()


# In[3]:


#check the null value from dataset
file.isnull().sum()


# In[4]:


#delete the null value column postal code
file=file.drop(columns=['Postal Code'])
file.head()


# In[5]:


#check the null value column delete or not 
file.isnull().sum()


# In[6]:


# to display statistics about data
file.describe()


# In[7]:


# to display basic info datatype
file.info()


# In[8]:


#to display no of sample on each class
file['Segment'].value_counts()


# In[21]:


#to display 
a=file['Region']
b=file['Shipping Cost']
plt.xlabel('Region')
plt.ylabel('Shipping Cost')
plt.title("REGION WISE SHIPPING COST")
plt.barh(a,b)


# In[10]:


#pie chart
#change sales datatype float to int 
file['Sales'] = file['Sales'].astype(int)
display(file.dtypes)


# In[19]:


#PIE CHART
d=file['Sales']
e= d.head(n=5)
f=file['Segment']
g=f.head(n=5)


# In[20]:


plt.title("SEGMENT WISE SALES")
plt.pie(e,labels=g)


# In[22]:


#scatter plot
#change Profit datatype float to int 
f=file['Sub-Category']
file['Profit'] = file['Profit'].astype(int)
display(file.dtypes)
g=file['Profit']


# In[14]:


plt.scatter(g,f)
plt.title("SUB-CATEGORY WISE PROFIT")
plt.xlabel("Sub-Category")
plt.ylabel("Profit")
plt.show()


# In[17]:


#line chart
x=file['Sales']
b= x.head(n = 6)
y=file['City']
a=y.head(n=6)
plt.title("CITY WISE SALES")
plt.plot(a,b)


# In[24]:


z=("THANK YOU")
print(z)


# In[ ]:




