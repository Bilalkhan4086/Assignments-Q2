#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[2]:


import numpy as np


# 2. Create a null vector of size 10 

# In[3]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[10]:


find = np.arange(10,50)
print(find)


# 4. Find the shape of previous array in question 3

# In[11]:


find.shape


# 5. Print the type of the previous array in question 3

# In[13]:


find.dtype


# 6. Print the numpy version and the configuration
# 

# In[21]:


print("Version = ",np.__version__)
print("Config",np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[22]:


find.ndim


# 8. Create a boolean array with all the True values

# In[27]:


find.astype(bool)


# 9. Create a two dimensional array
# 
# 
# 

# In[28]:


np.random.randn(10,20)


# 10. Create a three dimensional array
# 
# 

# In[29]:


np.random.randn(2,3,4)


# Difficulty Level **Easy**
11. Reverse a vector (first element becomes last)
# In[38]:


find[::-1]

12. Create a null vector of size 10 but the fifth value which is 1 
# In[43]:


arr = np.zeros(10)
arr[4] = 1
arr


# 13. Create a 3x3 identity matrix

# In[48]:


np.identity(3)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[51]:


arr.astype('float')


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[53]:


arr1 = np.array([[1., 2., 3.],

            [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],

           [7., 2., 12.]])
arr3 = arr1 * arr2
arr3


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[59]:


arr4 = arr1,arr2
np.array(arr4)


# 17. Extract all odd numbers from arr with values(0-9)

# In[76]:


od = np.arange(10)
od[od%2 == 1]


# 18. Replace all odd numbers to -1 from previous array

# In[74]:


od = np.arange(10)
od[od % 2 == 1] = -1
od


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[79]:


arr5 = np.arange(10)
arr5[4:8] = 12
arr5


# 20. Create a 2d array with 1 on the border and 0 inside

# In[103]:


x = np.ones(16).reshape(4,4)
x[1,1:3] = 0
x[2,1:3] = 0
x


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[105]:


arr2d = np.array([[1, 2, 3],

            [4, 5, 6], 

            [7, 8, 9]])

arr2d[1,1] = 12
arr2d


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[106]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0,0] = 64
arr3d


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[109]:


a2d = np.arange(9).reshape(3,3)
a2d[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[111]:


a2d[1,1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[114]:


st = a2d[0,2]
nd = a2d[1,2]
rd = st,nd
rd


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[122]:


values = np.random.randn(100).reshape(10,10)
print(values)
maxi = values.max()
mini =values.min()
print('maximum Value is =',maxi ,'and minimum value =',mini)

27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
---
Find the common items between a and b

# In[138]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
com = np.intersect1d(a,b)
com


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[244]:


np.searchsorted(a , np.intersect1d(a,b))


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[249]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data[names != 'Will'])
# data


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[250]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data[names == 'Bob'])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[142]:


a = np.arange(16)
b = a[a != 0 ]
c = b.reshape(5,3)
c

32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.
# In[180]:


a = np.arange(17)
b = a[a != 0 ]
c = b.reshape(2,2,4)
c


# 33. Swap axes of the array you created in Question 32

# In[187]:


c.swapaxes(2,0)


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[208]:


s = np.array([0,1,2,3,4,5,6,7,8,9])
sq =np.sqrt(s)
res = sq[ sq > 0.5]
rep = 


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[242]:


y = np.arange(12).reshape(3,4)
z1 = np.max(y[0])
z2 = np.max(y[1])
z3 = np.max(y[2])
print(z1)
print(z2)
print(z3)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[227]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
res = np.unique(names)
res

37. a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

---
From array a remove all items present in array b


# In[221]:


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
diff = np.setdiff1d(a,b)
diff


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[216]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
sampleArray[2] = newColumn
sampleArray


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[214]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
prod = np.dot(x,y)
prod


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[213]:


mat = np.arange(20).reshape(4,5)
matrix = np.cumsum(mat)
matrix

