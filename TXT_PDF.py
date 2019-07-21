
# coding: utf-8

# In[21]:


import pandas as pd
import glob


# In[96]:


path = r'\csv' # use your path
all_files = glob.glob(path + "/*.txt")


# In[98]:


li = []
for filename in all_files:
    df = pd.read_csv(filename)
    li.append(df)


# In[99]:


frame = pd.concat(li, axis=0, ignore_index=True)


# In[101]:


frame.to_csv("Email.csv")

