#!/usr/bin/env python
# coding: utf-8

# <h1>Based on the data provided, are scarce resources and socio-economic instability one of the leading cause of illness and death in developing countries?</h1>

# In[69]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[70]:


df = pd.read_csv("cause_of_deaths.csv")


# In[71]:


df.describe()


# In[72]:


df.shape


# In[73]:


df.dtypes


# In[76]:


df.rename(columns={'Country/Territory': 'Country'},
                         inplace=True)


# In[77]:


common_diseases = ['Malaria','HIV/AIDS','Tuberculosis',]


# In[78]:


for i in common_diseases:
    if df[i].dtypes != 'string':
        print(i)
        data = df.groupby(['Country'])[i].sum().sort_values(ascending =False)[:5]
        
        plt.figure(figsize=(12,6))
        plt.bar(data=data ,x = data.index , height = data.values, width=0.8, color = ['purple','crimson','green', 'yellow', 'magenta'])
        plt.xticks(rotation='vertical')
        plt.xlabel("Countries" , size = 10)
        plt.ylabel(i.upper()+'Totl deaths in Thousands')
        plt.title("COUNTRIES WITH HIGHEST "+ i.upper()+' DEATHS')
        


# In[79]:


import plotly.express as px


# In[83]:


for i in common_diseases:
    if df[i].dtypes != 'string':
        print(i)
        data = df.groupby(['Country'])[i].sum().sort_values(ascending =False)[:5]
        fig = px.scatter(x=df["Country"], y=df["Malaria"])
        fig.show()
       


# <p1>From the above viusalizations/charts, we can see that in other areas of the world, diseases like Malaria, HIV/AIDS,Tuberculosis are less prominent cause of death in developed countries like USA, Portugal, etc. These devloped countries have abundant resources and a stable economy to provide better healthcare to their citizens. We can also see from the charts that underdeveloped/developing or highly populated countries with high transmission rates have a higher number of reported cases or deaths due to the lack of resources and socio-economic instability have hindered efficient health control activities.<\p2>
