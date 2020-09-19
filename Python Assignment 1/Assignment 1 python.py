#!/usr/bin/env python
# coding: utf-8

# # Que 1
# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# 

# In[5]:


a=2000
b=3200
for i in range(a,b):
    if i%7==0 and i%5!=0:
        print(i)
        
    


# # Que 2
# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[9]:


a=input("Enter the first Name :- ")
b=input("Enter the last Name :- ")
print("Name in Reverse Order :-",b+ " " +a)


# # Que 3
# 3. Write a Python program to find the volume of a sphere with diameter 12 cm.
#    
#    Formula: V=4/3 * π * r 3

# In[18]:


import math
d=int(input("Enter the value of Diameter :- "))
r=d/2
V=(math.pi)*4/3*(r**3)
print("Volume of Sphere :-",V)


# In[ ]:





# In[ ]:




