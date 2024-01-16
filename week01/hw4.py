#!/usr/bin/env python
# coding: utf-8

# In[7]:


x = input() 
x = int(x)
y = input() 
y = int(y)
z = input() 
z = int(z)
sum = x+y+z
maximum = max(x,y,z)
minimum = min(x,y,z)
mid = sum - maximum - minimum
print(minimum,mid,maximum)

