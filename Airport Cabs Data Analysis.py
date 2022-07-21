#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


taxi = np.genfromtxt('D:\\DstaSet\\nyc_taxis.csv', delimiter=',', skip_header=True)


# In[15]:


speed = taxi[:,7]/(taxi[:,8]/3600)


# # Calculate The MEAN SPEED

# In[16]:


mean_speed = speed.mean()
print(mean_speed)


# # No. of Rides in the Month of February

# In[17]:


rides_feb = taxi[taxi[:,1] == 2, 1]
print(rides_feb.shape[0])


# # No. of rides with tip greater than $50

# In[19]:


print(taxi[taxi[:,-3] > 50,-3].shape[0])


# # No. of Rides where drop was JFK Airport code:2

# In[20]:


print(taxi[taxi[:,6] == 2,6].shape[0])


# In[ ]:




