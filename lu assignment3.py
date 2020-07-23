#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Enter the value of n: "))
hold = num
sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1;
    # displaying output
    print("Sum of first", hold, "natural numbers is: ", sum)


# In[ ]:


num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  

