#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[3]:


import numpy as np
a = np.arange(10).reshape(2,5)
a


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[10]:


a = np.arange(10).reshape(2,5).astype('int32')
b = np.ones(10).reshape(2,5).astype('int32')
c = np.vstack((a,b))
c


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[7]:


d = np.hstack((a,b))
d


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[11]:


e = a.flatten()
e


# # Question:5
### How to Convert higher dimension into one dimension?
# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[13]:


f = np.arange(15).reshape(3,5)
g = f.reshape(1,15)
g


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[16]:


g.reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[19]:


h = np.arange(25).reshape(5,5)
np.square(h[2])


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[21]:


i = np.arange(25).reshape(5,5)
np.mean(i)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[91]:


print("Standard deviation of Array: \n")
print(np.std(i))


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[90]:


np.median(i)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[69]:


i.T


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[80]:


arr = np.arange(1,17).reshape(4,4)
np.diag(arr).sum()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[81]:


from numpy.linalg import det
det(arr)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[85]:


ar = np.arange(1,21).reshape(4,5)
print(f"5th percentile of array: {np.percentile(ar, 5)}")
print(f"95th percentile of array: {np.percentile(ar, 95)}")


# ## Question:15

# # How to find if a given array has any null values?

# In[88]:


na = np.random.randn(4,4)
ma = np.sqrt(na)
check = np.isnan(ma).any()
check

