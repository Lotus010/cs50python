# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:04:17 2022

@author: psen
"""
#Intialize dict and list
grocery = {}
item = []

#Get input in item and sort
while True:
    try:
        item.append(input("Item: ").upper())             
    except EOFError:
        print()
        break
item.sort() 

#Add item in dictionary with value as 1
for i in range(len(item)):
    grocery[item[i]] = 1
    
#check duplicates and increment values with one 
last =''
for key in grocery:    
    if grocery[key] == last:
       new = {key:str(int(grocery[key])+1)} 
       grocery.update(new)        
    
    last = grocery[key]  
    
#Print grocery dictionary values and keys    
for key in grocery:  
    print(grocery[key],key)
  
    