# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:49:11 2022

@author: psen
"""

#Greet the Customer
Greeting = input("Greet the customer ").lower()

x = Greeting.split()



#Check the Greeting

if x[0] == 'hello' or x[0] == 'hello,':
    print("$0")
elif x[0][0] =='h':
    print("$20") 
else:
    print("$100") 
      

