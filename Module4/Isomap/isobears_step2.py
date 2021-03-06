
# coding: utf-8

# In[45]:

from sklearn.manifold import Isomap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
from mpl_toolkits.mplot3d import Axes3D
# get_ipython().magic(u'matplotlib inline')


# # Lab Assignment 5
# 
# Now that you've had your first taste of isomap, let's take your knowledge of it to the next level.
# 
# Whatever your high-dimensional samples are, be they images, sound files, or thoughtfully collected attributes, they can all be considered single points in a high dimensional feature-space. Each one of your observations is just a single point. Even with a high dimensionality, it's possible that most or all your samples actually lie on a lower dimension surface. Isomap aims to capture that embedding, which is essentially the motion in the underlying, non-linear degrees of freedom.
# 
# By testing isomap on a carefully constructed dataset, you will be able to visually confirm its effectiveness, and gain a deeper understanding of how and why each parameter acts the way it does. The ALOI, Amsterdam Library of Object Images, hosts a huge collection of 1000 small objects that were photographed in such a controlled environment, by systematically varying the viewing angle, illumination angle, and illumination color for each object separately. To really drive home how well isomap does what it claims, this lab will make use of two image sets taken from the ALOI's collection.
# 
# 

# <img src="./bear1.png" style="float:left"/> <img src="./bear2.png"/>

# Manifold extraction, and isomap specifically are really good with vision recognition problems, speech problems, and many other real-world tasks, such as identifying similar objects, or objects that have undergone some change. In the case of the 3D rotating object such as the office chair example from earlier, if every pixel is a feature, at the end of the day, the manifold surface is parametrizable by just the angle of the chair—a single feature!
# 
# 1.  Start by having a look through the Module4/Datasets/ALOI/ directory. There are two directories filled with 192 x 144 pixel images. Identify their ordering and try to figure out what's changing between the images. They might not be perfectly ordered, but that doesn't matter to isomap.
# 2.  Create a regular Python list object. Then, write a for-loop that iterates over the images in the Module4/Datasets/ALOI/32/ folder, appending each of them to your list. Each .PNG image should first be loaded into a temporary NDArray, just as shown in the Feature Representation reading.
# 
#     Optional: Resample your images down by a factor of two if you have a slower computer. You can also convert the image from  0-255  to  0.0-1.0  if you'd like, but that will have no effect on the algorithm's results.    
#     
# 
# 3.  Convert the list to a dataframe and run isomap on it to compute the lower dimensional embedding. Be sure to set n_components to 3 so you can visualize your manifold. You can also set the neighborhood size to six.
# 4.  Plot the first two manifold components using a 2D scatter plot, then plot the first three components using a 3D scatter plot. Run your assignment and then answer the questions below.

# In[22]:

bears = []
path = './Datasets/ALOI/32'
colors = []
for f in os.listdir(path):
    if '.png' in f:
        pic = mpimg.imread(os.path.join(path,f))
        bears.append(pic.flatten())
        colors.append('b')

path = './Datasets/ALOI/32i'
for f in os.listdir(path):
    if '.png' in f:
        pic = mpimg.imread(os.path.join(path,f))
        bears.append(pic.flatten())
        colors.append('r')


# In[23]:

bears[:2]


# In[25]:

bears = pd.DataFrame(bears)


# In[26]:

bears.shape

num_neighbors = 6

# In[29]:

iso = Isomap(n_components=3, n_neighbors=num_neighbors)
iso.fit(bears)
T = iso.transform(bears)

T.shape

isodf = pd.DataFrame(T, columns=['a', 'b', 'c'])

isodf.head()


fig1 = plt.figure(figsize=(12,10))
ax1 = fig1.add_subplot(111)
ax1.set_title("2D projection with {} neighbors".format(num_neighbors))
ax1.scatter(isodf.a, isodf.b, c=colors)


fig2 = plt.figure(figsize=(12,10))
ax2 = fig2.add_subplot(111, projection='3d')
ax2.set_title("3D projection with {} neighbors".format(num_neighbors))
ax2.scatter3D(isodf.a, isodf.b, isodf.c, c=colors)

plt.show()


