#!/usr/bin/env python
# coding: utf-8

# In[23]:


help("reduce")


# In[ ]:


"""
1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()

"""


# In[106]:


def My_reduce(func,b):
    a=b[0]                 # store first index value from list in a 
    
    for i in range(1,len(b)): 
        
        a=func(a,b[i])     #  calling the function
        
    return a
            


# In[107]:


# use of My_reduce function : 

lis=range(3)
My_reduce(lambda a,b:a+b,lis)


# In[108]:


# use of orignal reduce function : 
import functools 
lis=range(3)
print(functools.reduce(lambda a,b : a+b,lis))


# In[ ]:


"""
1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

"""


# In[95]:


# To Build my own Filter Function 
def my_filter(func,lt):
    empty=[]            # Emplty list
    for i in lt:
        if func(i):          # condition
           empty.append(i)  # adding element to the empty list   
    return empty             
    


# In[94]:


# use of My_filter function : 

lst=[1,2,3,4,5,6,7,8,9]
list(my_filter(lambda a: a+5,lst))


# In[98]:


# use of orignal filter function : 

lst=[1,2,3,4,5,6,7,8,9]
list(filter(lambda a: a+5,lst))


# In[ ]:





# In[42]:


"""

2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists

['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""


# In[99]:


print("Answer :-")
[str(j)*i for j in "xyz" for i in range(1,5)]


# In[102]:


print("Answer :-")
[str(i)*j for j in range(1,5) for i in "xyz"]


# In[103]:


print("Answer :-")
[[j for j in range(i,i+4)] for i in range(2,6)]


# In[104]:


print("Answer :-")
[[i+j] for j in range(1,4) for i in range(1,4)]


# In[105]:


print("Answer :-")
[(i,j) for j in range(1,4) for i in range(1,4)]


# In[ ]:




