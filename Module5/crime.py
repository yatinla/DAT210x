from __future__ import print_function
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import matplotlib
# get_ipython().magic(u'matplotlib inline')


# In[2]:



# In[3]:

from sklearn.cluster import KMeans
import pandas as pd
import numpy as np


# In[4]:

# %load assignment1.py
#
# TOOD: Import whatever needs to be imported to make this work
#
# .. your code here ..


matplotlib.style.use('ggplot') # Look Pretty


# In[ ]:

#
# TODO: To procure the dataset, follow these steps:
# 1. Navigate to: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present/ijzp-q8t2
# 2. In the 'Primary Type' column, click on the 'Menu' button next to the info button,
#    and select 'Filter This Column'. It might take a second for the filter option to
#    show up, since it has to load the entire list first.
# 3. Scroll down to 'GAMBLING'
# 4. Click the light blue 'Export' button next to the 'Filter' button, and select 'Download As CSV'

def doKMeans(df):
    #
    # INFO: Plot your data with a '.' marker, with 0.3 alpha at the Longitude,
    # and Latitude locations in your dataset. Longitude = x, Latitude = y
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(df.Longitude, df.Latitude, marker='.', alpha=0.3)

    #
    # TODO: Filter df so that you're only looking at Longitude and Latitude,
    # since the remaining columns aren't really applicable for this purpose.
    #
    # .. your code here ..
    longlat = df[['Longitude','Latitude']]
    #
    # TODO: Use K-Means to try and find seven cluster centers in this df.
    #
    # .. your code here ..
    kmeans_model = KMeans(n_clusters=7)
    kmeans_model.fit(longlat)
    print ("kmeans_model intertia_ = {}".format(kmeans_model.inertia_))
    #
    # INFO: Print and plot the centroids...
    centroids = kmeans_model.cluster_centers_
    print ("Centroids: {}".format(centroids))
    ax.scatter(centroids[:,0], centroids[:,1], marker='x', c='red', alpha=0.5, linewidths=3, s=169)
    print (centroids)


# In[6]:

#
# TODO: Load your dataset after importing Pandas
#
# .. your code here ..
#
# Read my fixed-up version
crime = pd.read_csv('Datasets/ChicagoGamblingCrimes.csv')


# In[7]:

crime.shape


# In[8]:

#
# TODO: Drop any ROWs with nans in them
#
# .. your code here ..
#
# Read my fixed up version with datetime

# crime = crime.dropna(axis=0)
crime = crime.dropna(axis=0)


# In[9]:

crime.shape


# In[10]:

#
# TODO: Print out the dtypes of your dset
#
# .. your code here ..
col_types = pd.DataFrame({'Column':crime.columns.tolist(), 'Type':[crime[c].dtype for c in crime.columns]})
col_types


# In[11]:

#
# Coerce the 'Date' feature (which is currently a string object) into real date,
# and confirm by re-printing the dtypes. NOTE: This is a slow process...
#
# .. your code here ..
crime.loc[0,'Date']


# In[12]:

pd.to_datetime('01/14/2004 10:00:00 PM', format="%m/%d/%Y %I:%M:%S %p")
crime.Date = pd.to_datetime(crime.Date, format="%m/%d/%Y %I:%M:%S %p")
crime.Date.dtype


# In[16]:

# crime.to_csv('crime_with_datetime.csv', index=False)


# In[15]:

crime.head()


# In[32]:

# Need to drop outliers
lat_mean = crime.Latitude.mean()
lat_std = crime.Latitude.std()
long_mean = crime.Longitude.mean()
long_std = crime.Longitude.std()
print (lat_mean)
print (lat_std)
print (long_mean)
print (long_std)


# In[33]:

crime = crime[abs(crime.Longitude - long_mean) < 4*long_std]


# In[34]:

crime.shape


# In[35]:

crime = crime[abs(crime.Latitude - lat_mean) < 4*lat_std]


# In[36]:

crime.shape


# In[43]:

# INFO: Print & Plot your data
doKMeans(crime)


# In[38]:

#
# TODO: Filter out the data so that it only contains samples that have
# a Date > '2011-01-01', using indexing. Then, in a new figure, plot the
# crime incidents, as well as a new K-Means run's centroids.
#
# .. your code here ..

df = crime[crime.Date > pd.to_datetime('2011-01-01')]


# In[39]:

df.shape


# In[40]:

# INFO: Print & Plot your data
doKMeans(df)
plt.show()


# In[ ]:



