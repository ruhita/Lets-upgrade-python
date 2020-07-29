#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Key to value and value to key"""
port1 = {21:"FTP",22:"SSH",23:"telnet",80:"http"} 
port2 ={value:key for key,value in port1.items()}
print("The output:",port2)


# In[ ]:



"""sum of tuple in the list"""
list1=[(1,2),(3,4),(5,6),(4,5)]
res=[]
for each in range(0,len(list1)):
    a,b=list1[each]
    res.append(a+b)
print(res)
[3, 7, 11, 9]
In [40]:
"""making as one list"""
list1=[(1,2,3),[1,2],['a','hit','less']]
list2=[]
list2=[i for each in list1 for i in each]
print (list2)
[1, 2, 3, 1, 2, 'a', 'hit', 'less']

