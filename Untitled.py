#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Question 1 answer:



# In[ ]:


In [6]:
str = "what we think we become; we are python programmers."
sub = input("Enter the substring")
if str.count(sub)==0:
    print("No substring ")
else:
    print("The sub strings occured are at:")
    for i in range(len(str)-1):
        if (str[i]+str[i+1])==sub:
            print(i+1)
            i+=1


# In[ ]:


Enter the substringwe
The sub strings occured are at:
6
15
26


# In[ ]:


Question 2 answer:
islower()
case 1:

In [7]:
str1="Letsupgrade"
str1.islower()
Out[7]:
False
case 2:

In [8]:
str2="letsupgrade"
str2.islower()
Out[8]:
True
case 3:

In [9]:
str3="LetsUpgrade1"
str3.islower()
Out[9]:
False
case 4:

In [10]:
str4="12345"
str4.islower()
Out[10]:
False
case 5:

In [12]:
str5="LETSUPGRADE"
str5.islower()
Out[12]:
False
case 6:

In [19]:
str5="letsupgrade1"
str5.islower()
Out[19]:
True
isupper()
case 1:

In [11]:
str1="Letsupgrade"
str1.isupper()
Out[11]:
False
case 2:

In [17]:
str2="letsupgrade"
str1.isupper()
Out[17]:
False
case 3:

In [14]:
str3="LetsUpgrade1"
str3.isupper()
Out[14]:
False
case 4:

In [15]:
str4="12345"
str4.isupper()
Out[15]:
False
case 5:

In [16]:
str5="LETSUPGRADE"
str5.isupper()
Out[16]:
True
case 6:

In [18]:
str5="LETSUPGRADE1"
str5.isupper()
Out[18]:
True

