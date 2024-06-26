#!/usr/bin/env python
# coding: utf-8

# ##### Count the number of perfect square numbers in a given range, range is take as input from user. 

# In[18]:


l = int(input("Enter the lower limit: "))
r = int(input("Enter the upper limit: "))
for i in range(l, r + 1):
    if (i**(.5) == int(i**(.5))):
        print(i, end=" ")


# ##### Generate the Pattern

# In[23]:


num = int(input("Enter the Number: "))

for i in range(0, num):
    for j in range(0, i+1):
        print("*", end="")
    print()
for i in range(1, num):
    for j in range(0, num-i):
        print("*", end="")
    print()


# ##### Take a number as input from user and display whether it is prime or not. 

# In[2]:


num = int(input("Enter the number: "))
if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

