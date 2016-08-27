
# coding: utf-8

# In[2]:

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# get_ipython().magic(u'matplotlib inline')
matplotlib.style.use('ggplot')


# In[4]:

# Here's a new one
from mpl_toolkits.mplot3d import Axes3D


# In[7]:

df = pd.read_csv('uci_concrete.csv')


# In[8]:

df.head()


# In[14]:

fig = plt.figure(figsize=(10,6))

plt.suptitle('Cement versus H2O versus Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Cement Content')
ax.set_ylabel('Water Content')
ax.set_zlabel('Strength')
ax.scatter(df.cement, df.water, df.strength, c='r', marker='o')



# In[15]:

fig = plt.figure(figsize=(10,6))

plt.suptitle('Cement versus Slag versus Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Cement Content')
ax.set_ylabel('Slag Content')
ax.set_zlabel('Strength')
ax.scatter(df.cement, df.slag, df.strength, c='g', marker='o')


# In[17]:

fig = plt.figure(figsize=(10,6))

plt.suptitle('Cement versus Fly Ash versus Concrete Strength')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Cement Content')
ax.set_ylabel('Fly Ash Content')
ax.set_zlabel('Strength')
ax.scatter(df.cement, df.slag, df.ash, c='b', marker='o')

# This doesn't work
# fig.show()
plt.show()
# In[ ]:



