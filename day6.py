#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[1,2,3,4,5,7,8]
list2= ["a","b","c","d","e"]
res = {}
for key in list1:
     for value in list2:
      res[key] = value
      list2.remove(value)
        break 


# In[ ]:



print ("dictionary output is : " + str(res))
dictionary output is : {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

